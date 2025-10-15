# --- IMPORTS ---
# pandas is for data manipulation (like Excel in Python).
import pandas as pd
# We need our database models and session factory.
from database import SessionLocal, Product, UserInteraction, User
# scikit-learn is the machine learning library we use for the text analysis.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- RECOMMENDATION FUNCTION ---
# It takes a user_name and returns a list of recommended products and the user's last purchase.
def get_user_profile_recommendations(user_name: str, num_recommendations: int = 2):
    # Start a new database session.
    db = SessionLocal()
    try:
        # Step 1: Find the user in the database by their name.
        user = db.query(User).filter(User.name == user_name).first()
        if not user:
            return [], None # If user doesn't exist, we can't recommend anything.
        
        user_id = user.id

        # Step 2: Load data into pandas DataFrames for easier processing.
        products_df = pd.read_sql(db.query(Product).statement, db.bind)
        interactions_df = pd.read_sql(db.query(UserInteraction).filter(UserInteraction.user_id == user_id).statement, db.bind)

        if interactions_df.empty:
            return [], None # If the user has no history, we can't recommend.

        # Step 3: Build a "user profile" based on their interaction history.
        # Get the IDs of all products the user has interacted with.
        user_product_ids = interactions_df['product_id'].tolist()
        # Get the full details of those products.
        user_products = products_df[products_df['id'].isin(user_product_ids)]
        # Combine all the descriptions of these products into one giant string. This represents the user's "taste".
        user_profile = ' '.join(user_products['description'])

        # Step 4: Use TF-IDF to convert text into numbers.
        # This algorithm turns words into vectors, giving more weight to important words.
        tfidf = TfidfVectorizer(stop_words='english')
        # Create a list of all product descriptions plus the user's taste profile at the end.
        all_text = products_df['description'].tolist() + [user_profile]
        # Analyze the text and create a matrix of vectors.
        tfidf_matrix = tfidf.fit_transform(all_text)
        
        # Separate the product vectors from the user's taste vector.
        product_matrix = tfidf_matrix[:-1]
        user_profile_vector = tfidf_matrix[-1]
        
        # Step 5: Calculate Cosine Similarity.
        # This measures the angle between the user's taste vector and each product vector.
        # A smaller angle (closer to 1) means the product is a better match.
        cosine_sim = cosine_similarity(user_profile_vector, product_matrix)

        # Sort the products by their similarity score in descending order.
        sim_scores = sorted(list(enumerate(cosine_sim[0])), key=lambda x: x[1], reverse=True)
        
        # Step 6: Get the top recommendations, excluding items the user already interacted with.
        recommended_indices = [i[0] for i in sim_scores if products_df.iloc[i[0]]['id'] not in user_product_ids][:num_recommendations]
        recommended_products = products_df.iloc[recommended_indices].to_dict('records')

        # Step 7: Find the user's last purchase to give context to the LLM.
        last_purchase = interactions_df[interactions_df['interaction_type'] == 'purchase'].tail(1)
        if last_purchase.empty:
            return recommended_products, {} # Return empty dict if no purchases.

        last_purchased_product_id = last_purchase['product_id'].iloc[0]
        last_purchased_product = products_df[products_df['id'] == last_purchased_product_id].iloc[0].to_dict()
        
        return recommended_products, last_purchased_product
    finally:
        # Always close the database session to free up resources.
        db.close()
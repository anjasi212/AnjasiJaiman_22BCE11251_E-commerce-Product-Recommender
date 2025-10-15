# --- IMPORTS & INITIALIZATION ---
# THIS IS THE MOST IMPORTANT PART.
# `load_dotenv()` MUST be called at the absolute top, before any other local imports.
# This ensures that the OPENAI_API_KEY from your .env file is available for all other modules.
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel
# This is the middleware that handles the CORS security policy.
from fastapi.middleware.cors import CORSMiddleware

# Import our own project files.
from recommender import get_user_profile_recommendations
from llm_explainer import generate_explanation, initialize_client

# Now that dotenv has loaded the key, we can safely initialize the LLM client.
initialize_client()

# Create the FastAPI application instance.
app = FastAPI(title="E-commerce Product Recommender API")

# --- CORS MIDDLEWARE CONFIGURATION ---
# This is the "guest list" for your API. It tells the browser which websites are allowed to make requests.
origins = [
    "http://127.0.0.1:5500", # The address of your frontend from VS Code's Live Server
    "http://localhost:5500",
    "null", # Allow requests from local files (when you double-click frontend.html)
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Which origins are allowed.
    allow_credentials=True,
    allow_methods=["*"], # Allow all HTTP methods (GET, POST, etc.).
    allow_headers=["*"], # Allow all request headers.
)


# --- PYDANTIC MODELS (DATA VALIDATION) ---
# These classes define the expected structure of your API's JSON responses.
# FastAPI uses them to automatically validate data and generate documentation.
class ProductResponse(BaseModel):
    id: int
    name: str
    category: str
    description: Optional[str] = None
    explanation: Optional[str] = None

class RecommendationResponse(BaseModel):
    user_name: str
    recommendations: List[ProductResponse]


# --- API ENDPOINT DEFINITION ---
# This decorator tells FastAPI that the function below handles GET requests to "/recommendations/{user_name}".
@app.get("/recommendations/{user_name}", response_model=RecommendationResponse)
def get_user_recommendations(user_name: str):
    # Step 1: Call the recommender function with the user's name from the URL.
    recommended_products, last_purchase = get_user_profile_recommendations(user_name)

    # Step 2: Handle the case where no recommendations can be made.
    if not recommended_products:
        # Raise an HTTPException, which FastAPI turns into a proper 404 Not Found response.
        raise HTTPException(status_code=404, detail=f"Could not generate recommendations for user '{user_name}'.")

    # Step 3: For each recommended product, call the LLM to get an explanation.
    for product in recommended_products:
        explanation = generate_explanation(last_purchase, product)
        # Add the explanation to the product dictionary.
        product['explanation'] = explanation

    # Step 4: Return the final data, which FastAPI will serialize into JSON.
    return {"user_name": user_name, "recommendations": recommended_products}
# --- IMPORTS ---
# sqlalchemy is the library (ORM) we use to talk to the database with Python objects instead of raw SQL.
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

# --- DATABASE CONFIGURATION ---
# This tells sqlalchemy where our database file is. "sqlite:///ecommerce.db" means it's a file named ecommerce.db in the same folder.
DATABASE_URL = "sqlite:///ecommerce.db"

# The engine is the core interface to the database.
engine = create_engine(DATABASE_URL)

# A Session is a temporary conversation with the database. We create a factory to generate these sessions.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is a class that our database models will inherit from.
Base = declarative_base()


# --- DATABASE MODELS (TABLE DEFINITIONS) ---

# Defines the 'users' table.
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True, nullable=False) # Names must be unique.

# Defines the 'products' table.
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(Text)

# Defines the 'user_interactions' table, which links users to products.
class UserInteraction(Base):
    __tablename__ = "user_interactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    # These ForeignKey columns create a relationship between the tables.
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    interaction_type = Column(String, nullable=False) # e.g., 'view', 'purchase'


# --- DATABASE INITIALIZATION FUNCTION ---

# This function sets up the database from scratch.
def init_db():
    # Delete all existing tables to start fresh.
    Base.metadata.drop_all(bind=engine)
    # Create all the tables we defined above.
    Base.metadata.create_all(bind=engine)
    
    # Start a new conversation with the database.
    db = SessionLocal()

    # Create Python objects for our sample users.
    sample_users = [
        User(id=101, name="Yash"), User(id=102, name="Mahak"), User(id=103, name="Palak"),
        User(id=104, name="Gaurav"), User(id=105, name="Abhishek")
    ]
    
    # Create Python objects for our sample products.
    sample_products = [
        Product(id=1, name='Laptop Pro', category='Electronics', description='A high-performance laptop for professionals.'),
        Product(id=2, name='Wireless Mouse', category='Electronics', description='An ergonomic mouse with long battery life.'),
        Product(id=3, name='Mechanical Keyboard', category='Electronics', description='A tactile keyboard for typing enthusiasts.'),
        Product(id=4, name='Running Shoes', category='Apparel', description='Lightweight shoes for marathon runners.'),
        Product(id=5, name='Cotton T-Shirt', category='Apparel', description='A comfortable t-shirt for daily wear.'),
        Product(id=6, name='Gaming Monitor', category='Electronics', description='A high-refresh-rate monitor for a smooth gaming experience.'),
        Product(id=7, name='Yoga Mat', category='Fitness', description='A non-slip mat for your daily yoga and exercise routine.'),
        Product(id=8, name='Dumbbell Set', category='Fitness', description='A versatile dumbbell set for strength training.'),
        Product(id=9, name='Noise-Cancelling Headphones', category='Electronics', description='Immersive sound quality for music and calls.'),
        Product(id=10, name='Leather Jacket', category='Apparel', description='A stylish and durable leather jacket.'),
    ]
    
    # Create Python objects for the interactions, linking users to products.
    sample_interactions = [
        UserInteraction(user_id=101, product_id=1, interaction_type='purchase'), UserInteraction(user_id=101, product_id=3, interaction_type='view'),
        UserInteraction(user_id=101, product_id=9, interaction_type='purchase'), UserInteraction(user_id=102, product_id=10, interaction_type='purchase'),
        UserInteraction(user_id=102, product_id=5, interaction_type='view'), UserInteraction(user_id=103, product_id=7, interaction_type='purchase'),
        UserInteraction(user_id=103, product_id=8, interaction_type='purchase'), UserInteraction(user_id=103, product_id=4, interaction_type='view'),
        UserInteraction(user_id=104, product_id=9, interaction_type='purchase'), UserInteraction(user_id=104, product_id=5, interaction_type='purchase'),
        UserInteraction(user_id=105, product_id=2, interaction_type='purchase'), UserInteraction(user_id=105, product_id=5, interaction_type='view'),
    ]
    
    # Add all these objects to the session.
    db.add_all(sample_users)
    db.add_all(sample_products)
    db.add_all(sample_interactions)
    
    # Commit (save) all the changes to the database file.
    db.commit()
    # End the conversation.
    db.close()
    print("Database initialized with Yash, Mahak, Palak, Gaurav, and Abhishek.")

# This makes the script runnable from the command line.
# If you run `python database.py`, this init_db() function will be called.
if __name__ == "__main__":
    init_db()

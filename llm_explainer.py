# --- IMPORTS ---
import os
from openai import OpenAI # We use the OpenAI library to talk to any OpenAI-compatible API, like OpenRouter.

# --- CLIENT INITIALIZATION ---
# We declare the client here, but it will be properly initialized in main.py
# after the .env file has been loaded. This avoids a race condition.
client = None

def initialize_client():
    """
    This function is called from main.py after the environment variables are loaded.
    It configures and creates the API client.
    """
    global client
    try:
        client = OpenAI(
            # This is the crucial part: we tell the client to send requests to OpenRouter's server, not OpenAI's.
            base_url="https://openrouter.ai/api/v1",
            # The key is read from the .env file.
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
    except Exception as e:
        print(f"Failed to initialize OpenAI client: {e}")
        client = None

def generate_explanation(last_purchased_product: dict, recommended_product: dict) -> str:
    """
    Generates a short, friendly explanation for a recommendation using the LLM.
    """
    # If the client failed to initialize, we can't do anything.
    if not client:
        return "Could not generate explanation: OpenAI client not initialized."
    
    # This is the "prompt" we send to the AI. It's a template we fill with product details.
    # Good prompts are specific and give the AI clear instructions and examples.
    prompt = f"""
    A user recently purchased the '{last_purchased_product.get('name', 'product')}'.
    We are recommending them the '{recommended_product.get('name', 'product')}'.
    Generate a single, compelling, and friendly sentence explaining why they might like this.
    """
    try:
        # This is the actual API call.
        response = client.chat.completions.create(
            # We use a free model available on OpenRouter to avoid costs.
            model="mistralai/mistral-7b-instruct:free",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=70, # Limit the length of the response.
        )
        # We extract the text content from the AI's response.
        return response.choices[0].message.content.strip()
    except Exception as e:
        # If the API call fails, we print the error and return a generic fallback message.
        print(f"OpenRouter API call failed: {e}")
        return "Because you liked the other product, you might like this one too."
🤖 E-commerce Recommender with LLM Explanations

A smart recommendation system that delivers personalized product suggestions — and uniquely uses a Large Language Model (LLM) (via OpenRouter
) to explain why each product is recommended. 💬✨

🌟 Features

🧠 Content-Based Filtering – Builds a taste profile for every user based on product interactions.

🗣️ AI-Powered Explanations – Generates natural, personalized reasons for each recommendation.

⚡ FastAPI Backend – Asynchronous and efficient backend.

💻 Simple Frontend – Responsive interface built with HTML, Tailwind CSS, and JavaScript.

🧱 SQLite + SQLAlchemy ORM – Clean and lightweight database management.

🛠️ Tech Stack
Category	Technologies
Backend	Python, FastAPI, SQLAlchemy, Uvicorn
Data / ML	Pandas, Scikit-learn
LLM Integration	OpenAI SDK (via OpenRouter)
Frontend	HTML, Tailwind CSS, JavaScript
Database	SQLite
🚀 Quickstart
1️⃣ Clone Repository
git clone https://github.com/Yash0951/product-recommender-api.git
cd product-recommender-api

2️⃣ Set Up Environment
cp .env.example .env


Add your OpenRouter API key in .env.

3️⃣ Install & Run
python -m venv venv
source venv/bin/activate      # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python database.py
uvicorn main:app --reload


Backend will start at http://127.0.0.1:8000

4️⃣ Open Frontend

Open frontend.html in your browser.
Enter any username (e.g., Anjasi, Palak, Giriraj) → Click “Get Recommendations”.

You’ll see:

🛍️ Personalized product list

💬 AI-generated explanations

5️⃣ Explore API Docs

Interactive Swagger UI:
👉 http://127.0.0.1:8000/docs

Example Endpoint

GET /recommendations/{username}
→ Returns a list of recommended products with AI explanations

🧩 Credits

Developed with ❤️ using FastAPI, Scikit-learn, and OpenRouter LLMs.

Demo Video Link:
https://drive.google.com/file/d/12VHCe6Enoaq1_EKHGcrCfEPbACXvneSj/view?usp=sharing

THANK YOU

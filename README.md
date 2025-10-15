# 🤖 E-commerce Recommender with LLM Explanations

A **full-stack intelligent recommendation system** that delivers **personalized product suggestions** — and uniquely, uses a **Large Language Model (LLM)** (via [OpenRouter](https://openrouter.ai)) to generate **human-like explanations** for each recommendation.  

> Imagine a shopping platform that not only *recommends* products but also *tells you why* it thinks you’ll love them. 💬✨

#### Demo Video - https://youtu.be/JF1ZZ8JZ9AU?si=hnm9DnrdEnPkpAKC
---

## 🌟 Features

- 🧠 **Content-Based Filtering** – Builds a *taste profile* for every user based on product descriptions they interact with.  
- 🗣️ **Dynamic AI Explanations** – Integrates an LLM to generate *context-aware, natural language reasons* behind each recommendation.  
- ⚡ **FastAPI Backend** – High-performance, asynchronous Python backend for handling logic and data processing.  
- 🧱 **SQLAlchemy ORM** – Simplifies database management with a clean, Pythonic interface to SQLite.  
- 💻 **Interactive Frontend** – Minimal yet responsive web interface built with HTML, Tailwind CSS, and JavaScript.  

---

## 🛠️ Tech Stack

| Category | Technologies |
|-----------|---------------|
| **Backend** | Python, FastAPI, SQLAlchemy, Uvicorn |
| **Data / ML** | Pandas, Scikit-learn |
| **LLM Integration** | OpenAI Python SDK (configured for OpenRouter) |
| **Frontend** | HTML, Tailwind CSS, JavaScript |
| **Database** | SQLite |

---

## 🚀 Quickstart: Setup & Run

Follow these simple steps to get started 👇  

### **Step 1: Clone the Repository**
```
git clone https://github.com/Yash0951/product-recommender-api.git
```
```
cd product-recommender-api
```
### **Step 2: Configure API Key**
⚠️ The app won’t run without a valid API key from OpenRouter(https://openrouter.ai/)
##### On Windows CMD
```
copy .env.example .env
```
##### On Git Bash / Mac / Linux
```
cp .env.example .env
```
Then open the .env file and replace the placeholder key with your actual OpenRouter API key.

### **Step 3: Install Dependencies & Run**
Run the following commands step-by-step:

1️⃣ Create a virtual environment
```
python -m venv venv
```
2️⃣ Activate it
##### On Windows CMD
```
venv\Scripts\activate
```
##### On Windows Git Bash:
```
source venv/Scripts/activate
```
##### On Mac/Linux:
```
source venv/bin/activate
```
3️⃣ Install all dependencies
```
pip install -r requirements.txt
```
4️⃣ Initialize and populate the database
```
python database.py
```
5️⃣ Start the FastAPI server
```
uvicorn main:app --reload
```
Your backend is now live at http://127.0.0.1:8000
Keep this terminal open!

### **Step 4: Open the Frontend**

Navigate to the project folder and open the **`frontend.html`** file directly in your web browser.

> 📝 **Note:**  
> The frontend should be running at **`http://127.0.0.1:5500`**.  
> If your server runs on a different address or port, update the fetch URL inside the main.py file.

---

Once opened, you’ll see an input field where you can enter any username (for example: `Yash`, `Gaurav`, `Mahak`, `Palak` or `Abhishek`).  
Click the **“Get Recommendations”** button or press **Enter**.  

The page will display:
- 🛍️ **Personalized product recommendations**  
- 💬 **AI-generated explanations** powered by the LLM through OpenRouter  

Enjoy your intelligent recommendation experience! 🚀
### **Step 6: Explore API Documentation**

The FastAPI backend automatically provides **interactive API documentation** so you can easily test all available endpoints.  

Once your server is running, open your browser and visit:  
👉 **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

> 🧭 **Tip:**  
> - The Swagger UI lets you test endpoints directly from the browser.  
> - You can view the input/output models, authentication headers, and try live API requests without writing a single line of code.

---

Example view:
```text
GET /recommendations/{username}
Response → Returns a list of recommended products along with AI-generated explanations.


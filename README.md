# 🚀 E-Commerce-Chatbot

🔎 **AI-Powered Hybrid Chatbot using RAG + Text-to-SQL**

E-Commerce-Chatbot is an intelligent conversational system that can answer both **FAQ-based queries** and **product-related queries** using a hybrid architecture:

* 📚 Retrieval-Augmented Generation (RAG) for FAQs
* 🧠 LLM-powered Text-to-SQL for structured product queries
* 🔀 Semantic routing to dynamically choose the correct pipeline

<img width="1917" height="862" alt="image" src="https://github.com/user-attachments/assets/69a269d8-f94b-4d3b-b9be-4144d145fa6a" />


---

## ✨ Features

* 💬 Chat-based interface using Streamlit
* 🔀 Intelligent query routing (FAQ vs Product search)
* 📚 RAG pipeline using ChromaDB + embeddings
* 🗄️ Text-to-SQL pipeline using LLM + SQLite
* ⚡ Fast semantic search with HuggingFace embeddings
* 🔗 Product recommendations with links
* 🧠 Context-aware response generation

---

## 🧠 Architecture

```
User Query
     │
     ▼
Semantic Router (Intent Classification)
     │
 ┌───────┴────────┐
 ▼                ▼
FAQ Pipeline      SQL Pipeline
(RAG)             (Text-to-SQL)
 ▼                ▼
ChromaDB          SQLite DB
 ▼                ▼
LLM Answer        LLM Response Formatting
     │
     ▼
Final Response to User
```

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **LLM**: Groq (LLaMA 3.3 - 70B Versatile)
* **Embeddings**: all-MiniLM-L6-v2
* **Vector DB**: ChromaDB
* **Database**: SQLite
* **Routing**: Semantic Router (HuggingFace Encoder)
* **Language**: Python

---

## 📂 Project Structure

```
E-Commerce-Chatbot/
│
├── main.py              # Streamlit UI + routing logic
├── sql.py               # Text-to-SQL pipeline
├── router.py            # Semantic routing logic
├── retrive_faq.py       # RAG pipeline (ChromaDB)
├── config.py            # Configurations (models, paths)
├── db.sqlite            # Product database
│
├── resources/
│   ├── faq_data.csv
│   └── ecommerce_data_final.csv
│
└── .env                 # API keys
```

---

## ⚙️ Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/E-Commerce-Chatbot.git
cd E-Commerce-Chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### Setup Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run main.py
```

---

## 💡 Example Queries

### 📚 FAQ Queries (RAG)

* What is the return policy?
* How do I track my order?
* What payment methods are available?

### 🛍️ Product Queries (SQL)

* Show top 3 shoes by rating
* Find Nike shoes under 3000
* List shoes with rating above 4.5
* Show products with highest discount

---

## 🔍 How It Works

### 🔀 Semantic Routing

* Classifies user query into:

  * `faq` → RAG pipeline
  * `sql` → Text-to-SQL pipeline

---

### 📚 RAG Pipeline (FAQ)

1. Convert query → embeddings
2. Retrieve similar FAQs from ChromaDB
3. Pass context + query → LLM
4. Generate accurate answer

---

### 🗄️ SQL Pipeline

1. Convert natural language → SQL query (LLM)
2. Execute query on SQLite DB
3. Format results using LLM
4. Return structured response

---

## 🚀 Future Improvements

* ⚡ Streaming responses for better UX
* 🌐 Deploy on Streamlit Cloud / AWS
* 📈 Add evaluation metrics (accuracy, latency)

---

## 🧪 Limitations

* Routing may fail for ambiguous queries
* SQL generation depends on LLM accuracy
* No conversation memory (stateless responses)

---

## 🎯 Use Cases

* E-commerce customer support chatbot
* Product recommendation assistant
* AI-powered FAQ system




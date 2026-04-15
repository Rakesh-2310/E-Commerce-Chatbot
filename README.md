# 🛍️ E-Commerce Chatbot (LLM + RAG + Text-to-SQL)

An intelligent **AI-powered E-commerce chatbot** that combines **Retrieval-Augmented Generation (RAG)** and **Text-to-SQL** to answer both **FAQ-based** and **data-driven product queries** in real time.

---

## 🚀 Key Highlights

* 🔀 **Semantic Routing** → Automatically decides whether a query is FAQ or product-related
* 📚 **RAG-based FAQ System** → Uses ChromaDB + embeddings for accurate answers
* 🛢️ **Text-to-SQL Engine** → Converts natural language → SQL → executes on database
* 🧠 **LLM-Powered Reasoning** → Uses Groq (LLaMA 3) for generation
* 💬 **Interactive UI** → Built with Streamlit chat interface
* ⚡ **Low Latency + High Accuracy Architecture**

---

## 🧠 Architecture Overview

```text
                ┌──────────────┐
                │  User Query  │
                └──────┬───────┘
                       │
              ┌────────▼────────┐
              │ Semantic Router │
              └──────┬─────────┘
           ┌─────────┴─────────┐
           │                   │
     ┌─────▼─────┐       ┌─────▼─────┐
     │ FAQ Chain │       │ SQL Chain │
     └─────┬─────┘       └─────┬─────┘
           │                   │
   ChromaDB Retrieval     SQL Generation
           │                   │
       LLM Answer         DB Query → LLM
           │                   │
           └──────────┬────────┘
                      │
                Final Response
```

---

## 🧩 Project Structure

```bash
E-Commerce-Chatbot/
│
├── resources/
│   ├── ecommerce_data_final.csv
│   ├── faq_data.csv
│   ├── image.png
│
├── config.py          # Configurations (paths, models, chunking)
├── main.py            # Streamlit UI + orchestration
├── retrive_faq.py     # RAG pipeline using ChromaDB
├── route.py           # Semantic routing logic
├── sql.py             # Text-to-SQL pipeline
├── db.sqlite          # Product database
└── README.md
```

---

## ⚙️ Workflow (End-to-End)

### 1️⃣ Configuration (`config.py`)

* Stores:

  * File paths
  * Embedding model (`all-MiniLM-L6-v2`)
  * LLM model (`llama-3.3-70b-versatile`)
  * Chunk size & overlap

---

### 2️⃣ User Interface (`main.py`)

* Built with **Streamlit chat UI**
* Handles:

  * User input
  * Chat history
  * Routing queries → `faq_chain` or `sql_chain`

---

### 3️⃣ Semantic Routing (`route.py`)

* Uses **Sentence Transformers**
* Computes **cosine similarity** between query & predefined intents
* Routes into:

  * `faq` → informational queries
  * `sql` → product/database queries

---

### 4️⃣ FAQ Pipeline (RAG) (`retrive_faq.py`)

#### 🔹 Steps:

1. Load FAQ CSV
2. Convert questions → embeddings
3. Store in **ChromaDB**
4. Retrieve top-k relevant answers
5. Pass context to LLM

#### 🔹 Key Feature:

* **Strict grounding**:

  > If answer not in context → returns `"I don't know"`
* Prevents hallucination ✅

---

### 5️⃣ SQL Pipeline (Text-to-SQL) (`sql.py`)

#### 🔹 Steps:

1. LLM generates SQL query from question
2. Extract query using `<SQL>` tags
3. Execute on SQLite database
4. Convert results → human-readable response

#### 🔹 Dual LLM Design:

* **Stage 1:** Query Generation
* **Stage 2:** Result Interpretation

---

## 💡 Example Queries

### 🔹 FAQ Queries

* "What is your return policy?"
* "How long does refund take?"
* "Is cash on delivery available?"

### 🔹 Product Queries

* "Show shoes under 3000"
* "Top rated Nike shoes"
* "Shoes with rating above 4.5 and discount > 40%"

---

## 🛠️ Tech Stack

| Component  | Technology            |
| ---------- | --------------------- |
| UI         | Streamlit             |
| LLM        | Groq (LLaMA 3.3)      |
| Embeddings | Sentence Transformers |
| Vector DB  | ChromaDB              |
| Database   | SQLite                |
| Language   | Python                |

---

## ⚡ Installation & Setup

# Install dependencies
pip install -r requirements.txt

### 🔐 `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run main.py
```

---

## 🧪 Example Output

```text
User: Show top 3 shoes with highest rating

Bot:
1. Nike Air Zoom: Rs. 2999 (40% off), Rating: 4.6 <link>
2. Puma Running Shoes: Rs. 2499 (35% off), Rating: 4.5 <link>
3. Adidas Sports Shoes: Rs. 2799 (30% off), Rating: 4.4 <link>
```

---

## 📈 Future Improvements

* 🔁 Replace rule-based routing with **LLM Router / Agent**
* 🧠 Add **Re-ranking (Cross-Encoder)** for better retrieval
* 🔐 SQL safety layer (query validation / sandboxing)
* 📊 Add analytics dashboard (user queries, accuracy)
* 🌐 Deploy with FastAPI + Docker + Cloud

---

## 🎯 Why This Project Stands Out

* Combines **RAG + Text-to-SQL in one system**
* Demonstrates **end-to-end LLM system design**
* Shows **real-world production patterns**:

  * Routing
  * Retrieval
  * Query generation
  * Response synthesis



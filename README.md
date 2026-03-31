# NovaArchive AI – Enterprise RAG Assistant

NovaArchive AI is a high-performance **Retrieval-Augmented Generation (RAG)** application built using the **Amazon Bedrock ecosystem**.

It enables users to interact with **unstructured PDF documents** using natural language and get **accurate, context-aware, hallucination-free answers** by combining:

- 🔍 Semantic Search
- 🧠 LLM Reasoning
- ⚡ Fast Local Vector Retrieval

---

## 📸 Project Preview

### 🖥️ Application Output
![App UI](./assets/output.png)

*Modern Streamlit interface powered by AWS Bedrock models.*

---

### 🔄 System Architecture (RAG Pipeline)
![Flowchart](./assets/flowchart.png)

*End-to-end pipeline: Ingestion → Embedding → Storage → Retrieval → Generation*

---

## ⚙️ How It Works

### 🔹 1. Ingestion Phase
- PDFs are loaded from `/data`
- Text is split into chunks (≈1000 characters)
- Embeddings are generated using **Amazon Titan v2**

### 🔹 2. Storage
- Embeddings are stored locally using **ChromaDB**
- Enables fast and cost-efficient retrieval

### 🔹 3. Retrieval
- User query → converted into embedding
- Similar chunks are retrieved using **vector similarity search**

### 🔹 4. Generation
- Retrieved context is passed to **Amazon Nova Pro**
- LLM generates **accurate, context-aware answers**

---

## 🛠️ Technical Stack
* **LLM:** Amazon Nova Pro (`amazon.nova-pro-v1:0`)
* **Embeddings:** Amazon Titan Text Embeddings v2
* **Vector Store:** ChromaDB
* **Orchestration:** LangChain & Boto3
* **Frontend:** Streamlit
---

## 📂 Project Structure
NovaArchive-AI/
│
├── data/ # Input PDFs
├── chroma_db/ # Vector database (auto-generated)
├── assets/ # Images (flowchart + output)
│ ├── flowchart.png
│ └── output.png
│
├── app.py # Streamlit app (UI + query handling)
├── ingest.py # PDF ingestion + embedding pipeline
├── requirements.txt # Dependencies
├── README.md # Documentation
└── .gitignore


## 🚀 Getting Started

### 1. Prerequisites
* AWS Account with Model Access enabled for **Nova Pro** and **Titan v2** in `us-east-1`.
* Python 3.10+ (Anaconda recommended).

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/Harshit-Pandey01/NovaArchive-AI.git](https://github.com/Harshit-Pandey01/NovaArchive-AI.git)
cd NovaArchive-AI

# Install dependencies
pip install langchain langchain-community langchain-aws chromadb pypdf boto3 streamlit

# AWS Configuration
aws configure

#Set:
Region: us-east-1

# Access Key & Secret Key
📥 Add Your Data
Place your PDF files inside the data/ folder

Run Ingestion Pipeline
python ingest.py
Creates embeddings
Stores them in chroma_db/


Run the App
streamlit run app.py

✨ Features
📄 Chat with multiple PDFs
⚡ Fast local vector search (ChromaDB)
🧠 AWS Bedrock LLM integration
🎯 Context-aware answers (reduced hallucination)
💻 Clean and modern UI (Streamlit)
🔒 Fully local retrieval (cost-efficient)
# AI---Colab---PDF-Resume-Summarizer

# 🔍 Resume Question Answering with LangChain + Hugging Face

This project demonstrates a **Conversational AI pipeline** that reads a PDF resume and answers natural language questions about its content. It uses:

- **LangChain** for document loading, chunking, vector storage, and QA chaining
- **Hugging Face Transformers** for embedding and LLM models
- **Google Colab** for an easy, reproducible cloud notebook environment

---

## 🧠 What It Does

Upload a resume (PDF), and ask questions like:

- “What technologies does this person have experience with?”
- “Summarize this resume in 3 bullet points.”
- “List all certifications and degrees.”
- “What industries has this person worked in?”

The model searches the document and returns a relevant, human-readable answer.

---

## 🚀 How It Works

1. **PDF Loading**  
   Uses `PyPDFLoader` from LangChain to load the file.

2. **Text Splitting**  
   Chunks text into manageable pieces using `RecursiveCharacterTextSplitter`.

3. **Embeddings + Vector Store**  
   Generates dense vectors with Hugging Face’s `all-MiniLM-L6-v2` and stores them using `Chroma`.

4. **Language Model (LLM)**  
   Uses `google/flan-t5-base` from Hugging Face to generate answers based on vector search results.

5. **Question Answering**  
   Accepts natural language queries and returns results using LangChain's `RetrievalQA`.

---

## 🛠️ Tech Stack

| Component            | Tool/Model                                |
|----------------------|-------------------------------------------|
| Vector Store         | Chroma                                    |
| Embedding Model      | `sentence-transformers/all-MiniLM-L6-v2`  |
| LLM                  | `google/flan-t5-base`                     |
| LangChain Modules    | `DocumentLoader`, `TextSplitter`, `RetrievalQA`, `LLM` |
| Runtime              | Google Colab (GPU/CPU)                    |

---

## 📦 Setup Instructions

Install dependencies:
   ```bash
   pip install -U langchain langchain-community transformers sentence-transformers chromadb
Upload your resume PDF.

Paste your Hugging Face API token securely:

python

from google.colab import userdata
hf_token = userdata.get('HF_TOKEN')
Run the cells and ask your questions!

📸 Sample Output

❓ What technologies does this person have experience with?
💬 Python, Tableau, SQL, Excel, HTML, JavaScript...

❓ What are 3 career highlights from this resume?
💬 1. Led implementation of workflow automation using Birst and Metabase.
    2. Created AI-powered PDF templates for field data inspection.
    3. Managed integrations and support for SaaS analytics products.


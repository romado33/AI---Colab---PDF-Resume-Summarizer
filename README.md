# AI---Colab---PDF-Resume-Summarizer

# 📄 Resume Q&A Chatbot with LangChain + HuggingFace

This project is an interactive chatbot that answers questions about a resume PDF using natural language. It uses LangChain to handle document loading and retrieval, HuggingFace Transformers for embeddings and LLM, and ChromaDB as a vector store.

## 🔍 Features

- Upload any resume in PDF format
- Ask questions like:
  - "What technologies does this person know?"
  - "Summarize this resume in 3 bullet points."
  - "What industries has this person worked in?"
- Uses HuggingFace free models (no OpenAI key required)
- Runs fully in Google Colab

## 🧠 Tech Stack

- Python (Google Colab)
- LangChain
- HuggingFace Transformers & Pipelines
- Sentence-Transformers (`all-MiniLM-L6-v2`)
- Chroma Vector Store
- PyPDF for PDF parsing

## 🚀 Getting Started

1. Clone the repo or open the notebook in Google Colab.
2. Install dependencies:
   ```bash
   pip install langchain langchain-community langchain-huggingface \
               transformers sentence-transformers chromadb pypdf

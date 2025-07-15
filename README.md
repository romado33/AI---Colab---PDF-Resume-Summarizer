# 📄 Resume QA with LangChain + Hugging Face + Gradio

Conversational AI that reads resumes and answers questions like a recruiter. Upload any PDF resume, and ask questions like:

- “What technologies does this person have experience with?”
- “Summarize this resume in 3 bullet points.”
- “List any certifications and degrees.”

Built with LangChain, Hugging Face Transformers, Gradio, and ChromaDB.

---

## 🚀 Features

✅ PDF parsing  
✅ Local embeddings via Sentence Transformers  
✅ RAG (Retrieval-Augmented Generation) pipeline  
✅ Secure Hugging Face key handling  
✅ Web demo via Gradio  
✅ Ready for Hugging Face Spaces or Streamlit

---

## 🧠 Demo (Gradio)

[![Gradio Space](https://img.shields.io/badge/Launch-Demo-green?logo=gradio)](https://huggingface.co/spaces/YOUR_USERNAME/resume-qa)

> Upload a resume and start asking questions in natural language.

---

## 📂 Project Structure

resume-qa/
├── app/
│ ├── main.py # CLI or Streamlit interface
│ ├── utils.py # Parsing, embedding utils
├── notebooks/
│ └── Resume_QA_Colab.ipynb
├── uploads/ # Temporary PDF storage (.gitignored)
├── README.md
├── requirements.txt
└── .gitignore

yaml
Copy
Edit

---

## 🔧 Setup Instructions

### 🖥️ Local (Python 3.10+)
```bash
git clone https://github.com/YOUR_USERNAME/resume-qa
cd resume-qa
pip install -r requirements.txt
Set your Hugging Face token securely:

bash
export HUGGINGFACEHUB_API_TOKEN=your_token_here
Then run the app:

bash
python app/main.py
🧪 Google Colab
Use the provided notebooks/Resume_QA_Colab.ipynb.
You'll be prompted to upload a resume and enter your Hugging Face key as a secret.

🌐 Deploy to Hugging Face Spaces
Push your project to a public repo

Create a new Space

Select Gradio as the SDK

In app/main.py, ensure gr.Interface(...) is returned at the end

Add HUGGINGFACEHUB_API_TOKEN as a secret

🌟 Example Questions
What technologies does this person have experience with?
Summarize this resume in 3 bullet points.
What industries has this person worked in?
List all certifications or degrees.
What roles has this person held in the past?
🔒 Security Notes
API keys are never hardcoded – they're loaded securely via environment variables or secrets

Uploaded resumes are stored in memory or temp folders (never saved permanently)

Hugging Face gated models are not used unless explicitly enabled

📦 Requirements
nginx
langchain
langchain-community
langchain-huggingface
transformers
sentence-transformers
chromadb
gradio
pypdf
🤝 Contributing
PRs welcome! Please ensure your changes are well-tested and follow project structure.

👨‍💻 Author
Rob Dods
🟦 LinkedIn
🐙 GitHub

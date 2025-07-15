# 📄 Resume QA with LangChain + Hugging Face + Gradio

Conversational AI that reads resumes and answers questions like a recruiter.  
Upload any PDF resume and ask questions such as:

- What technologies does this person have experience with?
- Summarize this resume in 3 bullet points.
- List any certifications and degrees.

Built using LangChain, Hugging Face Transformers, Gradio, and ChromaDB.

---

## 🚀 Features

- PDF parsing
- Local embeddings via Sentence Transformers
- RAG (Retrieval-Augmented Generation) pipeline
- Secure Hugging Face key handling
- Web demo via Gradio
- Ready for Hugging Face Spaces or Streamlit

---

## 🧠 Demo

Try the hosted demo on Hugging Face Spaces:  
`https://huggingface.co/spaces/YOUR_USERNAME/resume-qa`

Upload a resume and start asking questions in natural language.

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

### Local (Python 3.10+)

1. Clone the repository:
git clone https://github.com/YOUR_USERNAME/resume-qa
cd resume-qa

markdown
Copy
Edit

2. Install dependencies:
pip install -r requirements.txt

javascript
Copy
Edit

3. Set your Hugging Face token:
export HUGGINGFACEHUB_API_TOKEN=your_token_here

markdown
Copy
Edit

4. Run the app:
python app/main.py

yaml
Copy
Edit

---

### Google Colab

Use the notebook in `notebooks/Resume_QA_Colab.ipynb`.  
You'll be prompted to upload a resume and enter your Hugging Face key via Colab secrets.

---

### Hugging Face Spaces

1. Push this project to a public GitHub repo.
2. Create a new Space at Hugging Face.
3. Choose **Gradio** as the SDK.
4. Make sure `main.py` returns a `gr.Interface`.
5. Add `HUGGINGFACEHUB_API_TOKEN` under **Secrets** in the Space settings.

---

## 🌟 Example Questions

- What technologies does this person have experience with?
- Summarize this resume in 3 bullet points.
- What industries has this person worked in?
- List all certifications or degrees.
- What roles has this person held in the past?

---

## 🔒 Security Notes

- API keys are never hardcoded; they're handled via environment variables or Colab/HF secrets.
- Uploaded resumes are stored temporarily and not persisted.
- Gated models are not used unless explicitly enabled.

---

## 📦 Requirements

- langchain  
- langchain-community  
- langchain-huggingface  
- transformers  
- sentence-transformers  
- chromadb  
- gradio  
- pypdf

---

## 🤝 Contributing

Pull requests are welcome!  
Please ensure your code is well-documented and tested.

---

## 👨‍💻 Author

Rob Dods  
[GitHub](https://github.com/robdods)  
[LinkedIn](https://linkedin.com/in/robdods)

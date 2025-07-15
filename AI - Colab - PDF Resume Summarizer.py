# ✅ STEP 2: Import necessary packages
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from google.colab import userdata
import tempfile, os

# ✅ STEP 3: Set Hugging Face token (optional)
hf_token = userdata.get("HUGGINGFACEHUB_API_TOKEN")
if hf_token:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_token

# ✅ STEP 4: Upload and read your PDF file
from google.colab import files
uploaded = files.upload()  # Upload e.g. "Rob Dods - 2025.pdf"
pdf_filename = next(iter(uploaded))

loader = PyPDFLoader(pdf_filename)
pages = loader.load()

splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(pages)

# ✅ STEP 5: Embed using a lightweight, fast HF model
embedding_model = "sentence-transformers/paraphrase-MiniLM-L3-v2"
embeddings = HuggingFaceEmbeddings(model_name=embedding_model)

persist_dir = tempfile.mkdtemp()
db = Chroma.from_documents(docs, embeddings, persist_directory=persist_dir)

# ✅ STEP 6: Load a lightweight free HF model
model_id = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
llm = HuggingFacePipeline(pipeline=pipe)

# ✅ STEP 7: Build retrieval QA chain
qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

# ✅ STEP 8: Ask questions!
questions = [
    "What technologies does this person have experience with?",
    "Summarize this resume in 3 bullet points.",
    "What industries has this person worked in?",
]

for q in questions:
    print(f"\n❓ {q}")
    answer = qa.invoke(q)
    print("💬", answer)

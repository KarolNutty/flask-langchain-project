import os
import shutil

import texto
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS, DocArrayInMemorySearch
# 1. Split
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_text(texto)

# 2. Embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# 3. Vetores
vectorstore = FAISS.from_texts(
    texts=chunks,
    embedding=embeddings
)
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains.retrieval import RetrievalQA


VECTOR_PATH = "vectorstore"


def clear_vectorstore():
    if os.path.exists(VECTOR_PATH):
        shutil.rmtree(VECTOR_PATH)
    os.makedirs(VECTOR_PATH, exist_ok=True)


def create_vectorstore(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )
    chunks = splitter.split_text(text)

    embeddings = OpenAIEmbeddings()

    vectorstore = DocArrayInMemorySearch.from_texts(
        chunks,
        embedding=embeddings
    )

    # Salvando como pickle
    import pickle
    with open(os.path.join(VECTOR_PATH, "store.pkl"), "wb") as f:
        pickle.dump(vectorstore, f)

    return True


def load_vectorstore():
    import pickle
    with open(os.path.join(VECTOR_PATH, "store.pkl"), "rb") as f:
        return pickle.load(f)


def answer_question(question: str):
    vectorstore = load_vectorstore()
    llm = ChatOpenAI(temperature=0)

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        chain_type="stuff"
    )

    return qa.run(question)

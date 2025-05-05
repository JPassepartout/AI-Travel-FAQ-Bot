from langchain_community.vectorstores import FAISS
from langchain_google_vertexai import VertexAIEmbeddings
from langchain.schema import Document

def create_faiss_vector_store(qa_data):

    # Convert embeddings to a NumPy array
    documents = [Document(page_content=qa["question"] + " " + qa["answer"]) for qa in qa_data]  # This creates the document objects
    # Create FAISS index using Langchain
    vector_store = FAISS.from_documents(
        documents,
        VertexAIEmbeddings(model="text-embedding-004")
    )

    return vector_store



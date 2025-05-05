import os
from dotenv import load_dotenv
from utils.pdf_loader import load_qa_data
from utils.vector_store import create_faiss_vector_store
from utils.query_handler import process_query,format_results

# Load environment variables from .env file
load_dotenv()
project = os.environ["project"]
location = os.environ["location"]


qa_data = load_qa_data("data/travel_faqs.pdf")  # Load the Q&A data from the PDF
vector_store = create_faiss_vector_store(qa_data)  # Create the vector store using FAISS


while True:
    query = input("Please enter your question: ")
    if query.lower() in ['exit','-1','quit']:
        break
    # Process the query and get the top-k results
    results = process_query(query, vector_store, top_k=3)
    # Format and display the results
    formatted_results = format_results(results)
    print(formatted_results)


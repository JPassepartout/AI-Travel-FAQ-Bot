
def process_query(query, vector_store, top_k=3):
    """
    Process the user's query, search the FAISS vector store, and return the top-k results.
    """
    # Search the vector store for the most similar documents
    search_results = vector_store.similarity_search(query, k=top_k)
    return search_results
def format_results(results):
    """
    Format the results into a user-friendly string.
    """
    formatted_results = "Top similar Q&A pairs:\n"
    for result in results:
        question, answer = result.page_content.split("  ", 1)  # Split question and answer
        formatted_results += f"Q: {question.strip()}\nA: {answer.strip()}\n\n"

    return formatted_results

# AI Travel FAQ Bot

This is a simple AI-powered FAQ chatbot that answers travel-related questions using LangChain, VertexAI embeddings, and FAISS for semantic search.

## 🔧 Features

- Loads questions and answers from a PDF
- Embeds Q&A data with VertexAI embeddings
- Stores vectors in a FAISS index
- Accepts user queries and returns top 3 most relevant Q&A pairs

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```
## 🔐 Environment Variables
Create a .env file in the root directory:
```bash
project = your-google-cloud-project-id
location = your-gcp-region
```
## 💡 Notes
Embeddings are generated using text-embedding-004 model from Vertex AI.
Ensure your GCP account has VertexAI access and is authenticated:
```bash
gcloud auth application-default login
```
## 🚀 Usage
```bash
python main.py
```

Example input/output:
```less
Please enter your question: How many minutes in advance should I arrive for my flight?
Top similar Q&A pairs:
Q: How early should I arrive at the airport?
A: It is recommended to arrive at least 2 hours before a domestic flight and 3 hours before
an international flight.

Q: What should I do if my baggage is lost?
A: Contact your airline’s baggage claim desk immediately and file a report. Keep your
baggage tags and boarding pass.

Q: Can I bring liquids in my carry-on bag?
A: Yes, but each liquid must be in a container of 100ml or less, and all containers must fit
into a single, clear, resealable 1-liter plastic bag.
```
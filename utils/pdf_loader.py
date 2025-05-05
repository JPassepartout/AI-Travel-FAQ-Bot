import pdfplumber
import re

def load_qa_data(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:#../data/travel_faqs.pdf
        first_page = pdf.pages[0]
        text = first_page.extract_text()    #text = "\n".join([page.extract_text() for page in pdf.pages])

        # Split the entire text using regex, breaking at every "Q1:", "Q2:", etc.
        text = re.split(r"Q\d+:", text)[1:]

        i = 0
        qa_data = []

        # Loop through each chunk of the split text
        for qa in text:
            # Split by the answer, which starts with "\nA:"
            text[i] = qa.split("\nA:")

            # Store the Q&A pairs into the dictionary
            qa_data.append({
                "question":text[i][0],
                "answer":text[i][1]
            })
            i += 1
    return qa_data




import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline
import os

# Set up environment variable for Hugging Face API key
os.environ["HF_HOME_API_KEY"] = "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"

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            if page.extract_text():
                text += page.extract_text()
        return text.strip()
    except Exception as e:
        st.error(f"Error during text extraction: {e}")
        return ""

# Function to answer questions from the PDF text using a BERT-based question-answering model
def answer_questions(pdf_text, question):
    try:
        qa_pipeline = pipeline(
            "question-answering",
            model="deepset/bert-large-uncased-whole-word-masking-squad2",  # Updated model for better accuracy
            tokenizer="deepset/bert-large-uncased-whole-word-masking-squad2",
        )
        response = qa_pipeline(question=question, context=pdf_text)
        return response.get("answer", "").strip()
    except Exception as e:
        st.error(f"Error while answering questions: {e}")
        return ""

# Streamlit app
st.sidebar.title("Q & A App 💬")
st.sidebar.markdown(
    """
    ## About
    This app is an LLM-powered chatbot built using Streamlit and Hugging Face Transformers.  
    Upload a PDF and ask questions to get answers based on the document content.
    """
)

st.title("PDF Q & A Chatbot 🤖")

# Upload PDF file
uploaded_file = st.file_uploader("Upload your PDF:", type="pdf")

# Main conversation loop
if uploaded_file is not None:
    pdf_text = extract_text_from_pdf(uploaded_file)
    if pdf_text:
        st.write("**Extracted Content:**")
        st.write(pdf_text[:5000])  # Limit displayed text to first 5000 characters for performance

        st.write("---")

        # Chatbot interface
        with st.expander("Chat with the Q&A Bot"):
            # Welcome message
            st.write("Welcome! Please ask your query related to the PDF.")
            
            user_question = st.text_input("You: ")
            if user_question:
                if user_question.lower() == "exit":
                    st.write("Goodbye!")
                else:
                    answer = answer_questions(pdf_text, user_question)
                    st.write("Bot:", answer)

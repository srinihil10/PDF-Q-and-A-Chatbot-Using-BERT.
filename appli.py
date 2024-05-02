import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
import os

# Set up environment variable for Hugging Face API key
os.environ["HF_HOME_API_KEY"] = "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"

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text.strip()
    except Exception as e:
        st.error(f"Error during text extraction: {e}")
        return ""

# Function to answer questions from the PDF text using a BERT-based question-answering model
def answer_questions(pdf_text, question):
    try:
        tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
        model = AutoModelForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
        qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)
        answer = qa_pipeline(question=question, context=pdf_text)["answer"]
        return answer.strip()
    except Exception as e:
        st.error(f"Error while answering questions: {e}")
        return ""

# Streamlit app
st.sidebar.title(' Q & A App 💬')
st.sidebar.markdown('''
    ## About
    This app is an LLM-powered chatbot built using STREAMLIT , HUGGING FACE TRANSFORMERS , BERT  ''')

st.title("PDF Q & A bot 🤗💬")
uploaded_file = st.file_uploader("Upload your PDF:", type="pdf")

if uploaded_file is not None:
    pdf_text = extract_text_from_pdf(uploaded_file)
    if pdf_text:
        st.write("**Extracted Content:**")
        st.write(pdf_text)

        st.write("---")

        st.write("**Ask Questions:**")
        user_question = st.text_input("Ask a question:")
        if user_question:
            answer = answer_questions(pdf_text, user_question)
            st.write("**Answer:**")
            st.write(answer)

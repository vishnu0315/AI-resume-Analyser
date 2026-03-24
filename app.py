import streamlit as st
import pdfplumber
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

st.title("AI Resume Analyzer")

uploaded_resume = st.file_uploader("Upload Resume (PDF)", type="pdf")

job_description = st.text_area("Paste Job Description")

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

if uploaded_resume and job_description:

    resume_text = extract_text_from_pdf(uploaded_resume)

    text = [resume_text, job_description]

    cv = CountVectorizer().fit_transform(text)
    similarity = cosine_similarity(cv)[0][1]

    score = round(similarity * 100, 2)

    st.subheader(f"ATS Match Score: {score}%")

    if score > 70:
        st.success("Strong match with job description")
    elif score > 40:
        st.warning("Moderate match, improve keywords")
    else:
        st.error("Low match, add more relevant skills")
        st.error("Low match, add more relevant skills")
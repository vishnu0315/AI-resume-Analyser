# AI Resume Analyzer

## Overview
The AI Resume Analyzer is a web-based application that evaluates resumes by comparing them with job descriptions. It uses Natural Language Processing (NLP) techniques to calculate how well a resume matches a given job role and provides an approximate ATS (Applicant Tracking System) score.

This project helps users understand how their resumes perform against job requirements and identify areas for improvement.

---

## Features
- Upload resume in PDF format  
- Extract text from resumes automatically  
- Compare resume with job description  
- Generate ATS match score  
- Simple and interactive web interface  

---

## Technologies Used
- Python  
- Streamlit  
- NLTK (Natural Language Processing)  
- Scikit-learn  
- PDFPlumber  

---

## How It Works
1. The user uploads a resume in PDF format.  
2. The system extracts text from the resume.  
3. The user provides a job description.  
4. The application compares both texts using NLP techniques.  
5. A similarity score is calculated using cosine similarity.  
6. The ATS match score is displayed to the user.  

---


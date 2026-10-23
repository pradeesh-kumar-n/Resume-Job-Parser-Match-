import os
import tempfile

import streamlit as st

from utils import extract_text_from_pdf, extract_skills, calculate_match_score

st.set_page_config(
    page_title="Resume-Job Matcher",
    page_icon="📄",
    layout="centered",
)

st.title("📄 Resume-Job Matcher")
st.write("Upload a candidate's resume and a job description to find the best match.")

uploaded_file = st.file_uploader("Upload Resume (PDF/TXT)", type=["pdf", "txt"])
job_description = st.text_area("Paste the Job Description here", height=250)

if st.button("Analyze Match"):
    if uploaded_file is not None and job_description.strip():
        with st.spinner("Analyzing..."):
            temp_path = None
            try:
                if uploaded_file.name.lower().endswith(".txt"):
                    resume_text = uploaded_file.read().decode("utf-8", errors="ignore")
                else:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                        tmp.write(uploaded_file.getbuffer())
                        temp_path = tmp.name

                    resume_text = extract_text_from_pdf(temp_path)

                if not resume_text.strip():
                    st.error(
                        "No readable text was found in the uploaded file. "
                        "Please upload a searchable PDF, a scanned PDF with readable text, or a TXT resume."
                    )
                else:
                    resume_skills = extract_skills(resume_text)
                    score = calculate_match_score(resume_text, job_description)
                    score_percentage = f"{score * 100:.1f}%"

                    st.subheader("📊 Analysis Results")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Match Score", score_percentage)
                    with col2:
                        st.metric("Skills Found", len(resume_skills))

                    st.subheader("🧠 Matched Skills")
                    st.write(", ".join(resume_skills) if resume_skills else "No key skills found.")

                    with st.expander("View Extracted Resume Text"):
                        st.text(resume_text)

            finally:
                if temp_path and os.path.exists(temp_path):
                    os.remove(temp_path)
    else:
        st.error("Please upload a PDF/TXT file and paste a job description.")

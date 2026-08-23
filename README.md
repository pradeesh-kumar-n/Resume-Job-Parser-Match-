# 📄 Resume‑Job Matcher

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)

A Streamlit‑based application that helps recruiters, job seekers, and HR professionals quickly evaluate how well a candidate’s resume aligns with a job description. It combines **OCR**, **skill extraction**, and **NLP similarity scoring** to deliver a clear match score and highlight relevant skills.

---

## ✨ Features
- **OCR Resume Parsing**: Extracts text from PDF resumes using `pdf2image` and `pytesseract`.
- **Skill Extraction**: Identifies key technical and soft skills from resumes.
- **Match Scoring**: Uses TF‑IDF and cosine similarity to calculate how closely a resume matches a job description.
- **Interactive UI**: Built with Streamlit for an easy, web‑based experience.
- **Docker Support**: Run the app in a container without worrying about dependencies.

---

## 🛠️ Tech Stack
- **Python 3.10**
- **Streamlit** (UI framework)
- **pdf2image + Tesseract OCR** (resume text extraction)
- **scikit‑learn** (TF‑IDF vectorization and similarity scoring)
- **Docker** (containerization)

---

## 🚀 Getting Started

### Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/pradeesh-kumar-n/resume-job-matcher.git
cd resume-job-matcher
pip install -r requirements.txt
'''
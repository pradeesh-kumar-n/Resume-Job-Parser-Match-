import re
import os
from typing import List

import fitz  # PyMuPDF
from pdf2image import convert_from_path
from PIL import Image, ImageOps
import pytesseract
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

skill_database = [
    "python", "java", "javascript", "sql", "html", "css", "react", "node.js",
    "machine learning", "data analysis", "aws", "docker", "git", "communication",
    "leadership", "flask", "django", "rest api", "api", "postgresql", "mongodb",
    "tensorflow", "pytorch", "c++", "c#", "azure", "kubernetes", "agile"
]

def _clean_text(text: str) -> str:
    if not text:
        return ""
    text = text.replace("\x00", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from PDF. Tries native PDF text first, then OCR fallback."""
    full_text = ""

    # 1) Try native PDF text extraction for searchable PDFs
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                page_text = page.get_text("text")
                if page_text:
                    full_text += page_text + "\n"
    except Exception:
        full_text = ""

    if full_text.strip():
        return _clean_text(full_text)

    # 2) Fallback to OCR for scanned PDFs or image-based PDFs
    try:
        images = convert_from_path(pdf_path, dpi=300)
        for image in images:
            img = ImageOps.grayscale(image)
            img = ImageOps.autocontrast(img)
            img = img.resize((img.width * 2, img.height * 2))

            page_text = pytesseract.image_to_string(
                img,
                config="--psm 6"
            )
            if page_text:
                full_text += page_text + "\n"
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""

    return _clean_text(full_text)

def extract_skills(text: str) -> list:
    """Find skills from resume text."""
    if not text:
        return []

    normalized_text = _clean_text(text).lower()
    found_skills = set()

    for skill in skill_database:
        skill_text = skill.lower()
        if skill_text in normalized_text:
            found_skills.add(skill)

    return sorted(found_skills)

def calculate_match_score(resume_text: str, job_description: str) -> float:
    """Calculate similarity score between resume and job description."""
    if not resume_text.strip() or not job_description.strip():
        return 0.0

    documents = [resume_text, job_description]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return float(similarity_matrix[0][0])

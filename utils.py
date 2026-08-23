import re
from pdf2image import convert_from_path
import pytesseract
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

skill_database = [
    "python", "java", "javascript", "sql", "html", "css", "react", "node.js",
    "machine learning", "data analysis", "aws", "docker", "git", "communication", "leadership"
]

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from PDF using OCR"""
    try:
        images = convert_from_path(pdf_path)
        full_text = ""
        for image in images:
            text = pytesseract.image_to_string(image)
            full_text += text + "\n"
        return full_text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ''

def extract_skills(text: str) -> list:
    """Find skills from resume text"""
    found_skills = set()
    for skill in skill_database:
        if re.search(r"\b" + re.escape(skill) + r"\b", text, re.IGNORECASE):
            found_skills.add(skill)
    return list(found_skills)

def calculate_match_score(resume_text: str, job_description: str) -> float:
    """Calculate similarity score between resume and job description"""
    documents = [resume_text, job_description]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity_matrix[0][0]

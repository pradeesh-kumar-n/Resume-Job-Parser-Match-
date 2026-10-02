from utils import extract_skills, calculate_match_score

# Read sample files
with open('sample_resume.txt', 'r', encoding='utf-8') as f:
    resume_text = f.read()

with open('sample_job_description.txt', 'r', encoding='utf-8') as f:
    job_description = f.read()

# Extract skills from resume
resume_skills = extract_skills(resume_text)
print(f"Skills found in resume: {resume_skills}")
print(f"Number of skills: {len(resume_skills)}")

# Calculate match score
score = calculate_match_score(resume_text, job_description)
score_percentage = f"{score * 100:.1f}%"
print(f"Match score: {score_percentage}")

# Also extract skills from job description for comparison
job_skills = extract_skills(job_description)
print(f"Skills mentioned in job description: {job_skills}")
print(f"Number of job skills: {len(job_skills)}")

# Find matching skills
matching_skills = set(resume_skills) & set(job_skills)
print(f"Matching skills: {matching_skills}")
print(f"Number of matching skills: {len(matching_skills)}")
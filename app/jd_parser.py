import re
import spacy

nlp = spacy.load("en_core_web_sm")

def parse_job_description(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        jd_text = f.read()

    doc = nlp(jd_text)

    skills = extract_skills(jd_text)
    title = extract_title(doc)
    experience = extract_experience(jd_text)

    return {
        "job_title": title,
        "required_skills": skills,
        "experience_required": experience,
        "raw_text": jd_text
    }

def extract_title(doc):
    for ent in doc.ents:
        if ent.label_ == "ORG":
            continue
        if ent.label_ == "JOB_TITLE" or ent.label_ == "PERSON":
            return ent.text
    # fallback: use first line
    return doc.text.split('\n')[0].strip()

def extract_experience(text):
    match = re.search(r"(\d+)\+?\s+years? of experience", text, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None

def extract_skills(text):
    skill_keywords = ["python", "java", "c++", "sql", "excel", "tensorflow", "flask", "html", "css", "react", "docker"]
    found = []
    for word in skill_keywords:
        if re.search(rf"\b{word}\b", text, re.IGNORECASE):
            found.append

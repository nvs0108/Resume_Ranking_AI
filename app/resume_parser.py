import os
import re
import docx
import spacy
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    return extract_text(file_path)

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_email(text):
    match = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match[0] if match else None

def extract_phone(text):
    match = re.findall(r"\+?\d[\d\s\-]{8,}\d", text)
    return match[0] if match else None

def extract_skills(text):
    # Sample static skill list; you can make it dynamic later
    skill_keywords = ["python", "java", "c++", "sql", "excel", "tensorflow", "flask", "html", "css"]
    found = []
    for word in skill_keywords:
        if re.search(rf"\b{word}\b", text, re.IGNORECASE):
            found.append(word)
    return list(set(found))

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def parse_resume(file_path):
    ext = file_path.split(".")[-1]
    if ext == "pdf":
        text = extract_text_from_pdf(file_path)
    elif ext == "docx":
        text = extract_text_from_docx(file_path)
    else:
        return None

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "raw_text": text
    }

def parse_resumes(resume_folder):
    resumes_data = []
    for file in os.listdir(resume_folder):
        if file.endswith(".pdf") or file.endswith(".docx"):
            path = os.path.join(resume_folder, file)
            data = parse_resume(path)
            if data:
                data["file_name"] = file
                resumes_data.append(data)
    return resumes_data

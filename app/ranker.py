from sentence_transformers import SentenceTransformer, util

# Load BERT-like model for embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_candidates(resumes_data, job_desc_data):
    jd_text = job_desc_data["raw_text"]
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)

    ranked = []
    for resume in resumes_data:
        res_text = resume["raw_text"]
        res_embedding = model.encode(res_text, convert_to_tensor=True)

        # Cosine similarity score
        similarity = util.cos_sim(jd_embedding, res_embedding).item()

        # Additional bonus if required skills are present
        skill_match_count = len(set(resume["skills"]) & set(job_desc_data["required_skills"]))
        skill_boost = skill_match_count * 0.05  # Each matched skill gives a 0.05 boost

        # Experience boost (optional)
        experience_boost = 0
        if job_desc_data["experience_required"]:
            experience_boost = 0.1  # You can enhance this based on years

        total_score = round(similarity + skill_boost + experience_boost, 3)

        ranked.append({
            "name": resume.get("name") or resume.get("file_name"),
            "score": total_score,
            "skills": resume.get("skills"),
            "email": resume.get("email"),
            "phone": resume.get("phone")
        })

    # Sort by score (highest first)
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked

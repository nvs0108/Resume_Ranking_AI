from sentence_transformers import SentenceTransformer, util
import pandas as pd

model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_candidates(resumes, job_description):
    jd_text = job_description.get("skills", "") + " " + job_description.get("experience", "") + " " + job_description.get("education", "")

    jd_embedding = model.encode(jd_text, convert_to_tensor=True)

    ranked = []
    for res in resumes:
        resume_text = res.get("skills", "") + " " + res.get("experience", "") + " " + res.get("education", "")
        res_embedding = model.encode(resume_text, convert_to_tensor=True)
        similarity = float(util.pytorch_cos_sim(jd_embedding, res_embedding)[0][0])
        res["score"] = round(similarity * 100, 2)  # scale to 0-100
        ranked.append(res)

    ranked_df = pd.DataFrame(ranked).sort_values(by="score", ascending=False).reset_index(drop=True)
    return ranked_df

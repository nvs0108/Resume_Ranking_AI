from app.resume_parser import parse_resumes
from app.jd_parser import parse_job_description
from app.ranker import rank_candidates

def main():
    resumes_data = parse_resumes("data/resumes")
    job_desc = parse_job_description("data/job_descriptions/jd1.txt")
    ranked = rank_candidates(resumes_data, job_desc)
    print("Top Candidates:")
    for r in ranked:
        print(r['name'], "->", r['score'])

if __name__ == "__main__":
    main()

import pandas as pd
pd.DataFrame(ranked).to_csv("output/ranked_candidates.csv", index=False)

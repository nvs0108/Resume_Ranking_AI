import streamlit as st
import pandas as pd
import os
import tempfile

from app.resume_parser import parse_resume
from app.jd_parser import parse_job_description
from app.ranker import rank_candidates
from app.db import init_db, insert_candidate, get_all_candidates

# Init DB when app starts
init_db()

st.set_page_config(page_title="AI Resume Ranker", layout="wide")
st.title("🤖 AI Resume Screening & Candidate Ranking System")

st.sidebar.header("📤 Upload Files")

uploaded_jd = st.sidebar.file_uploader("Upload Job Description (.txt)", type="txt")
uploaded_resumes = st.file_uploader("Upload Resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

import io

if not df.empty:
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    st.download_button(
        label="⬇️ Download Ranked Candidates (CSV)",
        data=csv_buffer.getvalue(),
        file_name="ranked_candidates.csv",
        mime="text/csv"
    )
type=["pdf", "docx"], accept_multiple_files=True)

if uploaded_jd and uploaded_resumes:
    jd_path = tempfile.mktemp(suffix=".txt")
    with open(jd_path, "wb") as f:
        f.write(uploaded_jd.read())
    jd_data = parse_job_description(jd_path)

    resumes = []
    for res_file in uploaded_resumes:
        res_path = tempfile.mktemp(suffix=os.path.splitext(res_file.name)[-1])
        with open(res_path, "wb") as f:
            f.write(res_file.read())
        parsed = parse_resume(res_path)
        if parsed:
            parsed["file_name"] = res_file.name
            resumes.append(parsed)

    ranked = rank_candidates(resumes, jd_data)

    st.subheader("🏆 Ranked Candidates")
    df = pd.DataFrame(ranked)
    st.dataframe(df)

    if st.button("💾 Save to Database"):
        for r in ranked:
            insert_candidate(r)
        st.success("Saved all candidates to DB ✅")
    

# -----------------------------------------
st.markdown("---")
st.subheader("📊 Dashboard: View Stored Candidates")

candidates = get_all_candidates()
if candidates:
    df_db = pd.DataFrame(candidates, columns=["ID", "Name", "Email", "Phone", "Skills", "Score", "Resume File"])

    # Filter UI
    min_score = st.slider("Minimum Score", 0.0, 1.0, 0.5, 0.01)
    skill_filter = st.text_input("Filter by Skill (e.g., Python)").strip().lower()

    filtered_df = df_db[df_db["Score"] >= min_score]

    if skill_filter:
        filtered_df = filtered_df[filtered_df["Skills"].str.lower().str.contains(skill_filter)]

    st.dataframe(filtered_df)

    if not filtered_df.empty:
    csv_buffer2 = io.StringIO()
    filtered_df.to_csv(csv_buffer2, index=False)
    st.download_button(
        label="⬇️ Download Filtered Candidates (CSV)",
        data=csv_buffer2.getvalue(),
        file_name="filtered_candidates.csv",
        mime="text/csv"
    )

else:
    st.info("No candidates saved yet. Upload and save resumes to see dashboard.")

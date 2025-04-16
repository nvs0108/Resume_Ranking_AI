from flask import Flask, request, jsonify
import tempfile
import os

from app.resume_parser import parse_resume
from app.jd_parser import parse_job_description
from app.ranker import rank_candidates

app = Flask(__name__)

@app.route("/rank", methods=["POST"])
def rank_api():
    jd_file = request.files.get("job_description")
    resumes = request.files.getlist("resumes")

    if not jd_file or not resumes:
        return jsonify({"error": "Job description and resumes are required."}), 400

    jd_path = tempfile.mktemp(suffix=".txt")
    jd_file.save(jd_path)
    jd_data = parse_job_description(jd_path)

    parsed_resumes = []
    for res_file in resumes:
        res_path = tempfile.mktemp(suffix=os.path.splitext(res_file.filename)[-1])
        res_file.save(res_path)
        parsed = parse_resume(res_path)
        parsed["file_name"] = res_file.filename
        parsed_resumes.append(parsed)

    ranked = rank_candidates(parsed_resumes, jd_data)
    return jsonify(ranked)

if __name__ == "__main__":
    app.run(debug=True)

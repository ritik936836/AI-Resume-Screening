from flask import Flask, render_template, request
from extract_text import extract_text
from preprocess import preprocess
from similarity import (
    calculate_similarity,
    skill_match,
    get_resume_suggestions,
    final_score
)
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/", methods=["GET", "POST"])
def home():

    score = None
    matched_skills = []
    missing_skills = []
    suggestions = []

    if request.method == "POST":

        job = request.form.get("job", "")

        resume_file = request.files.get("resume_file")

        if resume_file:

            filepath = os.path.join(
                UPLOAD_FOLDER,
                resume_file.filename
            )

            resume_file.save(filepath)

            # Extract PDF Text
            resume_text = extract_text(filepath)

            # Preprocess
            resume_text = preprocess(resume_text)
            job = preprocess(job)

            # TF-IDF Score
            tfidf = calculate_similarity(
                resume_text,
                job
            )

            # Skills
            matched_skills, missing_skills = skill_match(
                resume_text,
                job
            )

            # Final Score
            score = final_score(
                tfidf,
                matched_skills,
                missing_skills
            )

            # Suggestions
            suggestions = get_resume_suggestions(
                missing_skills
            )

    return render_template(
        "index.html",
        score=score,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        suggestions=suggestions
    )


if __name__ == "__main__":
    app.run(debug=True)
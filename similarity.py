from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Technical skills list
SKILLS = [
    "python", "flask", "django", "machine learning",
    "deep learning", "data science", "sql", "mysql",
    "pandas", "numpy", "scikit-learn", "tensorflow",
    "opencv", "git", "github", "html", "css",
    "javascript", "react", "api", "rest api"
]


def calculate_similarity(resume_text, job_description):
    """
    Calculate TF-IDF Cosine Similarity
    """

    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform([resume_text, job_description])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])

    return similarity[0][0]


def skill_match(resume_text, job_description):

    resume = resume_text.lower()
    job = job_description.lower()

    matched = []
    missing = []

    for skill in SKILLS:

        if skill in job:

            if skill in resume:
                matched.append(skill.title())
            else:
                missing.append(skill.title())

    return matched, missing


def skill_score(matched_skills, missing_skills):

    total = len(matched_skills) + len(missing_skills)

    if total == 0:
        return 0

    return round((len(matched_skills) / total) * 100, 2)


def get_resume_suggestions(missing_skills):

    suggestions = []

    for skill in missing_skills:

        suggestions.append(
            f"Add '{skill}' to your resume if you have experience with it."
        )

    if len(missing_skills) == 0:
        suggestions.append(
            "Excellent! Your resume matches all required skills."
        )

    return suggestions


def final_score(tfidf_score, matched_skills, missing_skills):
    """
    Combine TF-IDF score and skill match score.
    """

    tfidf_percent = tfidf_score * 100

    skill_percent = skill_score(
        matched_skills,
        missing_skills
    )

    final = (tfidf_percent * 0.4) + (skill_percent * 0.6)

    return round(final, 2)
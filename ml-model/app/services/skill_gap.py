def extract_skills(text):
    text = text.lower()

    SKILL_CATEGORIES = {
        "backend": [
            "python", "java", "spring", "django", "flask", "fastapi",
            "node.js", "express", "rest api", "microservices"
        ],
        "frontend": [
            "html", "css", "javascript", "react", "angular", "vue",
            "bootstrap", "tailwind"
        ],
        "database": [
            "sql", "mysql", "postgresql", "mongodb", "firebase"
        ],
        "data_science_ml": [
            "machine learning", "deep learning", "tensorflow",
            "pytorch", "scikit learn", "pandas", "numpy",
            "data analysis", "nlp"
        ],
        "devops_cloud": [
            "docker", "kubernetes", "aws", "azure", "gcp",
            "ci cd", "jenkins", "linux"
        ],
        "mobile": [
            "android", "kotlin", "swift", "flutter", "react native"
        ],
        "testing": [
            "unit testing", "selenium", "jest", "cypress"
        ],
        "tools": [
            "git", "github", "jira", "postman"
        ],
        "accounting": [
            "accounting", "tally", "finance", "gst", "tax",
            "excel", "bookkeeping", "audit", "payroll"
        ],
        "soft_skills": [
            "communication", "leadership", "management", "teamwork"
        ]
    }

    all_skills = []
    for category in SKILL_CATEGORIES.values():
        all_skills.extend(category)

    return sorted(set([s for s in all_skills if s in text]))


def skill_gap_analysis(resume, jd):
    resume_skills = set(extract_skills(resume))
    jd_skills = set(extract_skills(jd))

    matching = list(resume_skills & jd_skills)
    missing = list(jd_skills - resume_skills)

    return matching, missing
def extract_skills(text):
    skills = [
        "python","machine learning","deep learning","tensorflow",
        "scikit learn","fastapi","flask","sql","pandas","numpy",
        "react","javascript","html","css","docker","aws"
    ]
    return [s for s in skills if s in text]


def skill_gap_analysis(resume, jd):
    resume_skills = set(extract_skills(resume))
    jd_skills = set(extract_skills(jd))

    matching = list(resume_skills & jd_skills)
    missing = list(jd_skills - resume_skills)

    return matching, missing
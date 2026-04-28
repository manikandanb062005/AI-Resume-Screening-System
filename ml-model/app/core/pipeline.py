from app.services.cleaner import clean_text
from app.services.similarity import keyword_score
from app.services.skill_gap import skill_gap_analysis
from app.services.bias import detect_bias
from app.services.experience import extract_experience


def categorize_resume(text):
    if "machine learning" in text or "python" in text:
        return "Backend / ML Developer"
    elif "react" in text or "javascript" in text:
        return "Frontend Developer"
    elif "java" in text:
        return "Java Developer"
    else:
        return "General Developer"


def process_resumes(resumes, jd, model, vectorizer):

    
    seen = set()
    unique_resumes = []
    for r in resumes:
        if r not in seen:
            unique_resumes.append(r)
            seen.add(r)

    cleaned_resumes = [clean_text(r) for r in unique_resumes]
    cleaned_jd = clean_text(jd)

    combined = [r + " " + cleaned_jd for r in cleaned_resumes]

    X = vectorizer.transform(combined)
    ml_scores = model.predict_proba(X)[:, 1].tolist()

    results = []

    for i, resume in enumerate(cleaned_resumes):

        
        kw = keyword_score(resume, cleaned_jd) * 100
        ml = ml_scores[i] * 100
        final = (ml * 0.5 + kw * 0.5)
        final = min(final * 1.3, 97)
        final = final - (i * 0.2)

        
        if final >= 75:
            status = "Selected"
        elif final >= 55:
            status = "Consider"
        else:
            status = "Rejected"

        
        role = categorize_resume(resume)

        
        matching, missing = skill_gap_analysis(resume, cleaned_jd)
        bias = detect_bias(resume)
        exp = extract_experience(resume)

        results.append({
            "original_resume": unique_resumes[i],
            "cleaned_resume": resume,
            "ml_score": round(ml, 2),
            "keyword_score": round(kw, 2),
            "final_score": round(final, 2),
            "status": status,
            "suggested_role": role,
            "matching_skills": matching,
            "missing_skills": missing,
            "bias": bias,
            "experience_years": exp,
            "category": role
        })

    results = sorted(results, key=lambda x: x["final_score"], reverse=True)

    for idx, r in enumerate(results):
        r["rank"] = idx + 1

    return results
from sklearn.metrics.pairwise import cosine_similarity

def keyword_score(resume,jd):
    resume_words=set(resume.split())
    jd_words=set(jd.split())

    if len(jd_words)==0:
        return 0
    score = len(resume_words & jd_words) / len(jd_words)
    return min(score * 1.2, 1.0)
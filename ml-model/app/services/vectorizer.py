from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize(resume,jd):
    corpus=resume + [jd]
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(corpus)
    return vectors
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, classification_report, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer

from xgboost import XGBClassifier

from app.services.cleaner import clean_text


df = pd.read_csv("src/resume_screening_dataset.csv")



df["resume"] = df["resume"].apply(clean_text)
df["job_description"] = df["job_description"].apply(clean_text)



df["text"] = df["resume"] + " " + df["job_description"]


X = df["text"]
y = df["label"]



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)



vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2),
    stop_words='english'
)

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)



param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [4, 6],
    'learning_rate': [0.05, 0.1]
}

model = GridSearchCV(
    XGBClassifier(
        eval_metric='logloss',
        use_label_encoder=False
    ),
    param_grid,
    cv=5,
    scoring='f1',
    verbose=1,
    n_jobs=-1
)

model.fit(X_train_vectorized, y_train)

print("Best parameters:", model.best_params_)

model = model.best_estimator_


y_pred = model.predict(X_test_vectorized)
y_pred_proba = model.predict_proba(X_test_vectorized)[:, 1]



print("Accuracy:", accuracy_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, y_pred_proba))

print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))



pickle.dump(model, open("models/model.pkl", "wb"))
pickle.dump(vectorizer, open("models/vectorizer.pkl", "wb"))

print("\nModel and vectorizer saved successfully ")
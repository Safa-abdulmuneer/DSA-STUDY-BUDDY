import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_csv("ml/leetcode_dataset.csv")

# Combine title + description for better matching
df["text"] = df["title"].astype(str) + " " + df["description"].astype(str)

# Vectorize
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X = vectorizer.fit_transform(df["text"])

# Save model
with open("ml/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("ml/model.pkl", "wb") as f:
    pickle.dump(X, f)

print("ML trained successfully")

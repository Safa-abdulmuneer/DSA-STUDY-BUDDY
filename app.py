from flask import Flask, request, jsonify, render_template, session
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.secret_key = "dsa-study-buddy"

# Load dataset
df = pd.read_csv("ml/leetcode_dataset.csv")
df["text"] = df["title"].astype(str) + " " + df["description"].astype(str)

# Load ML artifacts
vectorizer = pickle.load(open("ml/vectorizer.pkl", "rb"))
X = pickle.load(open("ml/model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    query = data.get("text")
    action = data.get("action")

    if not query:
        return jsonify({"error": "No input provided"})

    # ML search
    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, X)
    idx = similarity.argmax()
    row = df.iloc[idx]

    # Different behavior per button
    if action == "explain":
        result = f"""
Problem Title:
{row['title']}

Description:
{row['description']}
"""

    elif action == "summarize":
        result = f"""
Problem: {row['title']}
Difficulty: {row['difficulty']}
Acceptance Rate: {row['acceptance_rate']}%

Topics:
{row['related_topics']}
"""

    elif action == "quiz":
        result = f"""
Quiz based on this DSA problem:

1. Which data structure is primarily used?
2. What is the time complexity?
3. Can this be solved using recursion?
4. Is dynamic programming applicable?
5. What is the space complexity?
"""

    else:
        result = "Invalid action."

    session["result"] = result
    return jsonify({"redirect": "/result"})

@app.route("/result")
def result():
    return render_template("result.html", result=session.get("result"))

if __name__ == "__main__":
    app.run(debug=True)

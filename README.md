# DSA Study Buddy 🧠📘

An AI-powered web application that helps students learn Data Structures and Algorithms (DSA) by retrieving and explaining relevant problems using machine learning–based text similarity.

The system allows users to enter a DSA topic or LeetCode problem name and returns the most relevant problem explanation from a curated dataset in a clean and readable format.

# 📌 Problem Statement

Students often face difficulty understanding DSA concepts due to:

Scattered learning resources

Lack of personalized explanations

Difficulty mapping topics to relevant problems

Searching online frequently results in irrelevant or overwhelming content.

This project addresses the problem by providing:

A centralized DSA learning assistant

Offline, dataset-driven explanations

A simple and intuitive web interface

Explainable ML-based retrieval instead of black-box AI

# 🎯 Objectives

Allow users to search DSA topics or problem names

Retrieve the most relevant DSA problem from a dataset

Display detailed explanations in a structured format

Use machine learning for similarity-based matching

Keep the system lightweight and offline (no API dependency)

 # 🧠 System Overview

The system follows a Machine Learning–based Information Retrieval approach:

TF-IDF Vectorization to represent textual data

Cosine Similarity to measure relevance

Flask-based backend for processing

Web-based frontend for interaction

Workflow:

User enters a DSA topic or problem name

Input text is preprocessed

TF-IDF converts text into numerical vectors

Cosine similarity compares input with dataset problems

Most relevant problem is selected

Detailed explanation is displayed on a result page

 # 🏗️ Architecture

User Interface (HTML/CSS/JS)
⬇
Flask Backend Server
⬇
Text Preprocessing Module
⬇
TF-IDF Vectorizer
⬇
Cosine Similarity Engine
⬇
LeetCode-based Dataset (CSV)
⬇
Result Generation & Display

 # 🧪 Technologies Used
Frontend

HTML5

CSS3

JavaScript

Backend

Python

Flask

Machine Learning

Scikit-learn

TF-IDF Vectorizer

Cosine Similarity

Data Handling

Pandas

NumPy

Development Tools

VS Code

GitHub

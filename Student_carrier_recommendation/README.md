# 🎓 Career Recommendation System

This project is a machine learning-based **Career Recommendation System** that helps students identify suitable career paths based on academic scores, study habits, and personal activities. The system also includes a **Streamlit web app** for real-time predictions.

---

## 🔍 Overview

This system:
- Analyzes over 6,000 student records
- Predicts a career aspiration from 17 possible options
- Uses machine learning models like **KNN, Naive Bayes, Random Forest, and SVM**
- Incorporates **SMOTE** for class balancing
- Visualizes trends using **Matplotlib** and **Seaborn**
- Provides an interactive **Streamlit** app for user input

---

## 🧠 Career Classes

The system predicts one of the following career aspirations:

Lawyer, Doctor, Government Officer, Artist, Social Network Studies,
Software Engineer, Teacher, Business Owner, Scientist,
Banker, Writer, Accountant, Designer, Construction Engineer,
Game Developer, Stock Investor, Real Estate Developer

yaml
Copy
Edit

---

## 📊 Exploratory Data Analysis

The project includes visualizations for:
- Gender distribution (Pie chart)
- Weekly self-study hours (Histogram)
- Career aspiration distribution (Countplot)

---

## 📁 Dataset & Preprocessing

- `student-scores-6k.csv` contains student data.
- Columns like `id`, `name`, `email` are dropped.
- Scores across 7 subjects are combined into `total_score` and `average_score`.
- Categorical features are encoded using `LabelEncoder`.

---

## 🏗️ Machine Learning Pipeline

- **Features (`X`)**: Subject scores, study hours, job status, etc.
- **Target (`y`)**: Encoded career aspiration
- **Models Used**:
  - KNeighborsClassifier
  - Gaussian Naive Bayes
  - Random Forest Classifier
  - Support Vector Classifier (SVC)
- **Data Splitting**: `train_test_split` with 80-20 ratio
- **Imbalanced Data Handling**: `SMOTE` applied on training data

---

## ✅ Model Evaluation

Each model is evaluated using:
- Accuracy Score
- Confusion Matrix
- Classification Report

**Best performing model** is saved as:  
`career_recommendation.pkl`

---

## 🌐 Streamlit Web App

A user-friendly interface built with **Streamlit** allows:
- Manual input of student scores and attributes
- Instant prediction of career aspiration
- Real-time display of total and average score



## Output :

<img width="1700" height="989" alt="Image" src="https://github.com/user-attachments/assets/c2f55b93-2781-4440-ac24-6529f4b3d836" />

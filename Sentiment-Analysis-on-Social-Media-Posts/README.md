🛍️ Amazon Review Sentiment Analysis (BiLSTM + Flask)
This project uses Natural Language Processing (NLP) and a Bidirectional LSTM neural network to predict whether an Amazon product review is positive or negative. It is trained on a subset of Amazon reviews and served via a Flask web app for interactive predictions.

🔍 Overview
Data: Amazon product reviews dataset (train.ft.txt.bz2 & test.ft.txt.bz2)

Model: Deep learning model using Bidirectional LSTM, trained on 12,000 reviews

Text Processing: Cleaning, stemming, stopword removal, and tokenization

Deployment: Flask-based web app for real-time sentiment prediction

📊 Dataset
train.ft.txt.bz2: 12,000 training samples

test.ft.txt.bz2: 2,500 test samples

Each line is prefixed with a label (__label__1 or __label__2)

⚙️ Model Architecture
Embedding Layer (1000 words, 300-dim)

Bidirectional LSTM (2 layers with 128 units each)

Layer Normalization + Dropout

Dense layers with ReLU and Sigmoid for binary classification

📈 Model Evaluation
After training the model for up to 50 epochs (with early stopping), we observed the following results on the test set:

matlab
Copy
Edit
Accuracy       : 83%
Precision (0)  : 82%
Recall (0)     : 82%
F1-Score (0)   : 82%
Precision (1)  : 84%
Recall (1)     : 84%
F1-Score (1)   : 84%
✅ Confusion Matrix:

lua
Copy
Edit
[[ 979  212]
 [ 212 1097]]
💻 Web App (Flask)
The trained LSTM model is deployed using a Flask app:

Features:
Input: Any English sentence

Output: Sentiment prediction (Positive 😊 / Negative 😡) with confidence score

Example:
text
Copy
Edit
Input:   "This is the worst product I’ve ever used."
Output:  Sentiment: Negative 😡  (Confidence: 0.0041)
📂 File Structure
arduino
Copy
Edit
📁 amazon-review-sentiment/
├── model/
│   ├── lstm_model.h5
│   └── tokenizer.pkl
├── templates/
│   └── index.html
├── static/
│   └── (optional CSS/image files)
├── app.py
├── README.md
├── train.ft.txt.bz2
├── test.ft.txt.bz2
└── requirements.txt
📦 Libraries Used
TensorFlow / Keras

NLTK (stopwords, stemming)

NumPy

Matplotlib

Flask

scikit-learn (metrics)

🧠 How It Works (Core Pipeline)
Data Extraction → Load .bz2 files

Label Processing → Convert to binary (0 for negative, 1 for positive)

Text Cleaning → Lowercase, remove special characters, stem words

Tokenization + Padding

Model Training → BiLSTM + Dropout + LayerNorm

Evaluation & Deployment

✅ Results Summary
Achieved 83% accuracy on unseen test data

Strong performance across both positive and negative reviews

Robust to various phrasing and expressions

🧾 Conclusion
This project demonstrates a complete end-to-end sentiment analysis pipeline — from raw review data to model deployment via Flask. The BiLSTM model efficiently captures text context and performs binary classification with high accuracy.


![Image](https://github.com/user-attachments/assets/0df74dc6-4a54-4943-8f7d-0b880fd3bb14)
![Image](https://github.com/user-attachments/assets/6109ccbe-88b8-4ff7-b5ed-bf7acca3b089)


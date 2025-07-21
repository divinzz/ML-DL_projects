# 🤖 Amazon Product Review Sentiment Analysis using LSTM 🚀

This project performs **sentiment analysis** on Amazon product reviews using **Deep Learning (LSTM)** and provides a **real-time prediction web app using Flask**. It classifies reviews as **Positive 😊** or **Negative 😡**, helping businesses and users gain quick insights into customer feedback.

---

## 📌 Project Highlights

- 🔍 Dataset: Amazon Reviews (`train.ft.txt.bz2`, `test.ft.txt.bz2`)
- 🧼 Preprocessing: Label parsing, cleaning, stemming, stopword removal
- 📊 Tokenization: Keras Tokenizer + Padding
- 🧠 Model: Bidirectional LSTM with Dropout & LayerNormalization
- 🖥️ Frontend: Flask Web App for live sentiment predictions
- 🧪 Accuracy: ~83% on validation data
- ✅ Confusion Matrix & Classification Report generated

---

## 🗂️ Folder Structure

├── app.py # Flask Web App
├── lstm_model.h5 # Trained LSTM Model
├── tokenizer.pkl # Saved Tokenizer
├── templates/
│ └── index.html # Frontend HTML
├── static/ (optional) # For CSS/JS if added
├── amazonreviews.zip # Original dataset

yaml
Copy
Edit

---

## 🧰 Tech Stack

- Python 3.10+
- TensorFlow / Keras
- NLTK
- NumPy, Matplotlib, re
- Flask
- HTML/CSS (optional for styling)

---

📊 Model Performance
text
Copy
Edit
Confusion Matrix:
[[ 979  212]
 [ 212 1097]]

Accuracy: 83%
Precision: 82% (Neg), 84% (Pos)
F1-score: 83%
📈 Result Summary & Conclusion
The model achieves 83% accuracy on the test set.

It effectively distinguishes between positive and negative reviews.

The app performs real-time sentiment classification through a clean Flask interface.

Conclusion: This model and app demonstrate how deep learning can be applied to practical NLP problems like sentiment analysis on real-world data.


![Image](https://github.com/user-attachments/assets/0df74dc6-4a54-4943-8f7d-0b880fd3bb14)
![Image](https://github.com/user-attachments/assets/6109ccbe-88b8-4ff7-b5ed-bf7acca3b089)


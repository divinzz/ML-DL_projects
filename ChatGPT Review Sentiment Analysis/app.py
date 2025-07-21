import joblib
import re
import nltk
from flask import Flask, render_template, request
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = re.sub(r'\s+', ' ', text)  
    text = re.sub(r'[^\w\s]', '', text)  
    text = re.sub(r'\d+', '', text)  
    text = text.lower()  
    words = text.split()  
    return " ".join([word for word in words if word not in stop_words])  

model = joblib.load('C:\\Users\\ACER\\Documents\\ml prjt\\chatGPT_review\\sentiment_model.pkl')
vectorizer = joblib.load('C:\\Users\\ACER\\Documents\\ml prjt\\chatGPT_review\\vectorizer.pkl')
label_encoder = joblib.load('C:\\Users\\ACER\\Documents\\ml prjt\\chatGPT_review\\label_encoder.pkl')

def predict_sentiment(new_review):
    new_review_cleaned = preprocess_text(new_review)
    review_vectorized = vectorizer.transform([new_review_cleaned])
    prediction = model.predict(review_vectorized)
    sentiment = label_encoder.inverse_transform(prediction)
    return sentiment[0]

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Sentiment prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        if review:
            sentiment = predict_sentiment(review)
            return render_template('index.html', sentiment=sentiment, review=review)
        else:
            return render_template('index.html', sentiment="Please enter a review.")

if __name__ == "__main__":
    app.run(debug=True)

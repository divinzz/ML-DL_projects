import joblib
import re
import nltk
from textblob import TextBlob

nltk.download('stopwords')
from nltk.corpus import stopwords

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

if __name__ == "__main__":
    review = input("Enter a review: ")  
    sentiment = predict_sentiment(review)  
    print(f"The sentiment of the review is: {sentiment}") 

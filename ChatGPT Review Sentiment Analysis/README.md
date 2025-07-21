# ChatGPT Review Sentiment Analysis

## About the Project

### Introduction

In today's data-driven world, extracting meaningful insights from text data is more crucial than ever. User feedback, especially in the form of reviews, plays a pivotal role in shaping the direction of digital products and services. Whether through online platforms or direct customer interactions, understanding the sentiment behind reviews can greatly influence how businesses and developers respond to their audiences. This project focuses on performing **Sentiment Analysis** on user reviews for the popular AI model, **ChatGPT**.

Sentiment analysis is a key aspect of natural language processing (NLP) that involves classifying text data based on its emotional tone, often into categories like **positive**, **neutral**, or **negative**. By applying this method to user reviews, we can help product teams understand how users feel about ChatGPT, what they like, and what needs improvement. This can significantly improve decision-making, enhance customer satisfaction, and influence future developments of the product.

### Why Sentiment Analysis?

The power of sentiment analysis lies in its ability to analyze vast amounts of unstructured text data and generate insights that can be acted upon. For businesses, understanding how customers feel is essential to offering a product or service that aligns with their needs and expectations. Traditional methods of gathering feedback, such as surveys and focus groups, are time-consuming and limited in scale. In contrast, sentiment analysis can process thousands, if not millions, of reviews in a matter of seconds, delivering actionable insights at scale.

By analyzing user reviews of ChatGPT, we can identify key trends in user sentiment, gauge the overall satisfaction level, and detect any potential issues users might be facing. This insight can guide product development teams in improving the AI’s performance, user interface, and features, ultimately resulting in a more user-friendly and reliable product.

### Project Overview

This project is a **ChatGPT Sentiment Analysis** system that processes a large dataset of user reviews and classifies them into **Positive**, **Neutral**, or **Negative** sentiment categories. We used various techniques from **Natural Language Processing (NLP)** and machine learning to build this model, and it can be deployed to predict sentiment on new, unseen reviews.

The project involves:

- **Data Preprocessing**: Handling missing values, cleaning text data (removing punctuation, digits, and stop words), and tokenizing text.
- **Feature Extraction**: Converting raw text data into numerical form using techniques like **TF-IDF** (Term Frequency-Inverse Document Frequency).
- **Model Building**: Training several machine learning models, including **K-Nearest Neighbors (KNN)**, **XGBoost**, **Logistic Regression**, **Decision Trees**, and **Naive Bayes** for sentiment classification.
- **Evaluation**: Using metrics like **accuracy**, **precision**, **recall**, and **F1-score** to evaluate model performance.
- **Deployment**: Saving the trained model, vectorizer, and label encoder using **Joblib** for deployment in production environments.

### Key Features

- **Sentiment Categorization**: Classifies user reviews as **Positive**, **Neutral**, or **Negative** based on their sentiment.
- **Visualization**: Generates insightful visualizations, such as sentiment distribution over time, review counts by month, and word clouds to show the most common words in reviews.
- **Model Performance**: Achieves high accuracy scores with **Logistic Regression** performing the best among other classifiers.
- **Text Preprocessing**: Uses text-cleaning techniques like punctuation removal, case normalization, and stopword filtering to improve model accuracy.

### Technologies Used

- **Python**: The programming language used for data processing, model building, and deployment.
- **Pandas**: For data manipulation and cleaning.
- **NLTK & TextBlob**: For natural language processing tasks, including stopword removal and sentiment analysis.
- **Scikit-Learn**: Used for feature extraction, model building, and evaluation.
- **XGBoost**: A powerful gradient boosting library used for training models.
- **Matplotlib & Seaborn**: For generating visualizations.
- **Joblib**: For model serialization and saving pre-trained models.

### Benefits of This Project

1. **Scalability**: The system can process large volumes of reviews quickly, offering insights from thousands of reviews with minimal time and effort.
2. **Real-Time Insights**: By analyzing live user feedback, product managers and developers can act quickly on user sentiments and make necessary adjustments to improve the product.
3. **Data-Driven Decisions**: The project empowers businesses to make decisions based on real user feedback, improving user experience and satisfaction.

### Conclusion

The ChatGPT Sentiment Analysis project demonstrates how machine learning and natural language processing can be effectively used to understand and categorize user sentiment. By automating sentiment analysis, businesses can save time, gain valuable insights, and enhance their products or services accordingly. This project provides a framework that can be extended to other domains where text data is abundant and feedback analysis is crucial.

# OUTPUT OF THE TASK

![Image](https://github.com/user-attachments/assets/f48ba0aa-3a5a-459c-a60a-be8ac952eb5a)
![Image](https://github.com/user-attachments/assets/d538e505-5ed3-44de-80fa-84da860ba597)
![Image](https://github.com/user-attachments/assets/84111e20-9b0d-4a72-ac50-14a1630d6173)

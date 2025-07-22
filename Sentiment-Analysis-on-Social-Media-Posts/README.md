# 🛍️ Amazon Product Review Sentiment Analysis using LSTM & Flask

This project uses **Natural Language Processing (NLP)** and **Deep Learning** to classify Amazon product reviews as **positive** or **negative**. A **Bidirectional LSTM** model processes text data efficiently, and a simple **Flask web app** allows for real-time user interaction.

---

## 📌 Project Highlights

- 🧹 **Preprocessing**: Text cleaning, stemming, stopword removal, and tokenization.
- 📊 **EDA**: Word clouds for positive/negative reviews, review length distributions, class balance check.
- 🧠 **Model**: Bidirectional LSTM using embedding, dropout, normalization, and dense layers.
- 🌐 **Flask Web Interface**: Enter a review in the browser and get instant sentiment feedback.
- 🎯 **Performance**: Achieved ~83% test accuracy.

---

## 🧠 Model Summary

- **Embedding Layer** – Converts text to numerical format
- **Bidirectional LSTM** – Processes sequences in both directions
- **Dropout & Normalization** – Improves generalization
- **Dense Output Layer** – Predicts sentiment (positive/negative)

---

## 📊 Evaluation Metrics

- **Test Accuracy**: ~83%
- **Confusion Matrix**:

[[979 212]
[212 1097]]


- **Precision**:  
- Positive: 84%  
- Negative: 82%
- **F1 Score**: ~83%
---

## 🧾 Conclusion

This project demonstrates how **deep learning** and **NLP** techniques can be applied to sentiment classification tasks in real-world scenarios. Using a **Bidirectional LSTM** architecture, we achieved strong performance in identifying sentiment from Amazon reviews. 

By integrating the model with a **Flask web interface**, the system becomes interactive and user-friendly — allowing anyone to test the model with custom inputs in real time.

It lays the groundwork for scalable applications like customer feedback analysis, product review filtering, and automated moderation systems.


<img width="1912" height="979" alt="Image" src="https://github.com/user-attachments/assets/d477d03f-c5dd-45ad-a949-c6249b664cb4" />
<img width="1905" height="981" alt="Image" src="https://github.com/user-attachments/assets/9a5bb61a-a9c5-4b15-a7b6-55f00c5f1862" />


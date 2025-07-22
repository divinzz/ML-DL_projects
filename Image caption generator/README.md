# 🧠📸 Image Caption Generator using Deep Learning

This project generates human-like captions for images using a CNN-RNN deep learning architecture trained on the Flickr8k dataset. The model uses **DenseNet201** for image feature extraction and an **LSTM** decoder for generating natural language descriptions.

---

## 📂 Dataset

- **Name**: [Flickr8k](https://www.kaggle.com/datasets/adityajn105/flickr8k)
- **Size**: ~8,000 images with 5 captions each
- **License**: [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/)

---

## 🧰 Tech Stack

- **Language**: Python
- **Libraries**: TensorFlow, NumPy, Pandas, Matplotlib, Pillow, TQDM
- **Model**:
  - CNN: DenseNet201 (pre-trained on ImageNet)
  - RNN: LSTM-based sequence model
- **Deployment**: [Streamlit](https://streamlit.io/)

---

## 🏗️ Project Structure

image-caption-generator/
├── app.py # Streamlit web app
├── model.keras # Trained caption generator model
├── feature_extractor.keras # DenseNet201 feature extractor
├── tokenizer.pkl # Saved tokenizer
├── flickr8k/ # Dataset folder
│ ├── Images/
│ └── captions.txt
├── requirements.txt
└── README.md # You're here!

yaml
Copy
Edit

---

## 🚀 How to Run Locally

3. Prepare Dataset
Download from Kaggle: Flickr8k Dataset

Unzip inside flickr8k/ folder:

Copy
Edit
flickr8k/
├── Images/
└── captions.txt
4. Train the Model
Model training includes:

Caption cleaning and tokenization

Feature extraction with DenseNet201

LSTM-based caption generation

Training snippet:

python
Copy
Edit
caption_model.fit(
    train_generator,
    epochs=50,
    validation_data=validation_generator,
    callbacks=[checkpoint, earlystopping, learning_rate_reduction]
)
5. Save Trained Models
python
Copy
Edit
model.save("model.keras")
feature_extractor.save("feature_extractor.keras")

import pickle
with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)
🌐 Launch Streamlit App
bash
Copy
Edit
streamlit run app.py
✅ App Features
Upload any .jpg, .jpeg, or .png image

View generated caption instantly

Visual output of image + caption

🧠 Model Insights
Metric	Value
Train Loss	~3.1
Val Loss	~3.6
Epochs	14
Optimizer	Adam


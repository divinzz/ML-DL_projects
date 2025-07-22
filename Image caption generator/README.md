# 🖼️ Image Caption Generator 🧠

Automatically generate captions for images using Deep Learning (CNN + LSTM).  
Built with TensorFlow and deployed using Streamlit.

---

## 📚 Overview

This project uses a **pre-trained DenseNet201** to extract visual features from images and an **LSTM decoder** to generate natural language captions.  
Trained on the [Flickr8k Dataset](https://www.kaggle.com/datasets/adityajn105/flickr8k), each image has 5 ground-truth captions.

---

## 🚀 Features

- 📷 Feature Extraction with DenseNet201
- 🧠 Sequence Modeling using LSTM
- 🗣️ Custom Tokenizer with start/end tokens
- 📊 Training with Early Stopping & LR Scheduler
- 🌍 Streamlit Web App for live captioning

---

## 🛠️ Installation

```bash
git clone https://github.com/YOUR-USERNAME/image-caption-generator.git
cd image-caption-generator
pip install -r requirements.txt
📁 Folder Structure
bash
Copy
Edit
image-caption-generator/
│
├── app.py                   # Streamlit interface
├── model.keras              # Trained captioning model
├── feature_extractor.keras # CNN (DenseNet201)
├── tokenizer.pkl            # Saved tokenizer
├── flickr8k/                # Dataset folder
│   ├── Images/
│   └── captions.txt
└── requirements.txt
🧪 Run the Project
1. 📥 Download Dataset
From Kaggle: https://www.kaggle.com/datasets/adityajn105/flickr8k
Extract into flickr8k/ with the following structure:

Copy
Edit
flickr8k/
├── Images/
└── captions.txt
2. 🏋️‍♀️ Train the Model
python
Copy
Edit
caption_model.fit(
    train_generator,
    epochs=50,
    validation_data=validation_generator,
    callbacks=[checkpoint, earlystopping, learning_rate_reduction]
)
3. 💾 Save Components
python
Copy
Edit
model.save("model.keras")
feature_extractor.save("feature_extractor.keras")

import pickle
with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)
4. 🌐 Run the Web App
bash
Copy
Edit
streamlit run app.py
📸 Sample Output
Image:
1026685415_0431cbf574.jpg

Generated Caption:

css
Copy
Edit
a dog running across a grassy field
📉 Training Summary
Metric	Value
Train Loss	~3.1
Val Loss	~3.6
Epochs	14
Optimizer	Adam

✅ Requirements
Python 3.10+

TensorFlow

Pandas

NumPy

Matplotlib

Pillow

TQDM

Streamlit

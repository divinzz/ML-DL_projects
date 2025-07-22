# 🧠📸 Image Caption Generator

This project generates descriptive captions for images using a deep learning model combining **DenseNet201** for image feature extraction and **LSTM** for language generation. The app is trained on the [Flickr8k dataset](https://www.kaggle.com/datasets/adityajn105/flickr8k) and deployed using **Streamlit**.

---


## 📁 Project Structure

image-caption-generator/
│
├── app.py # Streamlit application
├── model.keras # Trained caption generation model
├── feature_extractor.keras # DenseNet201 feature extractor
├── tokenizer.pkl # Tokenizer used for caption encoding
├── flickr8k/ # Dataset folder
│ ├── Images/
│ └── captions.txt
├── requirements.txt # List of Python dependencies
└── README.md

yaml
Copy
Edit

---

## 📦 Installation

```bash
git clone https://github.com/your-username/image-caption-generator.git
cd image-caption-generator
pip install -r requirements.txt
📥 Dataset
Download the dataset: Flickr8k - Kaggle

Unzip the contents into the flickr8k/ directory as follows:


flickr8k/
├── Images/
└── captions.txt
🛠️ Model Training Steps
Caption Preprocessing

Lowercase, remove punctuation, clean spacing

Add startseq and endseq tokens

Tokenization

python
Copy
Edit
from tensorflow.keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(captions)
Feature Extraction with DenseNet201

python
Copy
Edit
fe = Model(inputs=model.input, outputs=model.layers[-2].output)
Sequence Modeling with LSTM
Combined with image features using a custom architecture.

Model Training

python
Copy
Edit
caption_model.fit(
    train_generator,
    epochs=50,
    validation_data=validation_generator,
    callbacks=[checkpoint, earlystopping, learning_rate_reduction]
)
Saving Models

python
Copy
Edit
caption_model.save("model.keras")
feature_extractor.save("feature_extractor.keras")
with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)
🖥️ Running the Streamlit App
bash
Copy
Edit
streamlit run app.py
Then open http://localhost:8501 in your browser.

📷 Example Output
Input Image


Generated Caption

text
Copy
Edit
a dog running across a grassy field
📊 Training Results
Metric	Value
Train Loss	~3.1
Val Loss	~3.6
Optimizer	Adam
Epochs	14

✅ Requirements
Install all dependencies using:

pip install -r requirements.txt
Contents of requirements.txt:

nginx
Copy
Edit
tensorflow
numpy
pandas
matplotlib
pillow
tqdm
streamlit

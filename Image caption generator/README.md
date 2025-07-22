# 🖼️ Image Caption Generator

This project generates image captions using a CNN-RNN architecture trained on the **Flickr8k** dataset. It uses **DenseNet201** for feature extraction and an **LSTM decoder** to generate descriptive captions. The model is deployed with a user-friendly **Streamlit** app.

---

## 📁 Dataset

- **Flickr8k**: 8000+ images with five captions per image.
- Download from [Kaggle](https://www.kaggle.com/datasets/adityajn105/flickr8k)

---

## 🧠 Model Overview

- **Feature Extractor**: DenseNet201 (pretrained)
- **Decoder**: LSTM with embedding + dense layers
- **Loss**: Categorical Crossentropy
- **Optimizer**: Adam

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/image-caption-generator.git
cd image-caption-generator
2. Install required packages
bash
Copy
Edit
pip install -r requirements.txt
Required Libraries:

tensorflow

numpy

pandas

matplotlib

tqdm

streamlit

pickle

You can create a requirements.txt file with these.

3. Download and extract dataset
Place the dataset files (Images/, captions.txt) inside a flickr8k/ directory in your project root.

4. Train the model (Optional)
Use the provided training notebook or scripts.

5. Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
🎯 Features
Extracts image features with DenseNet201

Tokenizes and encodes captions

Trains a caption generation model

Saves model and tokenizer

Interactive caption generation with Streamlit

🖼️ Example Output
Image:
(Upload your own in the app)

Generated Caption:
"a young boy is playing with a dog in the park"

🧪 Model Info
Best val_loss: ~3.60

Early stopping after 14 epochs



<img width="680" height="848" alt="Image" src="https://github.com/user-attachments/assets/b6677501-6d53-49da-b157-18dc62af5aa4" />


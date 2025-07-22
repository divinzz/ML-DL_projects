# 🖼️ Image Caption Generator

A deep learning project that automatically generates captions for images using a CNN-RNN architecture. This implementation uses the **Flickr8k** dataset, **DenseNet201** as the feature extractor, and a custom LSTM decoder. The project is also deployed using **Streamlit** for interactive use.

---

## 📁 Dataset

- **Name**: [Flickr8k](https://www.kaggle.com/datasets/adityajn105/flickr8k)
- **Contents**:
  - 8,000+ images (`Images/`)
  - Corresponding captions in `captions.txt`

---

## 🧠 Model Architecture

- **Feature Extractor**: DenseNet201 (pre-trained on ImageNet, outputs 1920-dimensional features)
- **Caption Generator**: 
  - Embedding Layer
  - LSTM (256 units)
  - Dense layers for final vocabulary prediction
- **Loss Function**: Categorical Crossentropy
- **Optimizer**: Adam
- **Training Strategy**: Custom `DataGenerator` with image and sequence inputs

---

## 🔧 Features

- Custom preprocessing for image and text
- Feature extraction and tokenizer saving/loading
- Training with checkpointing, early stopping, and learning rate reduction
- Caption generation with greedy decoding
- Streamlit app for interactive caption generation

---


---

## 📂 Project Structure

.
├── flickr8k/ # Unzipped dataset
│ ├── Images/
│ └── captions.txt
├── model.keras # Trained caption model
├── feature_extractor.keras # DenseNet201 feature extractor
├── tokenizer.pkl # Saved tokenizer
├── app.py # Streamlit web app
├── train_model.ipynb # Jupyter Notebook with full training pipeline
└── README.md


---


1 Install required packages

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

2. Download and extract dataset 

Place the dataset files (Images/, captions.txt) inside a flickr8k/ directory in your project root.

3. Train the model (Optional)

Use the provided training notebook or scripts.

4. Run the Streamlit App

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




## 🖼️ Example Output

<img width="680" height="848" alt="Image" src="https://github.com/user-attachments/assets/b6677501-6d53-49da-b157-18dc62af5aa4" />

**Generated Caption:**  
`"a young boy is playing with a dog in the park"`




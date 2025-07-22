# 👗 Fashion Recommendation System

The Fashion Recommendation System is a content-based image retrieval (CBIR) application that recommends visually similar fashion items based on a reference image. It leverages deep learning for image feature extraction and computes similarity between images to find the best matches from a fashion dataset.

This project is ideal for use cases such as:
- Online shopping experiences
- Virtual styling assistants
- Personal wardrobe management tools

---

## 📌 Project Overview

This system processes fashion item images to extract high-dimensional embeddings using a pretrained Convolutional Neural Network (CNN). These embeddings are used to measure similarity between items. When a user uploads an image, the system compares it against the dataset and displays the top visually similar recommendations.

The project is packaged into a clean web application using [Streamlit](https://streamlit.io/), allowing users to interact with the model in real time.

---

## 🧱 Project Structure

.
├── app.py # Main Streamlit web app
├── fashion_recommendation_model.ipynb # Notebook for preprocessing & model testing
├── recommendation_utils.py # Feature extraction and similarity functions
├── fashion.pkl # Pickled feature data or index for fast similarity search
├── data/ # Directory containing fashion images
└── requirements.txt # List of dependencies

yaml
Copy
Edit

---

## 🚀 How to Use

> 💡 Before starting, make sure you have Python 3.7+ installed.

### 1. Install Required Libraries

Install the dependencies by running:

```bash
pip install -r requirements.txt
Or manually install the key packages:

bash
Copy
Edit
pip install streamlit opencv-python scikit-learn numpy pandas Pillow
2. Launch the App
Run the Streamlit application locally:

bash
Copy
Edit
streamlit run app.py
The app will open in your browser at http://localhost:8501.

🧠 How It Works
🖼️ Step 1: Feature Extraction
Uses a pretrained model (e.g., ResNet50 or DenseNet201) from Keras.

Removes the final classification layer to get embeddings from the penultimate layer.

Converts all images into 1D feature vectors.

🔍 Step 2: Similarity Computation
Calculates cosine similarity between the uploaded image and dataset embeddings.

Returns top-N most similar images from the dataset.

🌐 Step 3: Web Interface
Built using Streamlit

User uploads a fashion image

The app displays the top visually similar items

📸 Sample Output
<img width="680" alt="Demo" src="https://github.com/user-attachments/assets/b6677501-6d53-49da-b157-18dc62af5aa4" />
Example Caption:
“Here are the top 5 visually similar fashion items for your input.”

🔮 Potential Improvements
Use FAISS or Annoy for faster similarity search on large datasets

Add multi-modal filtering (e.g., by color, price, brand)

Train a custom embedding model with contrastive or triplet loss

Integrate user feedback for personalization

🧾 License
This project is licensed under the MIT License — feel free to use, modify, and distribute.

🙌 Acknowledgements
Flickr-Fashion Dataset

Streamlit

Keras Applications

Pretrained CNNs for feature extraction


## Output :

<img width="1474" height="1009" alt="Image" src="https://github.com/user-attachments/assets/33cf94d3-edae-4ad8-825d-528270a01706" />


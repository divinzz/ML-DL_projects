# 👗 Fashion Recommendation System

The Fashion Recommendation System is a content-based image retrieval (CBIR) application that recommends visually similar fashion items based on a reference image. It leverages deep learning for image feature extraction and computes similarity between images to find the best matches from a fashion dataset.

This project is ideal for use cases such as:

- 🛒 Online shopping experiences  
- 🧍‍♀️ Virtual styling assistants  
- 🧳 Personal wardrobe management tools

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

## 🧠 How It Works

### 🖼️ Step 1: Feature Extraction

- Uses a pretrained model (e.g., ResNet50 or DenseNet201) from Keras
- Removes the final classification layer to get embeddings from the penultimate layer
- Converts all images into 1D feature vectors

### 🔍 Step 2: Similarity Computation

- Calculates **cosine similarity** between the uploaded image and dataset embeddings
- Returns top-N most similar images from the dataset

### 🌐 Step 3: Web Interface

- Built using **Streamlit**
- User uploads a fashion image
- The app displays the top visually similar items

---

## 📸 Sample Output

Here’s an example of how the app looks when a user uploads a fashion item:

<img width="680" alt="Fashion Recommendation Demo" src="https://your-image-link-here" />

**Recommended Items:**

- Similar shirts, dresses, or styles from the dataset  
- Based on visual features (texture, color, pattern)  
- Displayed in a scrollable or grid layout

---

## 🧪 Output Example

<img width="1474" height="1009" alt="Output Screenshot" src="https://github.com/user-attachments/assets/33cf94d3-edae-4ad8-825d-528270a01706" />

---

## 🔮 Potential Improvements

- 🧠 Use FAISS or Annoy for faster similarity search on large datasets  
- 🎨 Add multi-modal filtering (e.g., by color, price, brand)  
- 🔬 Train a custom embedding model with contrastive or triplet loss  
- 🧍‍♂️ Integrate user feedback for personalization  

---

## 🧾 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## 🙌 Acknowledgements

- [Flickr-Fashion Dataset](https://github.com/xthan/flickr-style)  
- [Streamlit](https://streamlit.io/)  
- [Keras Applications](https://keras.io/api/applications/)  
- Pretrained CNN models for feature extraction  

# 🌿 Plant Disease Classifier

This project is a deep learning-powered web app that classifies plant leaf images into different diseases (or healthy) using a trained TensorFlow model. It also provides a confidence score and a detailed description of the disease.

---

## 📸 Demo

Upload a plant leaf image and the app will:

- 🧠 Predict the disease (e.g., `Tomato___Late_blight`)
- 📊 Show prediction confidence (e.g., 97.5%)
- 📖 Display a helpful disease description

---

## 🚀 How to Run the Project

1. **Clone the repo**
```bash
git clone https://github.com/divinzz/ML-DL_projects.git
cd ML-DL_projects/Plant-Disease-Prediction
Install the dependencies

bash
Copy
Edit
pip install streamlit tensorflow pillow numpy
Make sure you have these files in the folder:

Untitled6.ipynb (main app code)

plant_disease_model.h5 (the trained model)

class indices.json (label mapping)

Run the app

bash
Copy
Edit
streamlit run Untitled6.ipynb
🧠 Model Info
Built with TensorFlow/Keras

Input images resized to 224x224

Predicts 38+ disease classes across multiple crops (tomato, apple, corn, etc.)

📂 Folder Structure
kotlin
Copy
Edit
Plant-Disease-Prediction/
├── Untitled6.ipynb
├── plant_disease_model.h5
├── class indices.json
└── README.md
🧪 Libraries Used
TensorFlow

Streamlit

NumPy

PIL (Python Imaging Library)

JSON

![Image](https://github.com/user-attachments/assets/c6d6f57a-243a-436b-b096-d3598fbdc943)

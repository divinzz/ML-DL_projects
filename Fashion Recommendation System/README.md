# 👗 Fashion Recommendation System

A machine learning-based project that suggests fashion styles and items to users based on their preferences using computer vision and classification techniques.

## 📌 Overview

This project aims to build a **Fashion Recommendation System** that can classify clothing images and recommend suitable fashion styles (e.g., casual, formal, ethnic). It combines image preprocessing, convolutional neural networks (CNN), and deep learning techniques to achieve accurate fashion classification and personalized suggestions.

---

## 🧠 Project Workflow

1. **Data Collection**  
   - Used a structured dataset of fashion images with labeled categories like _Casual_, _Formal_, _Ethnic_, etc.
   - Images organized in folders by category.

2. **Image Preprocessing**  
   - Converted images to grayscale.
   - Resized to uniform size (e.g., 100x100).
   - Normalized pixel values.
   - Stored processed image arrays (`data.npy`) and labels (`target.npy`) for efficient model training.

3. **Model Building**  
   - Created a CNN using Keras:
     - Convolutional layers
     - Max Pooling
     - Dropout to prevent overfitting
     - Dense layer with softmax activation for multi-class classification
   - Loss Function: `categorical_crossentropy`
   - Optimizer: `adam`

4. **Training**  
   - Split dataset into training and validation sets.
   - Trained over multiple epochs with `ModelCheckpoint` to save best models.

5. **Evaluation**  
   - Plotted training and validation loss and accuracy.
   - Evaluated the model using accuracy score and confusion matrix.

6. **Real-time Fashion Detection**  
   - Used OpenCV and Haar Cascades for real-time detection.
   - Integrated model predictions with live webcam feed.
   - Classifies whether fashion is _Casual_ or _Formal_ based on input.

---


## 📊 Key Libraries Used

- `TensorFlow / Keras` – for model creation and training
- `OpenCV` – for image handling and live webcam prediction
- `NumPy` – for array manipulation
- `Matplotlib` – for training performance visualization
- `os` – for directory handling
- `LabelEncoder` – for encoding target classes

---

## 📌 Model Summary

| Layer | Type           | Parameters |
|-------|----------------|------------|
| 1     | Conv2D         | 200 filters, (3x3) |
| 2     | MaxPooling2D   | (2x2)       |
| 3     | Flatten        | -           |
| 4     | Dropout        | 0.5         |
| 5     | Dense (50)     | relu        |
| 6     | Output (Softmax)| classes=3  |

---

💡 Features
Recommends fashion styles using deep learning

Real-time prediction using webcam

Simple, modular codebase

Extendable to more categories or user personalization

✅ Future Improvements
Add support for more fashion categories (e.g., Streetwear, Party)

Improve accuracy with larger datasets

Build a web app using Streamlit or Flask

Integrate user input for customized recommendations

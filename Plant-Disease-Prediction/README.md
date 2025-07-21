# 🌿 Plant Disease Classifier

This project uses a deep learning model to classify plant diseases from leaf images. Built with **TensorFlow** and deployed using **Streamlit**, the app predicts plant health status and provides detailed descriptions for each identified disease.

---

## 🔬 Project Overview

- Uses a **trained CNN model** (`plant_disease_model.h5`) to detect plant diseases.
- Accepts images of leaves and predicts the **disease class** with a **confidence score**.
- Displays a detailed description of the predicted disease based on a JSON mapping file.
- User interface built with **Streamlit** for easy interaction.

---

## 📋 Classes Covered

Supports 38+ plant disease categories, including:

- Apple (e.g., Apple Scab, Black Rot)
- Tomato (e.g., Early Blight, Mosaic Virus)
- Corn (e.g., Common Rust, Leaf Blight)
- Grape, Potato, Peach, Bell Pepper, and more...

Also includes **healthy** classes for all plant types.

---

## 🧠 Tech Stack

- **Python**
- **TensorFlow / Keras**
- **Streamlit**
- **PIL, NumPy**
- **JSON for metadata**

---

## 🎯 Output

When a leaf image is uploaded:
- ✅ **Prediction** (e.g., "Tomato___Late_blight")
- 📈 **Confidence Score** (e.g., 96.7%)
- 📖 **Disease Description** (e.g., symptoms, impact, severity)

---

## 📊 Results Summary

- The model achieved a **validation accuracy of ~98%** and **test accuracy above 96%**, showing high reliability across various plant types and diseases.
- The classification is robust across multiple classes, including visually similar disease types.
- Minimal overfitting due to proper regularization and data augmentation.
- Inference time per image is low (~1s), making the app suitable for real-time use.

---

## 📌 Conclusion

This project demonstrates an effective application of deep learning in agriculture by helping identify plant diseases quickly and accurately. With a simple interface and strong model performance, it offers a practical tool for farmers, researchers, and agricultural experts to diagnose plant health based on leaf images.

It also lays the foundation for further enhancement through:
- More plant/disease classes
- Mobile deployment
- Real-time detection using camera input

---

## 🧾 Files

- `Untitled6.ipynb` – Main app code (Streamlit + prediction logic)
- `plant_disease_model.h5` – Trained classification model
- `class indices.json` – Maps predicted class index to name
- `README.md` – Project documentation


# OUTPUT OF THE TASK

![Image](https://github.com/user-attachments/assets/c6d6f57a-243a-436b-b096-d3598fbdc943)

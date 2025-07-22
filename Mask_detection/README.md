# 😷 Face Mask Detection using CNN

This project uses **Convolutional Neural Networks (CNN)** to detect whether a person is wearing a face mask or not — with **real-time video detection** using a webcam.

## 📁 Project Structure

📦 Face Mask Detection
┣ 📂 Mask data/ ← Folder containing 'with mask' and 'without mask' images
┣ 📜 data.npy ← Preprocessed image data
┣ 📜 target.npy ← Labels (0 for no mask, 1 for mask)
┣ 📜 facedetector.h5 ← Trained Keras model
┣ 📜 main.py ← Main Python file (training + detection)
┗ 📜 README.md ← Project overview

yaml
Copy
Edit

---

## 🧠 Model Summary

- **Model Architecture**: CNN with Conv2D, MaxPooling2D, Dropout, and Dense layers
- **Activation Functions**: ReLU and Softmax
- **Loss Function**: Categorical Crossentropy
- **Optimizer**: Adam
- **Accuracy**: Tracked via training & validation metrics

---

## 🏗️ Features

- Image preprocessing (grayscale, resizing, normalization)
- One-hot encoding for target labels
- Train-test split using `train_test_split`
- Live face detection using Haar Cascades
- Real-time classification with color-coded bounding boxes:
  - 🟥 Red: Without Mask
  - 🟩 Green: With Mask

---

## 🖥️ Libraries Used

- `opencv-python` (`cv2`)
- `numpy`
- `matplotlib`
- `keras` (`Sequential`, `Conv2D`, etc.)
- `sklearn` (`train_test_split`)

---

## 🔬 Training

- 20 epochs with validation split
- Model saved as `facedetector.h5` using `ModelCheckpoint`
- Loss and accuracy graphs plotted for evaluation

---

## 🎥 Real-Time Detection

- Uses your webcam feed to:
  - Detect faces using Haar cascades
  - Classify as masked or unmasked
  - Show label and bounding box live

> Press `Esc` to exit real-time detection window.

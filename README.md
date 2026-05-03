#  FaceMorphix

### Real-Time Emotion Detection → Anime Avatar 🎌

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![OpenCV](https://img.shields.io/badge/OpenCV-ComputerVision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-FaceMesh-orange)

---

##  Overview

FaceMorphix is an AI-powered application that transforms your real-time facial expressions into anime-style avatars.

It detects emotions using facial landmarks and instantly maps them to animated characters, creating an engaging and interactive visual experience.

---

## 🚀 Features

*  Real-time webcam-based face tracking
*  Emotion Detection (Happy, Sad, Angry, Neutral)
*  Anime Avatar Mapping
*  Fast & optimized processing
*  Clean UI with Streamlit

---

## Tech Stack

| Technology | Use                     |
| ---------- | ----------------------- |
| Python     | Core language           |
| OpenCV     | Image processing        |
| MediaPipe  | Face landmark detection |
| Streamlit  | UI & deployment         |
| NumPy      | Numerical operations    |

---

##  Project Structure

```
FaceMorphix/
│── app.py
│── requirements.txt
│── assets/
│    ├── happy.png
│    ├── sad.png
│    ├── angry.png
│    └── neutral.png
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repo

```bash
git clone https://github.com/shaily27/FaceMorphix.git
cd FaceMorphix
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run App

```bash
streamlit run app.py
```

---

## 🌐 Deployment

This app can be deployed using:

* Streamlit Cloud
* Hugging Face Spaces

⚠️ Note: Webcam may not work directly on cloud due to browser restrictions.

---

## 💡 Working Logic

* Face landmarks extracted via MediaPipe
* Ratios (mouth, eyes, face width) calculated
* Emotion classified using rule-based logic
* Corresponding anime avatar displayed

---

##  Future Enhancements

*  Deep learning-based emotion detection
*  Real-time WebRTC camera
*  Custom anime avatar generator
*  Emotion analytics dashboard

---

##  Contributing

Pull requests are welcome! Feel free to fork and improve.

---

##  Author

**Shaily Gupta**
🔗 https://github.com/shaily27

---

##  Support

If you like this project, give it a ⭐ on GitHub!

---


# 🌱 EcoAirSense - AI Pollution Prediction System

EcoAirSense is an AI-powered web application to predict **Air, Water, and Noise pollution levels**. It also visualizes historical data on **interactive charts** and displays regional pollution on a **Google Map**.

Designed for environmental monitoring, hackathons, and real-world deployment.

---

## 🌟 Features
- 🌬️ Predict **Air Pollution** (PM2.5, PM10, NO₂)  
- 💧 Predict **Water Potability** (pH, Hardness, Solids, etc.)  
- 🔊 Predict **Noise Levels** from uploaded audio files  
- 📊 View **historical pollution trends** on interactive Chart.js graphs  
- 🗺️ See **regional pollution data** on Google Maps  
- 🖥️ Modern, mobile-friendly, eco-themed UI  

---

## 🛠 Tech Stack

| Frontend          | Backend       | Machine Learning         |
|--------------------|---------------|---------------------------|
| HTML, CSS, JS      | Flask (Python)| Random Forest (sklearn)   |
| Bootstrap 5        | Flask REST API| Librosa (audio features)  |
| Chart.js           | Flask Blueprints| pandas, numpy, pickle |

---

## 🚀 Setup Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Chetan-Singh04/Pollution-Prediction-System
cd Pollution-Prediction-System
````

### 2️⃣ Create and Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Train the ML Models (Optional)

```bash
cd backend/utils
python train_air_model.ipynb
python train_water_model.ipynb
python train_noise_model.ipynb
```

✅ Pre-trained models are already included in `/backend/models/`.

---

### 5️⃣ Run the App Locally

```bash
cd ../../
python backend/app.py
```

🌐 Open your browser and visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)


## 📸 Screenshots

### 🌬️ Home Page
![Home page](frontend\static\images\Home.png)

### 🌬️ Air Prediction
![Air Prediction](frontend\static\images\air-prediction.png)

### 💧 Water Prediction
![Water Prediction](frontend\static\images\water-prediction.png)

### 🔊 Noise Prediction
![Noise Prediction](frontend\static\images\noise-prediction.png)

### 📊 Charts Page
![Charts](frontend\static\images\charts.png)

### 🗺️ Map Page
![Map](frontend\static\images\map.png)

---

## 🙌 Acknowledgements

* Bootstrap 5 for UI components
* Chart.js for interactive graphs
* Google Maps API for mapping pollution data
* Librosa for audio feature extraction

---

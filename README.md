# 🌾 CropWise | Machine Learning-Based Crop Recommendation System

A Flask-based web application that recommends the most suitable crop based on soil nutrients and environmental conditions using a Random Forest Machine Learning model.

---

# 🚀 Project Overview

CropWise is a machine learning-powered decision support system developed to assist farmers in selecting the most suitable crop for cultivation. The application analyzes soil nutrients and environmental conditions to provide accurate crop recommendations, helping improve agricultural productivity and reduce crop failure.

The system combines a trained Random Forest classifier with a user-friendly Flask web application, enabling users to receive real-time crop recommendations through an intuitive interface.

---

# 🎯 Objectives

* Predict the most suitable crop based on soil and climate parameters.
* Provide farmers with data-driven agricultural recommendations.
* Maintain prediction history for registered users.
* Implement secure authentication and role-based access.
* Build an easy-to-use web application for precision agriculture.

---

# ✨ Features

### 🌱 Crop Recommendation

* Predicts the best crop using machine learning.
* Real-time prediction based on user inputs.

### 👤 User Authentication

* User Registration
* Secure Login
* Password hashing using Flask-Bcrypt
* Session management with Flask-Login

### 📊 Dashboard

* View previous crop predictions
* Personalized user dashboard

### 👨‍💼 Admin Panel

* Manage registered users
* View prediction history
* Monitor system activity

### 🧠 Machine Learning

* Random Forest Classifier
* Trained on agricultural datasets
* High prediction accuracy
* Handles nonlinear relationships effectively

---

# 📌 Input Parameters

The prediction model uses:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH Value
* Rainfall

---

# 🏗️ System Architecture

```text
User
   │
   ▼
Flask Web Application
   │
   ├── Authentication
   ├── Dashboard
   ├── Prediction Module
   │
   ▼
Random Forest Model
   │
   ▼
Crop Recommendation
   │
   ▼
SQLite Database
```

---

# 🛠️ Tech Stack

### Programming Language

* Python

### Framework

* Flask

### Machine Learning

* Scikit-learn
* Random Forest Classifier

### Database

* SQLite

### ORM

* SQLAlchemy

### Authentication

* Flask-Login
* Flask-Bcrypt

### Frontend

* HTML
* CSS
* Bootstrap
* Jinja2

---

# 📂 Project Structure

```text
CropWise/
│
├── app.py
├── train_model.py
├── crop_recommendation_model.pkl
├── dataset.csv
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── admin_dashboard.html
│
├── static/
│   ├── css/
│   └── crops/
│
└── instance/
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/CropWise_ML_Crop_Recommendation_System.git

cd CropWise_ML_Crop_Recommendation_System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

# 📷 Screenshots

Add screenshots here.

### 🏠 Home Page

<img width="1035" height="582" alt="image" src="https://github.com/user-attachments/assets/43ed6580-17af-4c46-9a5f-688594d6f939" />

### 🔐 Registration Page

<img width="1050" height="513" alt="image" src="https://github.com/user-attachments/assets/04b265c3-84b5-4954-94c2-a524cd535700" />

### 🔐 Login Page

<img width="1038" height="577" alt="image" src="https://github.com/user-attachments/assets/13db6094-eedf-46ea-839e-d214516de4ee" />

### 🌱 Crop Prediction

<img width="1037" height="502" alt="image" src="https://github.com/user-attachments/assets/c1c4edde-1165-4901-8e5b-5fe921b901e9" />

### 📊 Dashboard

<img width="1038" height="493" alt="image" src="https://github.com/user-attachments/assets/60850858-db4b-4765-ae45-763a233491bb" />

### 👨‍💼 Admin Dashboard

<img width="1035" height="580" alt="image" src="https://github.com/user-attachments/assets/e6155fd0-fe7e-4352-9420-9a0ba40b07c9" />

---

# 🧠 Machine Learning Model

**Algorithm Used**

* Random Forest Classifier

**Why Random Forest?**

* High prediction accuracy
* Reduces overfitting through ensemble learning
* Handles nonlinear relationships effectively
* Performs well on agricultural datasets
* Requires minimal feature engineering

---

# 📚 Dataset

The model was trained using an agricultural dataset containing:

* Soil nutrients
* Environmental parameters
* Crop labels

Features:

* Nitrogen
* Phosphorus
* Potassium
* Temperature
* Humidity
* pH
* Rainfall

Target:

* Recommended Crop

---

# 🔑 Key Learnings

* Machine Learning with Scikit-learn
* Random Forest Classification
* Flask Web Development
* User Authentication
* SQLAlchemy ORM
* SQLite Database
* Model Deployment
* Responsive Web Design

---

# 🚀 Future Enhancements

* Weather API Integration
* Fertilizer Recommendation
* Disease Prediction
* Crop Yield Prediction
* Multi-language Support
* Mobile Application
* Cloud Deployment

---

# 👨‍💻 Author

**Subramanian T**

MCA Graduate | Python Developer | Machine Learning Enthusiast

**LinkedIn:** [https://www.linkedin.com/in/subramanian-t](https://www.linkedin.com/in/subramanian-t-6b7b92255/)

**GitHub:** https://github.com/Subramanian2002

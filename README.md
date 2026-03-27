# 🏡 AI House Price Predictor

A full-stack machine learning web application that predicts property valuations based on key real estate features. This project demonstrates the end-to-end deployment of a Machine Learning model, from data processing and training to serving predictions via a RESTful API with a modern web interface.

## 🚀 Features
* **Machine Learning Engine:** Utilizes a Multiple Linear Regression model trained on real-world housing data.
* **RESTful Backend:** Built with Flask to bridge the Python ML model and the web client.
* **Modern UI/UX:** A responsive, aesthetic frontend built with Vanilla JS, HTML, and CSS Grid.
* **Instant Valuations:** Provides real-time price predictions in Indian Rupees (₹) based on user input.

## 🛠️ Tech Stack
* **Language:** Python 3.x, JavaScript, HTML5, CSS3
* **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib
* **Backend Framework:** Flask

## 📁 Project Structure
```text
house-price-prediction-ai/
│
├── house_price_regression_dataset.csv   # Training data
├── train_model.py                       # Script to train and export the model
├── house_price_model.pkl                # Serialized ML model
├── app.py                               # Flask application and API routes
├── .gitignore                           # Git ignore rules
├── README.md                            # Project documentation
│
└── templates/                           
    └── index.html                       # Frontend web interface
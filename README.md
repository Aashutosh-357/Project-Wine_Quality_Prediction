# 🍷 Wine Quality Prediction Web App: Tuned Random Forest Classifier

## Project Overview

This project implements a robust **Tuned Random Forest Classifier** to predict the quality of White Wine. The focus was on optimizing model performance through rigorous hyperparameter tuning, which resulted in a **6% improvement** over the baseline model.

The final model, achieving **~81% accuracy**, is deployed within a lightweight Flask web application. Users can input various physicochemical properties (like alcohol content, density, and pH) and instantly receive a prediction of whether the wine is "Good" or "Bad."

The application is deployed end-to-end on Render, demonstrating full-stack ML deployment skills.

---

## Key Features

* **Optimized ML Model:** Utilizes a **Random Forest Classifier** where performance was boosted by **6%** via hyperparameter tuning and cross-validation, achieving a final accuracy of **~81%**.
* **Data Analysis Focus:** Trained on the UCI Wine Quality Dataset, focusing on five critical features (volatile acidity, chlorides, density, pH, and alcohol) identified through exploratory data analysis.
* **Web Interface:** A simple, responsive user-friendly Flask application with an HTML form (`index.html`) for real-time input and inference.
* **Production Deployment:** Fully containerized and deployed on Render (PaaS) for public access and Continuous Deployment practice.

---

## 🛠️ Technical Stack

| Category | Tools & Libraries |
| :--- | :--- |
| **Backend/Web Framework** | **Python**, **Flask**, Gunicorn |
| **Machine Learning** | **Scikit-learn** (`RandomForestClassifier`, `StandardScaler`), **NumPy** |
| **Data Handling** | **Pandas**, NumPy |
| **Model Persistence** | **Joblib** (`.pkl` files) |
| **Deployment & CI/CD** | Git, GitHub, **Render** (PaaS) |

---

## 📂 Project Structure

The repository contains the following critical files:
Project-Wine_Quality_Prediction/
├── app.py                  # Main Flask application, loads model, handles routes, and prediction logic.
├── index.html              # Frontend HTML for the user input form.
├── requirements.txt        # Lists all necessary Python dependencies for the server.
├── Procfile                # Specifies the startup command for the web server (Gunicorn).
├── runtime.txt             # Specifies the required Python version (e.g., python-3.12.3).
├── Tuned_RandomForest.pkl  # The serialized Random Forest model (Tuned_RandomForest.pkl).
└── StandardScaler.pkl      # The fitted Standard Scaler object.

---

## 📊 Model Performance: Quantified Impact

The final Tuned Random Forest Classifier was rigorously evaluated on the held-out test set, demonstrating the value of hyperparameter optimization.

| Metric | Baseline Score | **Final Tuned Score** | Notes |
| :--- | :--- | :--- | :--- |
| **Accuracy** | ~75% (approx.) | $\mathbf{\approx 81\%}$ | **6% performance improvement** achieved through tuning. |
| F1-Score (Weighted) | N/A | $\mathbf{\approx 82\%}$ | High F1 score confirms robust performance on both Good and Bad classes. |

---

## 🚀 How to Run Locally

You can run this application on your local machine by following these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/ashutosh12222119/Project-Wine_Quality_Prediction.git](https://github.com/ashutosh12222119/Project-Wine_Quality_Prediction.git)
    cd Project-Wine_Quality_Prediction
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask Application:**
    ```bash
    python app.py
    ```

5.  **Access the App:** Open your web browser and navigate to `http://127.0.0.1:5000/`.

---

This application is set up for Continuous Deployment via GitHub to Render.

Deployment Platform: Render

**Live Link**: https://wine-quality-predictor-nkle.onrender.com/ 🚀

---

## 🧑‍💻 About the Developer

This project was developed by Ashutosh Kumar Rai as part of my ongoing **#Challenge 92** commitment to building Machine Learning systems.

* **LinkedIn:** [linkedin.com/in/ashutoshkr135/](https://linkedin.com/in/ashutoshkr135/)
* **GitHub:** [github.com/Aashutosh-357/](https://github.com/Aashutosh-357/)

---

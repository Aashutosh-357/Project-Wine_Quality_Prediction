import pandas as pd, numpy as np
import joblib
from flask import Flask, request, jsonify, render_template

# Initializing the Flask App
app = Flask(__name__)

# Load the Trained Model and the Fitted Scaler
try:
    model = joblib.load('Tuned_RandomForest.pkl')
    scaler = joblib.load('StandardScaler.pkl')
    print("Model and Scaler Loaded Successfully!!! ")
except FileNotFoundError:
    print("ERROR: Model or Scaler not found! ")
    model, scaler = None, None

# Define the features columns exact order as Trained
FEATURE_COLUMNS = [ 'volatile acidity', 'chlorides', 'density', 'pH', 'alcohol' ] 

# Map binary output to readable quality
QUALITY_MAP = {0: 'Bad(Quality Score <= 6)', 1: 'Good(Quality Score >= 7)'}

@app.route('/')
def home():
    """Render the inpute form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle the Prediction Request"""
    if model is None or scaler is None:
        return jsonify({'error': 'Model or Scaler not loaded on Server!'})
    
    # Get data from form.
    data = request.form.to_dict()

    # Convert form data to a list of floats in the correct order
    try:
        features = [float(data[col]) for col in FEATURE_COLUMNS]
    except KeyError as e:
        return jsonify({'error': f'Missing feature: {e}'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid input type. All the values must be numbers.'}), 400
    
    # Convert features list to a numpy array, then reshape for the scaler
    final_features = np.array(features).reshape(1, -1)

    # Apply Scaling
    scaled_features = scaler.transform(final_features)

    # Prediction
    prediction_array = model.predict(scaled_features)
    prediction_label = int(prediction_array[0])

    # Get the readable result
    output = QUALITY_MAP.get(prediction_label, 'Unknown Result')

    # Pass the result back to the HTML page
    return render_template('index.html', prediction_text=f"Predicted Wine Quality: {output}")

if __name__ == '__main__':
    app.run(debug=True)
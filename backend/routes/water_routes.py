from flask import Blueprint, request, jsonify
import pickle
import numpy as np
import os

# Load model and scaler
model_path = os.path.join(os.path.dirname(__file__), '../models/water_model.pkl')
scaler_path = os.path.join(os.path.dirname(__file__), '../models/water_scaler.pkl')
with open(model_path, 'rb') as f:
    water_model = pickle.load(f)
with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)

water_blueprint = Blueprint('water', __name__)

@water_blueprint.route('/predict', methods=['POST'])
def predict_water():
    data = request.json
    features = np.array([[
        data['pH'], data['Hardness'], data['Solids'], data['Chloramines'],
        data['Sulfate'], data['Conductivity'], data['Organic_carbon'],
        data['Trihalomethanes'], data['Turbidity']
    ]])
    features_scaled = scaler.transform(features)
    prediction = water_model.predict(features_scaled)[0]

    result = "Safe to Drink" if prediction == 1 else "Not Safe to Drink"
    return jsonify({"prediction": result})

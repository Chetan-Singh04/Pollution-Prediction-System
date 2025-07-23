from flask import Blueprint, request, jsonify
import pickle
import numpy as np
import os

# Load trained model
model_path = os.path.join(os.path.dirname(__file__), '../models/air_model.pkl')
with open(model_path, 'rb') as f:
    air_model = pickle.load(f)

air_blueprint = Blueprint('air', __name__)

@air_blueprint.route('/predict', methods=['POST'])
def predict_air():
    data = request.json
    pm25 = float(data['pm25'])
    pm10 = float(data['pm10'])
    no2 = float(data['no2'])

    prediction = air_model.predict([[pm25, pm10, no2]])[0]
    result = "Good Air Quality" if prediction == 0 else "Poor Air Quality"

    return jsonify({"prediction": result})

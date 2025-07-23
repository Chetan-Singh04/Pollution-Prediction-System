from flask import Blueprint, request, jsonify
import pickle
import librosa
import numpy as np
import os

# Load model
model_path = os.path.join(os.path.dirname(__file__), '../models/noise_model.pkl')
with open(model_path, 'rb') as f:
    noise_model = pickle.load(f)

noise_blueprint = Blueprint('noise', __name__)

@noise_blueprint.route('/predict', methods=['POST'])
def predict_noise():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file uploaded'}), 400
    
    audio_file = request.files['audio']
    temp_path = os.path.join(os.path.dirname(__file__), '../data/temp_audio.wav')
    audio_file.save(temp_path)

    try:
        # Extract features
        y_audio, sr = librosa.load(temp_path, duration=5.0)
        mfccs = librosa.feature.mfcc(y=y_audio, sr=sr, n_mfcc=40)
        mfccs_scaled = np.mean(mfccs.T, axis=0).reshape(1, -1)

        # Predict
        prediction = noise_model.predict(mfccs_scaled)[0]
        result = "Safe Noise Level" if prediction == 0 else "Unsafe Noise Level"

        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": f"Failed to process audio file: {str(e)}"}), 500
    finally:
        # Clean up temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)

from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

# Load the trained model
model_path = 'model.pkl'  # Update this path if different
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Bike Sharing Demand Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse the input data
        input_data = request.get_json()

        # Define the feature columns in the correct order
        feature_order = [
            'holiday', 'workingday', 'atemp', 'humidity', 'windspeed',
            'hour', 'season__1', 'season__2', 'season__3', 'season__4',
            'weather__1', 'weather__2', 'weather__3', 'weather__4'
        ]

        # Initialize all features to zero
        features = {col: 0 for col in feature_order}

        # Populate features from input data
        for key in input_data:
            if key in features:
                features[key] = input_data[key]

        # Convert to numpy array in the correct order
        features_array = np.array([features[col] for col in feature_order]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features_array)
        prediction =  np.power(10, prediction)

        # Return prediction
        return jsonify({"predicted_count": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)

# app.py
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the newly trained model
model = joblib.load('house_price_model.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract the 7 features in the exact order the model expects them
        features = [
            float(data['sqft']),
            float(data['bedrooms']),
            float(data['bathrooms']),
            float(data['year']),
            float(data['lot_size']),
            float(data['garage']),
            float(data['quality'])
        ]

        # Reshape for a single prediction
        final_features = np.array(features).reshape(1, -1)

        # Make the prediction
        prediction = model.predict(final_features)

        # Return the formatted prediction
      
        return jsonify({'predicted_price': f"₹{prediction[0]:,.2f}"})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(debug=True)
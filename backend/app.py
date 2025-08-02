from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pickle
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define paths for model and scaler
model_path = os.path.join(os.path.dirname(__file__), 'salary_model.pkl')
scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')

# Check if model and scaler files exist
if not os.path.exists(model_path) or not os.path.exists(scaler_path):
    # Sample data for training the model
    # In a real application, you would load this from a database or CSV file
    sample_data = {
        'experience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'education_level': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],  # 1: High School, 2: Bachelor's, 3: Master's, 4: PhD, 5: Professional
        'role': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],  # 1: Junior, 2: Mid-level, 3: Senior, 4: Lead, 5: Manager
        'industry': [1, 2, 1, 2, 3, 4, 3, 4, 5, 5],  # 1: Tech, 2: Finance, 3: Healthcare, 4: Education, 5: Other
        'salary': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000]
    }

    # Convert to DataFrame
    df = pd.DataFrame(sample_data)

    # Features and target
    X = df[['experience', 'education_level', 'role', 'industry']]
    y = df['salary']

    # Initialize and train the model
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = LinearRegression()
    model.fit(X_scaled, y)

    # Save the model and scaler
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    with open(scaler_path, 'wb') as f:
        pickle.dump(scaler, f)

# Load the model and scaler
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)
except Exception as e:
    print(f"Error loading model or scaler: {str(e)}")
    # If there's an error loading, recreate them
    # This is a fallback mechanism
    sample_data = {
        'experience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'education_level': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
        'role': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
        'industry': [1, 2, 1, 2, 3, 4, 3, 4, 5, 5],
        'salary': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000]
    }
    df = pd.DataFrame(sample_data)
    X = df[['experience', 'education_level', 'role', 'industry']]
    y = df['salary']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = LinearRegression()
    model.fit(X_scaled, y)

    # Save the model and scaler again
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    with open(scaler_path, 'wb') as f:
        pickle.dump(scaler, f)

@app.route('/api/predict', methods=['POST'])
def predict_salary():
    try:
        # Check if request contains JSON data
        if not request.is_json:
            return jsonify({
                'error': 'Request must contain JSON data',
                'status': 'error'
            }), 400

        data = request.json
        if data is None:
            return jsonify({
                'error': 'Invalid JSON data',
                'status': 'error'
            }), 400

        # Extract features with validation
        try:
            experience = float(data.get('experience', 0))
        except (ValueError, TypeError):
            return jsonify({
                'error': 'Experience must be a valid number',
                'status': 'error'
            }), 400

        try:
            education_level = int(data.get('education_level', 1))
            role = int(data.get('role', 1))
            industry = int(data.get('industry', 1))
        except (ValueError, TypeError):
            return jsonify({
                'error': 'Education level, role, and industry must be valid integers',
                'status': 'error'
            }), 400

        # Create feature array
        features = np.array([[experience, education_level, role, industry]])

        # Scale features
        try:
            features_scaled = scaler.transform(features)
        except Exception as e:
            print(f"Error scaling features: {str(e)}")
            return jsonify({
                'error': f'Error scaling features: {str(e)}',
                'status': 'error'
            }), 500

        # Make prediction
        try:
            prediction = model.predict(features_scaled)[0]
        except Exception as e:
            print(f"Error making prediction: {str(e)}")
            return jsonify({
                'error': f'Error making prediction: {str(e)}',
                'status': 'error'
            }), 500

        return jsonify({
            'predicted_salary': round(prediction, 2),
            'status': 'success'
        })

    except Exception as e:
        print(f"Unexpected error in predict_salary: {str(e)}")
        return jsonify({
            'error': f'An unexpected error occurred: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

"""
EduAI - Student Performance Predictor Web Application
Flask REST API and Web Interface
"""

from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np
from pathlib import Path
import traceback

app = Flask(__name__, template_folder='templates', static_folder=None)

# Load model and preprocessing objects
models_dir = Path('models')
try:
    model = joblib.load(models_dir / 'gradient_boosting_model.pkl')
    scaler = joblib.load(models_dir / 'scaler.pkl')
    feature_names = joblib.load(models_dir / 'feature_names.pkl')
    metadata = joblib.load(models_dir / 'model_metadata.pkl')
    print("✓ Models loaded successfully")
except Exception as e:
    print(f"✗ Error loading models: {e}")
    model = scaler = feature_names = metadata = None

# Grade mapping
GRADE_MAPPING = {
    0: 'A (Excellent)',
    1: 'B (Good)',
    2: 'C (Average)',
    3: 'D (Below Average)',
    4: 'F (Failing)'
}

ADVICE = {
    0: 'Excellent work! Keep maintaining your high standards.',
    1: 'Good performance! Continue studying and stay focused.',
    2: 'Average performance. Consider seeking tutoring support.',
    3: 'Below average. Increase study time and seek help.',
    4: 'Failing grade. Urgent intervention needed. Talk to counselor.'
}

@app.route('/')
def home():
    """Render the main web page"""
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    """
    API endpoint for making predictions
    Expects JSON with student features
    """
    try:
        # Check if models are loaded
        if model is None or scaler is None or feature_names is None:
            return jsonify({
                'success': False,
                'error': 'Models not loaded. Please check the models directory.'
            }), 503

        # Get JSON data from request
        data = request.get_json()

        # Validate required fields
        required_fields = feature_names
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({
                'error': f'Missing required fields: {missing_fields}. Expected: {required_fields}'
            }), 400

        # Create DataFrame with input data
        df_input = pd.DataFrame([{field: data[field] for field in feature_names}])

        # Scale features
        X_scaled = scaler.transform(df_input)

        # Make prediction
        prediction_class = model.predict(X_scaled)[0]
        probabilities = model.predict_proba(X_scaled)[0]
        confidence = float(np.max(probabilities))

        # Return prediction
        response = {
            'success': True,
            'predicted_class': int(prediction_class),
            'grade': GRADE_MAPPING[int(prediction_class)],
            'confidence': round(confidence * 100, 2),
            'advice': ADVICE[int(prediction_class)],
            'probabilities': {
                GRADE_MAPPING[i]: round(float(prob) * 100, 2)
                for i, prob in enumerate(probabilities)
            }
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@app.route('/api/features', methods=['GET'])
def get_features():
    """Get list of required features for predictions"""
    if feature_names is None or metadata is None:
        return jsonify({
            'error': 'Models not loaded'
        }), 503
    return jsonify({
        'features': feature_names,
        'model_info': metadata
    })

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🎓 EduAI - Student Performance Predictor")
    print("="*60)
    print("Starting Flask server...")
    print("✓ Models loaded successfully" if model else "✗ Models failed to load")
    print(f"✓ Template folder: {app.template_folder}")
    print("✓ Server will be available at: http://127.0.0.1:5000")
    print("✓ Press Ctrl+C to stop the server")
    print("="*60 + "\n")

    app.run(debug=False, host='0.0.0.0', port=5000)

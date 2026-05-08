# EduAI - Student Performance Predictor

A machine learning web application that predicts student academic performance based on various factors including study habits, attendance, and socio-economic indicators.

## Features

- **Machine Learning Model**: Gradient Boosting Classifier trained on student performance data
- **Web Interface**: Clean, responsive HTML interface for easy predictions
- **REST API**: JSON API endpoint for programmatic access
- **Real-time Predictions**: Instant predictions with confidence scores
- **Educational Insights**: Personalized advice based on predicted performance

## Model Performance

- **Accuracy**: 99.7%
- **Precision**: 99.7%
- **Recall**: 99.7%
- **F1-Score**: 99.7%

## Installation

1. Clone or download this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Web Application

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Fill in the student information form and click "Predict Performance"

### Using the API

Send a POST request to `/api/predict` with JSON data containing all required features:

```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Hours_Studied": 5,
    "Attendance": 85,
    "Parental_Involvement": 1,
    "Access_to_Resources": 2,
    "Extracurricular_Activities": 1,
    "Sleep_Hours": 7,
    "Previous_Scores": 75,
    "Motivation_Level": 2,
    "Internet_Access": 1,
    "Tutoring_Sessions": 2,
    "Family_Income": 2,
    "Teacher_Quality": 2,
    "School_Type": 1,
    "Peer_Influence": 1,
    "Physical_Activity": 3,
    "Learning_Disabilities": 0,
    "Parental_Education_Level": 1,
    "Distance_from_Home": 1,
    "Gender": 0
  }'
```

### Required Features

The model requires the following features for prediction:
- Hours_Studied (0-10)
- Attendance (0-100)
- Parental_Involvement (0-2: Low, Medium, High)
- Access_to_Resources (0-2: Low, Medium, High)
- Extracurricular_Activities (0-1: No, Yes)
- Sleep_Hours (0-10)
- Previous_Scores (0-100)
- Motivation_Level (0-2: Low, Medium, High)
- Internet_Access (0-1: No, Yes)
- Tutoring_Sessions (0-8)
- Family_Income (0-2: Low, Medium, High)
- Teacher_Quality (0-2: Low, Medium, High)
- School_Type (0-1: Public, Private)
- Peer_Influence (0-2: Negative, Neutral, Positive)
- Physical_Activity (0-6)
- Learning_Disabilities (0-1: No, Yes)
- Parental_Education_Level (0-2: Low, Medium, High)
- Distance_from_Home (0-2: Near, Moderate, Far)
- Gender (0-1: Male, Female)

## API Response

```json
{
  "success": true,
  "predicted_class": 0,
  "grade": "A (Excellent)",
  "confidence": 99.73,
  "advice": "Excellent work! Keep maintaining your high standards.",
  "probabilities": {
    "A (Excellent)": 99.73,
    "B (Good)": 0.15,
    "C (Average)": 0.08,
    "D (Below Average)": 0.03,
    "F (Failing)": 0.01
  }
}
```

## Model Details

- **Algorithm**: XGBoost Gradient Boosting Classifier
- **Preprocessing**: StandardScaler for feature normalization
- **Class Balancing**: SMOTE for handling imbalanced classes
- **Training Data**: Student performance dataset with 10,000+ records

## Project Structure

```
├── app.py                    # Flask web application
├── requirements.txt          # Python dependencies
├── models/                   # Trained model files
│   ├── gradient_boosting_model.pkl
│   ├── scaler.pkl
│   ├── feature_names.pkl
│   └── model_metadata.pkl
├── templates/
│   └── index.html           # Web interface
├── modeltraining.ipynb      # Model development notebook
└── student.csv              # Original dataset
```

## Technologies Used

- **Backend**: Python Flask
- **Machine Learning**: XGBoost, scikit-learn
- **Data Processing**: pandas, numpy
- **Frontend**: HTML, CSS, JavaScript
- **Serialization**: joblib

## License

This project is open source and available under the MIT License.
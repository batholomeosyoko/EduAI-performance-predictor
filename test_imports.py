#!/usr/bin/env python3
"""
Test script to verify imports and model loading
"""

try:
    from flask import Flask
    print("✓ Flask imported successfully")

    import joblib
    print("✓ joblib imported successfully")

    import pandas as pd
    print("✓ pandas imported successfully")

    import numpy as np
    print("✓ numpy imported successfully")

    from sklearn.preprocessing import StandardScaler
    print("✓ scikit-learn imported successfully")

    import xgboost
    print("✓ XGBoost imported successfully")

    from imblearn.over_sampling import SMOTE
    print("✓ imbalanced-learn imported successfully")

    # Test model loading
    from pathlib import Path
    models_dir = Path('models')
    model = joblib.load(models_dir / 'gradient_boosting_model.pkl')
    print("✓ Model loaded successfully")

    scaler = joblib.load(models_dir / 'scaler.pkl')
    print("✓ Scaler loaded successfully")

    feature_names = joblib.load(models_dir / 'feature_names.pkl')
    print(f"✓ Feature names loaded: {len(feature_names)} features")

    metadata = joblib.load(models_dir / 'model_metadata.pkl')
    print("✓ Model metadata loaded successfully")

    print("\n🎉 All imports and model loading successful!")
    print("The Flask app should work correctly.")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
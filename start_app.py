#!/usr/bin/env python3
"""
Simple launcher for EduAI Flask app with error handling
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    print("Starting EduAI Student Performance Predictor...")
    print("Loading Flask application...")

    from app import app

    print("Flask app loaded successfully!")
    print("Starting server on http://localhost:5000")
    print("Press Ctrl+C to stop the server")

    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)

except ImportError as e:
    print(f"Import Error: {e}")
    print("Please make sure all requirements are installed:")
    print("pip install -r requirements.txt")

except Exception as e:
    print(f"Error starting Flask app: {e}")
    import traceback
    traceback.print_exc()

input("Press Enter to exit...")
#!/usr/bin/env python3
"""
Test script to check Flask app startup
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("Testing Flask app startup...")
print("=" * 50)

try:
    print("1. Importing Flask...")
    from flask import Flask
    print("✓ Flask imported successfully")

    print("2. Importing other dependencies...")
    import joblib
    import pandas as pd
    import numpy as np
    from pathlib import Path
    print("✓ All dependencies imported successfully")

    print("3. Loading app module...")
    from app import app
    print("✓ App module loaded successfully")

    print("4. Testing app configuration...")
    print(f"   Template folder: {app.template_folder}")
    print(f"   Static folder: {app.static_folder}")
    print("✓ App configuration looks good")

    print("\n" + "=" * 50)
    print("🎉 Flask app is ready to run!")
    print("Run: python app.py")
    print("=" * 50)

except Exception as e:
    print(f"❌ Error during startup: {e}")
    import traceback
    traceback.print_exc()
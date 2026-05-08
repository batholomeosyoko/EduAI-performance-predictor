@echo off
echo ================================================
echo 🎓 EduAI - Student Performance Predictor
echo ================================================
echo.
echo Starting Flask server...
echo.
cd /d "%~dp0"
python app.py
cecho.
echo Server stopped.
pause
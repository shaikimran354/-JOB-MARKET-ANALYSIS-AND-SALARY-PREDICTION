@echo off
echo ========================================================
echo AI Job Data Analysis and Salary Prediction System
echo ========================================================

echo Installing Requirements...
pip install -r requirements.txt

echo.
echo Running Setup (Generating Data & Folders)...
python setup.py

echo.
echo Starting Streamlit Application...
streamlit run app.py

pause

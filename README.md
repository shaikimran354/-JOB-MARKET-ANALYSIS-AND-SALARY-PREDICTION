# AI Job Data Analysis and Salary Prediction System 🚀

A complete Machine Learning application for AI/ML job market analysis with interactive salary predictions using Streamlit.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-green)

## 🎯 Features

✨ **Interactive EDA Dashboard**
- Filters by Experience Level, Company Size, Job Title
- Real-time salary visualizations
- USD/INR currency conversion
- Download processed datasets

💡 **Salary Prediction Engine**
- AI-powered salary predictions
- Input: Role, Experience, Location, Company Details
- Instant results with currency conversion

🤖 **ML Models**
- Linear Regression, Random Forest, XGBoost, Hybrid Ensemble
- Automatic best model selection
- R² Score: 0.8981 (Random Forest)

---

## 📁 Project Structure

```
├── app.py                      # Main Streamlit app
├── requirements.txt            # Dependencies
├── README.md                   # Documentation
├── run_project.bat             # Windows launch script
├── data/ds_salaries.csv        # Dataset (1000 rows)
├── models/best_model.pkl       # Trained model
└── src/
    ├── data_preprocessing.py
    ├── model_training.py
    └── prediction.py
```

---

## 🚀 Quick Start

### Option 1: Windows (Fast)
```bash
double-click run_project.bat
```

### Option 2: Manual
```bash
pip install -r requirements.txt
streamlit run app.py
```

App opens at: `http://localhost:8501`

---

## 📊 Dataset Info

- **Records:** 1,000 AI/ML job entries
- **Salary Range:** $50K - $340K USD
- **Features:** Experience Level, Job Title, Location, Company Size, Remote Ratio

---

## 🤖 Model Performance

| Model | R² Score | MAE |
|-------|----------|-----|
| **Random Forest** | **0.8981** | **$14,056** |
| Linear Regression | 0.8926 | $14,124 |
| XGBoost | 0.8804 | $15,037 |
| Hybrid | 0.8960 | $14,146 |

---

## 💱 Features

- 📊 Interactive salary visualizations
- 🔍 Data filtering and analysis
- 💰 USD/INR currency conversion
- 🤖 ML-powered predictions
- 📥 Dataset download option
- 🎨 Dark theme UI

---

## 📋 Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | Streamlit 1.40+ |
| ML Libraries | scikit-learn, XGBoost |
| Data | pandas, numpy |
| Visualization | Plotly, Seaborn |
| Python | 3.9+ |

---

## 📝 Usage

1. **EDA Tab:**
   - Filter data by criteria
   - View salary distributions
   - Download dataset

2. **Prediction Tab:**
   - Enter job details
   - Get instant salary prediction
   - View in USD or INR

---

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Model not loading | Check `models/best_model.pkl` exists |
| Data not loading | Verify `data/ds_salaries.csv` path |
| Dependencies missing | Run `pip install -r requirements.txt` |

---

** OUTPUT **


<img width="1357" height="579" alt="image" src="https://github.com/user-attachments/assets/552af628-8227-479f-a621-5748b9fb4d35" />

<img width="1340" height="559" alt="image" src="https://github.com/user-attachments/assets/3fafaec1-9c72-422a-8d4d-dc654a434420" />
<img width="1334" height="559" alt="image" src="https://github.com/user-attachments/assets/e8818c14-f9d0-412c-ad9a-17f11efa006e" />



## 🎉 Quick Links

- 📚 [Streamlit Docs](https://docs.streamlit.io)
- 🐍 [Python Docs](https://docs.python.org)
- 📊 [scikit-learn](https://scikit-learn.org)

---

**Made with ❤️ | April 2026**

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
├── data/ds_salaries.csv        # Dataset (1000 rows)
├── models/best_model.pkl       # Trained model
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   └── prediction.py
└── .streamlit/config.toml      # Streamlit config
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

## 🌐 Deployment

### Deploy on Streamlit Cloud

1. **Push to GitHub:**
   ```bash
   git push -u origin main
   ```

2. **Deploy:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect GitHub repository
   - Select main file: `app.py`
   - Click Deploy

3. **Live URL:** `https://your-username.streamlit.app`

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

## 📞 Support

- 📧 GitHub Issues: Report problems
- 💬 Streamlit Community: Get help

---

## 🎉 Quick Links

- 📚 [Streamlit Docs](https://docs.streamlit.io)
- 🐍 [Python Docs](https://docs.python.org)
- 📊 [scikit-learn](https://scikit-learn.org)

---

**Made with ❤️ | April 2026**
python setup.py
```

#### 4. Start the Application
```bash
streamlit run app.py
```

Navigate to the provided localhost URL (usually `http://localhost:8501`) to experience the AI Job Predictor.

## Usage
1. **EDA Tab:** Explore the dataset with interactive filters and visualizations.
2. **Model Training Tab:** Train ML models and view performance metrics with feature importance.
3. **Salary Prediction Tab:** Input job details to get salary predictions.

## Deployment Notes
This project is designed to be fully compatible with Streamlit Community Cloud. Simply connect this repository and set the main file path to `app.py`.

# AI Job Data Analysis and Salary Prediction System 🚀

A complete end-to-end Machine Learning application for AI/ML job market analysis with interactive salary predictions, powered by Streamlit.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 🎯 Features

### 📊 **Exploratory Data Analysis (EDA) Dashboard**
- Interactive filters by Experience Level, Company Size, Job Title
- Real-time salary distribution visualizations
- Salary trends by experience and company size
- Top job roles frequency analysis
- CSV dataset download capability
- **Currency Conversion:** View salaries in USD or Indian Rupees (₹)

### 💡 **Advanced Salary Prediction**
- ML-powered predictions using trained Random Forest model
- Input job details: role, experience, location, employment type, remote ratio
- Instant predictions with USD/INR conversion
- Company size and location impact analysis

### 🤖 **Machine Learning Pipeline**
- **Models Trained:** Linear Regression, Random Forest, XGBoost, Hybrid Ensemble
- **Automatic Model Selection:** Best model chosen based on R² score
- **Feature Engineering:** Automatic encoding and scaling
- **Evaluation Metrics:** R² Score, MAE, MSE displayed

### 💰 **Sidebar Tools**
- Quick USD to INR currency converter
- Pre-calculated conversions for common salary ranges

---

## 📁 Project Structure

```
job-salary-predictor/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── run_project.bat             # Windows launcher script
│
├── data/
│   └── ds_salaries.csv         # AI/ML job salary dataset (1000 rows)
│
├── models/
│   └── best_model.pkl          # Pre-trained ML model
│
├── notebooks/
│   └── eda_analysis.ipynb      # Jupyter notebook for EDA
│
├── src/
│   ├── data_preprocessing.py   # Data cleaning & feature engineering
│   ├── model_training.py       # Model training & evaluation
│   └── prediction.py           # Inference module
│
└── .streamlit/
    └── config.toml             # Streamlit configuration
```

---

## 🚀 Installation & Usage

### Option 1: Windows (Fast Track)
```bash
double-click run_project.bat
```

### Option 2: Manual Setup

#### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

#### Step 1: Clone/Download Repository
```bash
git clone https://github.com/YOUR_USERNAME/job-salary-predictor.git
cd job-salary-predictor
```

#### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 3: Run the Application
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 📊 Dataset Information

**ds_salaries.csv** contains:
- **Rows:** 1,000 job records
- **Columns:** 11 features
- **Salary Range:** $50K - $340K USD
- **Job Roles:** Data Scientist, Engineer, ML Engineer, Analyst, etc.
- **Experience Levels:** Entry, Mid, Senior, Executive
- **Locations:** US, Canada, UK, India, Germany, France, etc.

### Features:
- `work_year` - Year of the job posting
- `experience_level` - Experience level (EN/MI/SE/EX)
- `employment_type` - Full-time/Part-time/Contract/Freelance
- `job_title` - Job position
- `salary_in_usd` - Annual salary in USD
- `remote_ratio` - Remote work percentage (0/50/100)
- `company_location` - Company location code
- `company_size` - Company size (S/M/L)

---

## 🎓 How It Works

### 1. Data Processing
- Loads and cleans data
- Handles missing values
- Encodes categorical variables
- Scales numerical features

### 2. Model Training
- Splits data (80/20 train/test)
- Trains 4 different models
- Evaluates using R², MAE, MSE
- Saves best model to `models/best_model.pkl`

### 3. Prediction
- Accepts user inputs
- Preprocesses features
- Passes through trained model
- Returns salary prediction with confidence

### 4. Visualization
- Interactive Plotly charts
- Real-time filtering
- Responsive design
- Dark theme with custom colors

---

## 📈 Model Performance

| Model | R² Score | MAE ($) |
|-------|----------|---------|
| Linear Regression | 0.8926 | $14,124 |
| **Random Forest** | **0.8981** | **$14,056** |
| XGBoost | 0.8804 | $15,037 |
| Hybrid Ensemble | 0.8960 | $14,146 |

✅ **Best Model:** Random Forest Regressor

---

## 💱 Currency Features

- **USD Display:** View all salaries in US Dollars
- **INR Display:** Convert to Indian Rupees (₹)
- **Exchange Rate:** 1 USD = ₹83.45
- **Quick Converter:** Pre-calculated salary conversions in sidebar

---

## 🌐 Live Deployment

### Deploy on Streamlit Cloud (Recommended)

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/job-salary-predictor.git
   git push -u origin main
   ```

2. **Deploy:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Select repository
   - Set main file: `app.py`
   - Click Deploy

3. **Your app will be live at:**
   ```
   https://job-salary-predictor-YOUR_USERNAME.streamlit.app
   ```

### Alternative Deployment Options
- **Heroku:** Deploy with Docker
- **AWS:** EC2 or App Runner
- **Google Cloud:** Cloud Run
- **Azure:** App Service

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|---------------|
| **Framework** | Streamlit 1.40+ |
| **ML Libraries** | scikit-learn, XGBoost |
| **Data Processing** | pandas, numpy |
| **Visualization** | Plotly, Seaborn, Matplotlib |
| **Model Serialization** | joblib |
| **Python Version** | 3.9+ |

---

## 📊 Usage Examples

### Example 1: Predict Salary
1. Go to "🔮 Salary Prediction" tab
2. Select: Senior level, Full-time, Data Scientist, US
3. Click "Predict Salary ✨"
4. View prediction in USD or INR

### Example 2: Analyze Trends
1. Go to "📊 Exploratory Data Analysis" tab
2. Filter by Experience Level: "Senior-level"
3. View salary distribution and top roles
4. Download processed CSV

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Model not loading | Ensure `best_model.pkl` exists in `/models` |
| Data not loading | Check `ds_salaries.csv` path in `/data` |
| Dependencies missing | Run `pip install -r requirements.txt` |
| Port already in use | Change port: `streamlit run app.py --server.port 8502` |

---

## 📝 Future Enhancements

- [ ] Real-time data from job APIs
- [ ] More advanced models (LSTM, Neural Networks)
- [ ] Skills-based salary impact analysis
- [ ] Company comparison tool
- [ ] Salary negotiation tips
- [ ] Multi-language support
- [ ] Mobile app version

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

**AI Job Market Analysis Team**
- GitHub: [Your GitHub Profile]
- Email: your.email@example.com

---

## 📞 Support

For issues, questions, or suggestions:
- 📧 Open an Issue on GitHub
- 💬 Streamlit Community: [discuss.streamlit.io](https://discuss.streamlit.io)

---

## 🙏 Acknowledgments

- Dataset: AI/ML Job Salary Data
- Built with: Streamlit, scikit-learn, XGBoost
- Inspired by: Real-world salary prediction needs

---

## 🎉 Quick Links

- 🌐 [Live Demo](https://job-salary-predictor.streamlit.app)
- 📚 [Streamlit Docs](https://docs.streamlit.io)
- 🐍 [Python Docs](https://docs.python.org)
- 📊 [scikit-learn](https://scikit-learn.org)

---

**Last Updated:** April 2026 | Made with ❤️
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

import streamlit as st
import pandas as pd
import plotly.express as px
import os
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline

# Currency exchange rate (USD to INR)
USD_TO_INR = 83.45

from src.data_preprocessing import load_data, clean_data_for_eda
from src.model_training import train_models
from src.prediction import load_model, predict_salary

# Configuring basic Streamlit page style
st.set_page_config(
    page_title="AI Job Data & Salary Predictor",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for aesthetic improvements
st.markdown("""
<style>
    .main-header {
        font-family: 'Inter', sans-serif;
        color: #1E3A8A;
        font-weight: 800;
        text-align: center;
        padding-bottom: 2rem;
    }
    .metric-card {
        background-color: #F3F4F6;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Application Heading
st.markdown("<h1 class='main-header'>AI Job Data Analysis and Salary Prediction </h1>", unsafe_allow_html=True)

# Sidebar - Currency Converter
with st.sidebar:
    st.header("💱 Currency Converter")
    st.write("**USD to INR Converter**")
    usd_amount = st.number_input("Enter USD Amount", value=100000, min_value=0, step=10000)
    USD_TO_INR = 83.45
    inr_amount = usd_amount * USD_TO_INR
    st.success(f"${usd_amount:,.0f} USD = ₹{inr_amount:,.0f} INR")
    st.caption(f"*Exchange rate: 1 USD = ₹{USD_TO_INR} (April 2026)")
    
    # Additional conversion info
    st.divider()
    st.write("**Quick Conversions**")
    conversions = {
        "$50,000": 50000 * USD_TO_INR,
        "$100,000": 100000 * USD_TO_INR,
        "$150,000": 150000 * USD_TO_INR,
        "$200,000": 200000 * USD_TO_INR,
    }
    for usd, inr in conversions.items():
        st.write(f"{usd} = ₹{inr:,.0f}")
    
    st.divider()

# Define Tabs
tab1, tab2 = st.tabs(["📊 Exploratory Data Analysis", "🔮 Salary Prediction"])

# --- TAB 1: EDA ---
with tab1:
    st.header("Exploratory Data Analysis (EDA)")
    try:
        raw_df = load_data()
        st.success("Successfully loaded dataset from default path.")
        
        # Prepare data for EDA
        df_eda = clean_data_for_eda(raw_df)
        
        # Filters
        st.subheader("Filters")
        col1, col2, col3 = st.columns(3)
        with col1:
            exp_filter = st.multiselect("Experience Level", options=df_eda['experience_level'].unique(), default=df_eda['experience_level'].unique())
        with col2:
            size_filter = st.multiselect("Company Size", options=df_eda['company_size'].unique(), default=df_eda['company_size'].unique())
        with col3:
            job_filter = st.multiselect("Job Title", options=df_eda['job_title'].unique(), default=df_eda['job_title'].unique()[:5])
        
        # Apply filters
        filtered_df = df_eda[
            (df_eda['experience_level'].isin(exp_filter)) &
            (df_eda['company_size'].isin(size_filter)) &
            (df_eda['job_title'].isin(job_filter))
        ]
        
        # Currency selection for EDA
        col_curr = st.columns(1)[0]
        eda_currency = col_curr.selectbox("View Salaries In:", ["USD", "INR"], key="eda_currency")
        
        # Create a copy of filtered_df with converted salaries if needed
        display_df = filtered_df.copy()
        if eda_currency == "INR":
            display_df['salary_in_usd'] = display_df['salary_in_usd'] * USD_TO_INR
            salary_label = "Salary (INR)"
            salary_format = "₹"
        else:
            salary_label = "Salary (USD)"
            salary_format = "$"
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Records", display_df.shape[0])
        col2.metric("Total Job Roles", display_df['job_title'].nunique())
        col3.metric("Avg Salary", f"{salary_format}{display_df['salary_in_usd'].mean():,.0f}")
        col4.metric("Max Salary", f"{salary_format}{display_df['salary_in_usd'].max():,.0f}")
        
        st.markdown("---")
        
        # Row 1 of Charts
        chart_col1, chart_col2 = st.columns(2)
        with chart_col1:
            st.subheader("Salary Distribution")
            fig1 = px.histogram(display_df, x="salary_in_usd", nbins=50, title=f"Distribution of {salary_label}",
                               color_discrete_sequence=['#3B82F6'])
            fig1.update_xaxes(title_text=salary_label)
            st.plotly_chart(fig1, use_container_width=True)
            
        with chart_col2:
            st.subheader("Salary vs Experience Level")
            order = ['Entry-level', 'Mid-level', 'Senior-level', 'Executive/Director']
            fig2 = px.box(display_df, x="experience_level", y="salary_in_usd", category_orders={"experience_level": order},
                          color="experience_level", title=f"Salary Ranges by Experience Level ({eda_currency})")
            fig2.update_yaxes(title_text=salary_label)
            st.plotly_chart(fig2, use_container_width=True)
            
        # Row 2 of Charts
        chart_col3, chart_col4 = st.columns(2)
        with chart_col3:
            st.subheader("Top 10 Job Roles Frequency")
            top_roles = display_df['job_title'].value_counts().nlargest(10).reset_index()
            top_roles.columns = ['Job Title', 'Count']
            fig3 = px.bar(top_roles, x='Count', y='Job Title', orientation='h', title="Most Common Roles",
                          color='Count', color_continuous_scale='Blues')
            fig3.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig3, use_container_width=True)
            
        with chart_col4:
            st.subheader("Company Size Impact on Salary")
            fig4 = px.violin(display_df, x="company_size", y="salary_in_usd", color="company_size", box=True,
                             title=f"Salary Distribution by Company Size ({eda_currency})")
            fig4.update_yaxes(title_text=salary_label)
            st.plotly_chart(fig4, use_container_width=True)
            
        st.subheader("Raw Data Preview")
        st.dataframe(display_df.head(10))
        
        # Download button
        csv = raw_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Processed CSV Dataset (USD)",
            data=csv,
            file_name="ai_job_salaries.csv",
            mime="text/csv",
        )
        
    except FileNotFoundError:
        st.error("Dataset not found. Please ensure the dataset is available in the data folder.")
    except Exception as e:
        st.error(f"Error loading EDA: {e}")

# --- TAB 2: Salary Prediction ---
with tab2:
    st.header("Predict Your Salary")
    st.write("Enter the job details below to get an AI-powered salary estimate.")
    
    # Try to load existing data to get unique values for dropdowns
    try:
        df_for_dropdowns = clean_data_for_eda(load_data())
        job_titles = sorted(df_for_dropdowns['job_title'].dropna().unique().tolist())
        locations = sorted(df_for_dropdowns['company_location'].dropna().unique().tolist())
        residences = sorted(df_for_dropdowns['employee_residence'].dropna().unique().tolist())
    except:
        job_titles = ['Data Scientist', 'Data Engineer', 'Machine Learning Engineer', 'Data Analyst']
        locations = ['US', 'GB', 'IN', 'CA', 'DE']
        residences = ['US', 'GB', 'IN', 'CA', 'DE']

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            work_year = st.selectbox("Work Year", [2024, 2023, 2022, 2021, 2020])
            exp_level = st.selectbox("Experience Level", ['EN', 'MI', 'SE', 'EX'], 
                                     format_func=lambda x: {'EN':'Entry', 'MI':'Mid', 'SE':'Senior', 'EX':'Executive'}[x])
            emp_type = st.selectbox("Employment Type", ['FT', 'PT', 'CT', 'FL'],
                                    format_func=lambda x: {'FT':'Full-time', 'PT':'Part-time', 'CT':'Contract', 'FL':'Freelance'}[x])
            job_title = st.selectbox("Job Title / Role", job_titles)
            
        with col2:
            remote_ratio = st.selectbox("Remote Pattern", [0, 50, 100], 
                                        format_func=lambda x: {0:'On-site', 50:'Hybrid', 100:'Fully Remote'}[x])
            company_location = st.selectbox("Company Location (Country Code)", locations)
            employee_residence = st.selectbox("Employee Residence (Country Code)", residences)
            company_size = st.selectbox("Company Size", ['S', 'M', 'L'],
                                        format_func=lambda x: {'S':'Small', 'M':'Medium', 'L':'Large'}[x])
        
        # Currency selection
        currency = st.selectbox("Display Salary In", ["USD (US Dollars)", "INR (Indian Rupees)"])
        
        submit_button = st.form_submit_button(label="Predict Salary ✨")
        
    if submit_button:
        input_dict = {
            'work_year': work_year,
            'experience_level': exp_level,
            'employment_type': emp_type,
            'job_title': job_title,
            'remote_ratio': remote_ratio,
            'company_location': company_location,
            'employee_residence': employee_residence,
            'company_size': company_size
        }
        
        with st.spinner("Analyzing parameters..."):
            try:
                model = load_model()
                pred_value_usd = predict_salary(model, input_dict)
                
                # Convert to selected currency
                if "INR" in currency:
                    pred_value = pred_value_usd * USD_TO_INR
                    currency_symbol = "₹"
                    currency_str = "INR"
                else:
                    pred_value = pred_value_usd
                    currency_symbol = "$"
                    currency_str = "USD"
                
                st.markdown(f"""
                <div style="background-color: #DEF7EC; padding: 20px; border-radius: 10px; border-left: 5px solid #31C48D; margin-top: 20px;">
                    <h3 style="color: #03543F; margin: 0;">Predicted Annual Salary:</h3>
                    <h1 style="color: #046C4E; font-size: 3em; margin: 0;">{currency_symbol}{pred_value:,.2f} {currency_str}</h1>
                </div>
                """, unsafe_allow_html=True)
                
                # Show currency conversion
                if "INR" in currency:
                    st.info(f"💱 Conversion: ${pred_value_usd:,.2f} USD = ₹{pred_value:,.2f} INR (Rate: 1 USD = ₹{USD_TO_INR})")
                
            except FileNotFoundError:
                st.error("Model is not trained yet. Please go to the 'Model Training' tab and train the models first.")
            except Exception as e:
                st.error(f"Prediction Error: {e}")


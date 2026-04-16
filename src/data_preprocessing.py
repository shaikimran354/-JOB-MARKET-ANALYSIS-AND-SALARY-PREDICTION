import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import os

def load_data(path='data/ds_salaries.csv'):
    """Loads the dataset from the given path."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found at {path}. Please run setup.py or upload a file.")
    df = pd.read_csv(path)
    
    # Drop the unnamed index column if it exists
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    
    # Handle column naming - rename salary_usd to salary_in_usd for consistency
    if 'salary_usd' in df.columns and 'salary_in_usd' not in df.columns:
        df = df.rename(columns={'salary_usd': 'salary_in_usd'})
    
    # Handle work_year if it doesn't exist (use years_experience or create default)
    if 'work_year' not in df.columns:
        if 'years_experience' in df.columns:
            df['work_year'] = 2024 - df['years_experience'].clip(lower=0, upper=10)
        else:
            df['work_year'] = 2024
        
    return df

def clean_data_for_eda(df):
    """Basic cleaning for Exploratory Data Analysis."""
    df = df.copy()
    
    # Map experience levels to more descriptive labels
    exp_map = {
        'EN': 'Entry-level',
        'MI': 'Mid-level',
        'SE': 'Senior-level',
        'EX': 'Executive/Director'
    }
    if 'experience_level' in df.columns:
        df['experience_level'] = df['experience_level'].map(exp_map).fillna(df['experience_level'])
        
    # Map employment types
    emp_map = {
        'PT': 'Part-time',
        'FT': 'Full-time',
        'CT': 'Contract',
        'FL': 'Freelance'
    }
    if 'employment_type' in df.columns:
        df['employment_type'] = df['employment_type'].map(emp_map).fillna(df['employment_type'])
    
    # Map company size
    size_map = {
        'S': 'Small (<50)',
        'M': 'Medium (50-250)',
        'L': 'Large (>250)'
    }
    if 'company_size' in df.columns:
        df['company_size'] = df['company_size'].map(size_map).fillna(df['company_size'])

    return df

def build_preprocessing_pipeline():
    """Builds a scikit-learn preprocessing pipeline for categorical and numerical features."""
    
    # Define features - will filter to only those that exist in the dataset
    categorical_features = ['experience_level', 'employment_type', 'job_title', 'employee_residence', 'company_location', 'company_size']
    numerical_features = ['work_year', 'remote_ratio', 'years_experience']
    
    # Pipeline for numeric features
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    # Pipeline for categorical features
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    # Combine using ColumnTransformer - will only use features that exist
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numerical_features),
            ('cat', categorical_transformer, categorical_features)
        ],
        remainder='drop'
    )
    
    return preprocessor

def get_train_test_split(df, test_size=0.2, random_state=42):
    """Splits dataset into X_train, X_test, y_train, y_test"""
    target = 'salary_in_usd'
    
    X = df.drop(columns=[target, 'salary', 'salary_currency'], errors='ignore')
    if target in df.columns:
        y = df[target]
    else:
        raise ValueError(f"Target column '{target}' not found in dataset.")
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # Quick test
    df = load_data()
    print("Initial shape:", df.shape)
    preprocessor = build_preprocessing_pipeline()
    X_train, X_test, y_train, y_test = get_train_test_split(df)
    
    # Fit transform print shape
    X_train_processed = preprocessor.fit_transform(X_train)
    print("Processed X_train shape:", X_train_processed.shape)

import pandas as pd
import numpy as np
import joblib
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, VotingRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from src.data_preprocessing import load_data, get_train_test_split, build_preprocessing_pipeline

def evaluate_model(model, X_test, y_test):
    """Evaluates the model and returns MAE, MSE, and R2."""
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    return mae, mse, r2

def train_models(df):
    """
    Trains multiple models, evaluates them, selects the best, 
    and saves the complete pipeline to models/best_model.pkl
    """
    X_train, X_test, y_train, y_test = get_train_test_split(df)
    preprocessor = build_preprocessing_pipeline()

    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        "XGBoost": XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42),
        "Hybrid (RF + XGBoost)": VotingRegressor([
            ('rf', RandomForestRegressor(n_estimators=50, random_state=42)),
            ('xgb', XGBRegressor(n_estimators=50, learning_rate=0.1, random_state=42))
        ])
    }

    results = {}
    best_model_name = None
    best_r2 = -float('inf')
    best_pipeline = None

    for name, model in models.items():
        print(f"Training {name}...")
        
        # Create a complete pipeline combining preprocessor and model
        pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', model)
        ])
        
        # Fit pipeline
        pipeline.fit(X_train, y_train)
        
        # Evaluate
        mae, mse, r2 = evaluate_model(pipeline, X_test, y_test)
        
        results[name] = {
            'MAE': mae,
            'MSE': mse,
            'R2': r2
        }
        
        print(f"[{name}] R2: {r2:.4f} | MAE: {mae:.2f}")

        # Update best model
        if r2 > best_r2:
            best_r2 = r2
            best_model_name = name
            best_pipeline = pipeline

    print(f"\nBest Model: {best_model_name} with R2: {best_r2:.4f}")
    
    # Save the best pipeline
    os.makedirs('models', exist_ok=True)
    model_path = os.path.join('models', 'best_model.pkl')
    joblib.dump(best_pipeline, model_path)
    print(f"Best model saved to {model_path}")

    return results, best_model_name, best_pipeline

if __name__ == "__main__":
    df = load_data()
    train_models(df)

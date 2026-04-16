import joblib
import pandas as pd
import os

def load_model(model_path='models/best_model.pkl'):
    """Loads the trained machine learning pipeline."""
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}. Please train the model first.")
        
    return joblib.load(model_path)

def predict_salary(model, input_dict):
    """
    Given a loaded model and a dictionary of inputs mapping to features,
    returns the predicted salary.
    """
    # Create a DataFrame from the dictionary
    df_input = pd.DataFrame([input_dict])
    
    # Predict using the full pipeline 
    # (The pipeline handles scaling and encoding automatically based on its training)
    prediction = model.predict(df_input)
    
    return prediction[0]

if __name__ == "__main__":
    # Test inference
    try:
        model = load_model()
        test_input = {
            'work_year': 2024,
            'experience_level': 'SE',
            'employment_type': 'FT',
            'job_title': 'Data Scientist',
            'remote_ratio': 100,
            'employee_residence': 'US',
            'company_location': 'US',
            'company_size': 'M'
        }
        pred = predict_salary(model, test_input)
        print(f"Predicted Salary for test input: ${pred:,.2f}")
    except Exception as e:
        print(f"Error during prediction test: {e}")

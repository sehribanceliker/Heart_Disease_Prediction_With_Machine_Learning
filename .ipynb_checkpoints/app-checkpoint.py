from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

app = Flask(__name__)

model = pickle.load(open('models/random_forest_model.pkl', 'rb'))
label_encoders = pickle.load(open('models/label_encoders.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

categorical_columns = ['LocationAbbr', 'GeographicLevel', 'Data_Value_Type', 'Stratification1', 'Stratification2']

valid_location_abbr = label_encoders['LocationAbbr'].classes_

def preprocess_data(input_data):
    input_df = pd.DataFrame([input_data], columns=categorical_columns)
    
    for column in categorical_columns:
        le = label_encoders[column]
        input_df[column] = le.transform(input_df[column].astype(str))
    
    input_scaled = scaler.transform(input_df)
    
    return input_scaled

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [request.form.get(key) for key in categorical_columns]
    
    location_abbr = input_data[0]
    if location_abbr not in valid_location_abbr:
        error_message = f"Invalid LocationAbbr value: {location_abbr}"
        return render_template('error.html', error_message=error_message)
    
    input_processed = preprocess_data(input_data)
    
    prediction = model.predict(input_processed)[0]
    
    result = 'High risk of heart attack' if prediction == 1 else 'Low risk of heart attack'
    return render_template('result.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)

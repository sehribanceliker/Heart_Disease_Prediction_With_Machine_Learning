## Heart Disease Mortality Data Among US Adults (35+) by State/Territory and County

 # Heart Disease Mortality Data Among US Adults (35+) by State/Territory and County

 This repository contains data and code related to the analysis and prediction of heart disease mortality rates among US adults aged 35 and older, by state, territory, and county. Also i created the backend and frontend for application. Flask and HTML was used for application and and given data predict to high risk heart disease, low risk heart disease etc.

 ## Data Description

 The dataset covers the years 2013 to 2015 and provides 3-year average rates that are age-standardized. County rates are spatially smoothed. The data is further broken down by gender and race/ethnicity.

 ### Source

 The data is sourced from the [National Vital Statistics System](http://www.cdc.gov/dhdsp/maps/atlas).

 ## Project Overview

 Heart disease, also known as cardiovascular disease, encompasses various conditions that impact the heart. It has been the leading cause of death worldwide for the past few decades. This project aims to leverage machine learning techniques to analyze complex medical data and help healthcare professionals predict heart disease.

 ## Contents

 - `Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv`: The dataset used for analysis.
 - `app.py`: A Flask application for predicting heart disease mortality rates.
 - `heart_disease_classification_model.ipynb`: A Jupyter Notebook containing the machine learning model and analysis.
 - `index.html`: A simple HTML page for displaying results.

 ## Getting Started

 ### Prerequisites

 Ensure you have the following installed:

 - Python 3.x
 - Flask
 - Joblib
 - Pandas
 - Scikit-learn

 ### Installation

 1. Clone the repository:
     ```bash
     git clone https://github.com/sehribanceliker/Heart-Disease-Mortality-Data-Among-US-Adults-35-by-State-Territory-and-County.git
     cd Heart-Disease-Mortality-Data-Among-US-Adults-35-by-State-Territory-and-County
     ```

 2. Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

 ### Usage

 1. Run the Flask application:
     ```bash
     python app.py
     ```

 2. Access the application in your web browser at `http://127.0.0.1:5000`.

 ## Model and Analysis

 Detailed analysis and model training process can be found in the `heart_disease_classification_model.ipynb` notebook.

 ## Contributing

 Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

 ## License

 This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

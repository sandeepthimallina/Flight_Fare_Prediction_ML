# Flight Fare Prediction Using Python and Machine Learning

## Project Overview

This is a Python-based Machine Learning project that predicts flight ticket prices based on different flight details.

The project includes data analysis, data visualization, Machine Learning model training, model evaluation, and a Streamlit web application.

## Objective

The objective of this project is to predict the price of a flight using:

- Airline
- Source city
- Destination city
- Class
- Day
- Month
- Departure hour
- Arrival hour
- Flight duration
- Number of stops

## Dataset

The project uses a cleaned flight fare dataset.

- Rows: 300,257
- Columns: 25
- Airlines: 8
- Source cities: 6
- Destination cities: 6
- Missing values: 0
- Duplicate rows: 0

## Machine Learning Model

A Random Forest Regression model is used to predict flight fares.

The dataset was divided into:

- Training data: 240,205 rows
- Testing data: 60,052 rows

## Model Performance

| Metric | Result |
|---|---:|
| MAE | 1149.62 |
| RMSE | 2535.47 |
| R² Score | 0.9876 |

The R² score of 0.9876 means that the model explains approximately 98.76% of the variation in the test-set flight fares.

## Data Visualization

The project includes the following visualizations:

1. Average fare by airline
2. Average fare by number of stops
3. Average fare by class
4. Top 10 routes by average fare
5. Flight fare distribution
6. Average fare by flight duration

## Streamlit Application

The trained Machine Learning model is connected to a Streamlit web application.

The user can enter flight details and click **Predict Flight Fare** to get the estimated ticket price.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Visual Studio Code

## Project Structure

```text
Flight_Fare_Prediction/
│
├── data/
│   └── Freshly_cleaned.csv
│
├── models/
│   └── flight_fare_model.pkl
│
├── notebooks/
│
├── venv/
│
├── app.py
├── data_analysis.py
├── model_training.py
├── visualization.py
├── requirements.txt
└── README.md
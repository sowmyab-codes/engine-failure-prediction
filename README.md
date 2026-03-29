# Aircraft Engine Failure Prediction

## Overview
This project predicts the liklihood of aircraft engine failure using machine learning.
It uses sensor data to classify whther the engine is safe or likely to fail soon.

## Problem Statement
Aircraft engines generate large amounts of sensor data.
Predicting failures in advance helps in:
-Preventive maintanence
-Reducing operational risks
-Improving safety

## Solution
A machine learning model is trained on engine sensor data and deployed as an API using FASTAPI.

## Features
-Predicts engine condition (Safe/Failure Soon)
-Built using Random Forest
-API developed using FastAPI

## Tech Stack
-Python
-Scikit-learn
-FastAPI
-Numpy
-joblib

## Project Structure
app/main.py
model/engine_failure_model.pkl
notebooks/aircraft_engine_failure_prediction.ipynb
requirements.txt
README.md

## How to Run the Project
### Step 1 - Install dependencies
pip install -r requirements.txt
### Step 2 - Run API
uvicorn app.main:app --reload
### Step 3- Open in browser
http://127.0.0.1:8000/docs

## API usage
### Endpoint
POST /predict
### Input
A list of 26 sensor values:
[200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200]

### Output
{"prediction": "Safe"}
or
{"prediction": "Failure Soon"}

## Data set
NASA turbofan Engine Degradation Simulation Dataset(C-MAPSS)

## Key Learnings
- End-to-end ML pipeline
- Model deployment using FastAPI
- API development and testing
- Handling real-world debugging issues

## Future Improvement
- Add frontend UI
- Improve model accuracy
- Deploy to cloud(AWS / Render)

## Author
Sowmya B

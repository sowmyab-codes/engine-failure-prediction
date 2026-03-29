# engine-failure-prediction
Predict remaining useful life of aircraft engines using NASA C-MAPSS dataset
##Overview
This project predicts aircraft engine failure using machine learning.
##Features
-Predicts engine condition (Safe/Failure Soon)
-Built using Random Forest
-API developed using FastAPI

## Tech Stack
-Python
-Scikit-learn
-FastAPI

## How to use
Send a POST request to /predict with 26 sensor values.

## Example Input
[200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200]

##Output
Safe / Failure Soon

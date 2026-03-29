from fastapi import FastAPI
import joblib
import numpy as np

print("Step 1: Imports done")

app = FastAPI()
print("Step 2: App created")
model = joblib.load("engine_failure_model.pkl")
print("Step 3: Model Loaded")

@app.get("/")
def home():
  return{"message":"Aircraft Engine Failure Prediction API"}
print("Step 4: Home endpoint added")

@app.post("/predict")
def predict(sensors: list[float]):

  data = np.array(sensors).reshape(1, -1)
  prediction = model.predict(data)[0]

  result = "Failure Soon" if prediction == 1 else "No Failure"
  return {"prediction": result}

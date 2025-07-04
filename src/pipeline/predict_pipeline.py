import pandas as pd
import numpy as np
import pickle
from src.logger import logger
from src.exception import CustomException
import sys

class PredictPipeline:
    def __init__(self):
        self.model_path = "artifacts/model.pkl"
        self.scaler_path = "artifacts/scaler.pkl"

    def predict(self, features):
        try:
            logger.info("Starting prediction")
            with open(self.model_path, "rb") as model_file:
                model = pickle.load(model_file)
            with open(self.scaler_path, "rb") as scaler_file:
                scaler = pickle.load(scaler_file)

            features_scaled = scaler.transform(features)
            prediction = model.predict(features_scaled)
            logger.info("Prediction completed")
            return prediction
        except Exception as e:
            logger.error("Error in prediction")
            raise CustomException(str(e), sys)

class CustomData:
    def __init__(self, glucose, blood_pressure, skin_thickness, insulin, bmi):
        self.glucose = glucose
        self.blood_pressure = blood_pressure
        self.skin_thickness = skin_thickness
        self.insulin = insulin
        self.bmi = bmi

    def get_data_as_dataframe(self):
        try:
            data = {
                "Glucose": [self.glucose],
                "BloodPressure": [self.blood_pressure],
                "SkinThickness": [self.skin_thickness],
                "Insulin": [self.insulin],
                "BMI": [self.bmi]
            }
            return pd.DataFrame(data)
        except Exception as e:
            logger.error("Error converting data to DataFrame")
            raise CustomException(str(e), sys)
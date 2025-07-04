import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from src.logger import logger
from src.exception import CustomException
from src.utils import save_object
import os
import sys

class DataTransformation:
    def __init__(self):
        self.scaler_path = os.path.join("artifacts", "scaler.pkl")
        self.features = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            # No cleaning needed here - already done before split
            X_train = train_df[self.features]
            y_train = train_df["Outcome"]
            X_test = test_df[self.features]
            y_test = test_df["Outcome"]

            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            save_object(self.scaler_path, scaler)

            train_arr = np.c_[X_train_scaled, y_train]
            test_arr = np.c_[X_test_scaled, y_test]

            return train_arr, test_arr, self.scaler_path
            
        except Exception as e:
            raise CustomException(str(e), sys)
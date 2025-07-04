import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logger
from src.exception import CustomException
from src.utils import save_dataframe
import os
import sys

class DataIngestion:
    def __init__(self):
        self.raw_data_path = os.path.join("artifacts", "raw.csv")
        self.cleaned_data_path = os.path.join("artifacts", "cleaned.csv")
        self.train_data_path = os.path.join("artifacts", "train.csv")
        self.test_data_path = os.path.join("artifacts", "test.csv")

    def clean_data(self, df):
        """Apply all cleaning steps from notebook"""
        df = df[df['Pregnancies'] <= 13]
        df = df[df['Glucose'] != 0]
        df = df[df['BloodPressure'] >= 40]
        df = df[(df['SkinThickness'] != 0) & (df['SkinThickness'] != 99)]
        df = df[(df['Insulin'] != 0) & (df['Insulin'] <= 500)]
        df = df[(df['BMI'] != 0) & (df['BMI'] < 53.2)]
        df = df[(df['DiabetesPedigreeFunction'] >= 0.1) & 
               (df['DiabetesPedigreeFunction'] <= 2.0)]
        return df

    def initiate_data_ingestion(self):
        try:
            logger.info("Starting data ingestion")
            # 1. Load raw data
            df = pd.read_csv("notebooks/diabetes.csv")
            save_dataframe(df, self.raw_data_path)
            
            # 2. Clean BEFORE splitting (like notebook)
            cleaned_df = self.clean_data(df)
            save_dataframe(cleaned_df, self.cleaned_data_path)
            
            # 3. Split with same random_state
            train_set, test_set = train_test_split(
                cleaned_df, 
                test_size=0.2, 
                random_state=0  # Must match notebook
            )
            
            save_dataframe(train_set, self.train_data_path)
            save_dataframe(test_set, self.test_data_path)

            logger.info(f"Train samples: {len(train_set)}, Test samples: {len(test_set)}")
            return self.train_data_path, self.test_data_path
            
        except Exception as e:
            logger.error("Error in data ingestion")
            raise CustomException(str(e), sys)
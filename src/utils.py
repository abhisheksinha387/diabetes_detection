import os
import pickle
import sys
import pandas as pd
from src.logger import logger
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logger.info(f"Object saved to {file_path}")
    except Exception as e:
        logger.error(f"Error saving object to {file_path}")
        raise CustomException(e, sys)

def save_dataframe(df, file_path):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df.to_csv(file_path, index=False)
        logger.info(f"DataFrame saved to {file_path}")
    except Exception as e:
        logger.error(f"Error saving DataFrame to {file_path}")
        raise CustomException(str(e), sys)
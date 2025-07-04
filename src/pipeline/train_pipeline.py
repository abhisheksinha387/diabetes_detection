from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logger
from src.exception import CustomException
import sys

def main():
    try:
        # Data Ingestion
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        # Data Transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, scaler_path = data_transformation.initiate_data_transformation(
            train_data_path, test_data_path
        )

        # Model Training with GridSearch
        model_trainer = ModelTrainer()
        model = model_trainer.initiate_model_trainer(train_arr, test_arr)

        logger.info("Training pipeline completed successfully")
        return model  # Return model for further inspection if needed
        
    except Exception as e:
        logger.error("Error in training pipeline")
        raise CustomException(str(e), sys)

if __name__ == "__main__":
    main()
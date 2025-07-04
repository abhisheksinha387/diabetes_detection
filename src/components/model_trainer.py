from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from src.logger import logger
from src.exception import CustomException
from src.utils import save_object
import os
import sys
import numpy as np

class ModelTrainer:
    def __init__(self):
        self.model_path = os.path.join("artifacts", "model.pkl")

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logger.info("Starting model training")
            X_train = train_array[:, :-1]
            y_train = train_array[:, -1]
            X_test = test_array[:, :-1]
            y_test = test_array[:, -1]

            # Define the model and parameters for GridSearch
            logistic = LogisticRegression(max_iter=1000)
            parameters = {
                'C': [0.01, 0.1, 1, 10],
                'class_weight': [None, 'balanced']
            }

            # Perform GridSearchCV
            grid_search = GridSearchCV(
                estimator=logistic,
                param_grid=parameters,
                scoring='accuracy',
                cv=5,
                verbose=1
            )
            grid_search.fit(X_train, y_train)

            # Get best model
            model = grid_search.best_estimator_
            
            # Log best parameters
            logger.info(f"Best parameters found: {grid_search.best_params_}")
            logger.info(f"Best accuracy score: {grid_search.best_score_}")

            # Save model
            save_object(self.model_path, model)
            
            # Evaluate
            test_acc = model.score(X_test, y_test)
            logger.info(f"Test set accuracy: {test_acc}")
            
            return model
            
        except Exception as e:
            raise CustomException(e, sys)
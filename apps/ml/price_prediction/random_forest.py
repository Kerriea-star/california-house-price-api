from pathlib import Path
import os
import joblib
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent

class RandomForestRegressor:
    def __init__(self):
        path_to_artifacts = "C:/Users/ojare/AIML/house-price-prediction/backend/carlifornia/artifacts/"

        self.values_fill_missing = joblib.load(path_to_artifacts + "train_mode.joblib")
        self.encoders = joblib.load(path_to_artifacts + "encoders.joblib")
        self.model = joblib.load(path_to_artifacts + "random_forest.joblib")

    def preprocessing(self, input_data):
        # JSON to pandas DataFrame
        input_data = pd.DataFrame(input_data, index=[0])
        # fill missing values
        input_data.fillna(self.values_fill_missing)
        # convert categoricals
        for column in ["ocean_proximity"]:
            categorical_convert = self.encoders[column]
            input_data[column] = categorical_convert.transform(input_data[column])
        return input_data
    def predict(self, input_data):
        return self.model.predict(input_data)
    
    def postprocessing(self, input_data):
        try:
            predicted_value = input_data[0]
            return {"predicted_value": predicted_value, "status": "OK"}
        except Exception as e:
            return {"status": "Error", "message": str(e)}


    def compute_prediction(self, input_data):
        try:
            input_data = np.array(input_data).reshape(1, -1)
            prediction = self.model.predict(input_data)
            return {"prediction": prediction[0]}
        except Exception as e:
            return {"error": str(e)}
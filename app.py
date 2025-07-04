from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.logger import logger
from src.exception import CustomException
import sys

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = CustomData(
            glucose=float(request.form["glucose"]),
            blood_pressure=float(request.form["blood_pressure"]),
            skin_thickness=float(request.form["skin_thickness"]),
            insulin=float(request.form["insulin"]),
            bmi=float(request.form["bmi"])
        )
        pred_df = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.predict(pred_df)[0]
        prediction_text = "You are likely to have diabetes." if prediction == 1 else "You are not likely to have diabetes."
        return render_template("home.html", prediction_text=prediction_text)
    except Exception as e:
        logger.error("Error in prediction endpoint")
        raise CustomException(str(e), sys)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
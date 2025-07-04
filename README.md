# Youtube Tutorial : 
# Working demo     : 
---

```markdown
# 🩺 Diabetes Detection System

This is an end-to-end machine learning project that predicts whether a person has diabetes based on health metrics like glucose level, blood pressure, skin thickness, insulin level, and BMI. The project includes data ingestion, preprocessing, model training, and a web app for user input and prediction.

## 📁 Project Structure

```

diabetes\_detection/
├── app.py                           # Flask app entry point
├── Dockerfile                       # Docker container definition
├── requirements.txt                 # Python dependencies
├── src/
│   ├── components/
│   │   ├── data\_ingestion.py        # Load and split dataset
│   │   ├── data\_transformation.py   # Clean and scale features
│   │   └── model\_trainer.py         # Train and save ML model
│   ├── pipeline/
│   │   └── train\_pipeline.py        # Executes entire ML pipeline
│   ├── exception.py                 # Custom exception handler
│   ├── logger.py                    # Logging utility
│   ├── utils.py                     # Utility functions
│   └── setup.py                     # Setup script (if needed)
├── pipeline/
│   └── predict\_pipeline.py          # Prediction logic
├── notebooks/
│   └── diabetes.csv                 # Dataset
├── templates/
│   └── home.html                    # Web form for user input

````

## 🔧 Features

- Clean and validate raw data
- Standardize numeric features using `StandardScaler`
- Train `LogisticRegression` for classification
- Predict outcome using a Flask web interface
- Logs all steps and errors
- Container-ready via Docker

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/diabetes_detection.git
cd diabetes_detection
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the training pipeline

```bash
python src/pipeline/train_pipeline.py
```

This will generate the trained model and scaler under the `artifacts/` directory.

### 4. Run the Flask app

```bash
python app.py
```

Then open your browser at `http://127.0.0.1:5000/`

### 5. (Optional) Run with Docker

```bash
docker build -t diabetes-detector .
docker run -p 5000:5000 diabetes-detector
```

## 🧪 Input Fields for Prediction

* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI

## 📊 Output

* **0** = Non-Diabetic
* **1** = Diabetic

## 📒 Logging

Logs are automatically saved under the `logs/` folder with timestamps.

## ⚠️ Error Handling

All components raise `CustomException` with detailed traceback and source file info.

## 🧠 ML Details

* Model: `LogisticRegression`
* Data: `diabetes.csv` from Kaggle
* Preprocessing: Feature scaling, zero-value filtering, outlier removal

## 📌 Dependencies

* Python ≥ 3.7
* pandas
* numpy
* scikit-learn
* Flask
* gunicorn (for production)
* pickle

(See `requirements.txt` for full list)

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).

## 🙋‍♂️ Author

**Abhishek Sinha**

---

> "Predicting diabetes shouldn't be a mystery — empower early diagnosis through data." 💡

```

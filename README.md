# Demo : 
---

# 🩺 Diabetes Detection ML Project

This project is a complete end-to-end **Machine Learning application** for detecting diabetes based on clinical input parameters. It includes data preprocessing, model training, and a web interface for predictions using Flask.

---

## 📁 Project Structure

```
diabetes_detection/
│
├── notebooks/
│   └── diabetes.csv                      # Raw dataset
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py            # Load & split dataset
│   │   ├── data_transformation.py       # Clean and scale data
│   │   └── model_trainer.py             # Train logistic regression model
│   │
│   ├── pipeline/
│   │   └── train_pipeline.py            # Executes full training pipeline
│   │
│   ├── exception.py                     # Custom exception handling
│   ├── logger.py                        # Logging module
│   ├── utils.py                         # Utility functions
│   └── setup.py                         # Setup script
│
├── pipeline/
│   └── predict_pipeline.py              # Prediction logic
│
├── templates/
│   └── home.html                        # HTML form for web UI
│
├── app.py                               # Flask backend
├── requirements.txt                     # Required dependencies
├── Dockerfile                           # Docker config
└── README.md                            # Project documentation
```

---

## 🧠 Workflow Overview

1. **Data Ingestion**

   * Reads the `diabetes.csv` dataset.
   * Splits into training and testing sets.
   * Saves them in `artifacts/`.

2. **Data Transformation**

   * Filters unrealistic values.
   * Scales selected features (`Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, `BMI`).
   * Saves transformed data and scaler.

3. **Model Training**

   * Trains a `LogisticRegression` model.
   * Saves model to `artifacts/model.pkl`.

4. **Prediction**

   * Accepts user input via Flask UI.
   * Loads saved model and scaler.
   * Returns prediction (Diabetic / Not Diabetic).

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/diabetes_detection.git
cd diabetes_detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the Model

```bash
python src/pipeline/train_pipeline.py
```

This will:

* Ingest and transform the data
* Train the model
* Save the model and scaler into `artifacts/`

### 4. Start the Web App

```bash
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Sample Input on UI

| Feature        | Example Value |
| -------------- | ------------- |
| Glucose        | 148           |
| Blood Pressure | 72            |
| Skin Thickness | 35            |
| Insulin        | 94            |
| BMI            | 33.6          |

---

## 📦 Docker Support (Optional)

You can containerize the app using:

```bash
docker build -t diabetes-app .
docker run -p 5000:5000 diabetes-app
```

---

## 📄 Requirements

Install all necessary packages using:

```
pip install -r requirements.txt
```

---

## 📑 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Abhishek Sinha**

---



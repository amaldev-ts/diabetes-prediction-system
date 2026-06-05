# Diabetes Prediction System

A Machine Learning-based web application that predicts whether a person is likely to have diabetes based on medical parameters.

## Overview

This project uses Machine Learning algorithms to analyze patient health data and predict diabetes risk. The application provides a simple web interface where users can enter medical details and receive prediction results instantly.

## Features

- Diabetes risk prediction
- User-friendly web interface
- Trained Machine Learning model
- Data preprocessing and scaling
- Fast prediction results
- Flask-based deployment

## Technologies Used

- Python
- Flask
- Scikit-Learn
- Pandas
- NumPy
- HTML
- CSS

## Dataset

The model is trained using the Pima Indians Diabetes Dataset.

### Input Parameters

- Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

## Project Structure

```
diabetes-prediction-system/
│
├── static/
├── templates/
├── app.py
├── main.py
├── predict.py
├── train_model.py
├── diabetes.csv
├── diabetes_model.pkl
├── scaler.pkl
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/amaldev-ts/diabetes-prediction-system.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
python app.py
```

4. Open browser

```
http://127.0.0.1:5000
```

## Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Scaling
4. Model Training
5. Model Evaluation
6. Prediction Deployment

## Future Improvements

- Deploy on Render/Streamlit
- Improve prediction accuracy
- Add user authentication
- Store prediction history
- Add advanced analytics dashboard

## Author

**Amal Dev**

Computer Science and Engineering Student

## License

This project is for educational and learning purposes.

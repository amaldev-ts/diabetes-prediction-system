import numpy as np
import pickle

model = pickle.load(open("diabetes_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))


def predict_diabetes():

    print("---- Patient Details ----")

    name = input("Name: ")

    age = float(input("Age: "))

    gender = int(input("Gender (0=Male 1=Female): "))

    print("\n--- Medical Details ---")

    glucose = float(input("Glucose: "))
    bp = float(input("Blood Pressure: "))

    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))

    bmi = weight / (height ** 2)

    if gender == 1:
        preg = float(input("Pregnancies: "))
    else:
        preg = 0

    data = np.array([
        preg,
        glucose,
        bp,
        bmi,
        age,
        gender
    ]).reshape(1, -1)

    data = scaler.transform(data)

    pred = model.predict(data)

    print("\nBMI =", round(bmi, 2))

    if pred[0] == 1:
        print("Result: Diabetic")
    else:
        print("Result: Not Diabetic")
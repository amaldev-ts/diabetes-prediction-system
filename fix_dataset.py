import pandas as pd
import numpy as np

df = pd.read_csv("diabetes.csv")

# remove unwanted columns
df = df.drop([
    "SkinThickness",
    "Insulin",
    "DiabetesPedigreeFunction"
], axis=1)

# add gender column
np.random.seed(0)
df["Gender"] = np.random.randint(0, 2, len(df))

# reorder columns
df = df[[
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "BMI",
    "Age",
    "Gender",
    "Outcome"
]]

df.to_csv("diabetes_new.csv", index=False)

print("New dataset created")
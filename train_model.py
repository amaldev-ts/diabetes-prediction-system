import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


print("Loading dataset...")

df = pd.read_csv("diabetes.csv")

print("Total rows:", len(df))


# -----------------------------
# Features
# -----------------------------

X = df[
    [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "BMI",
        "Age",
        "Gender",
    ]
]

y = df["Outcome"]


# -----------------------------
# Split (use small part if huge)
# -----------------------------

# if dataset very big, use sample

if len(df) > 10000:
    print("Large dataset detected, sampling 10000 rows")
    df = df.sample(10000, random_state=1)

    X = df[
        [
            "Pregnancies",
            "Glucose",
            "BloodPressure",
            "BMI",
            "Age",
            "Gender",
        ]
    ]

    y = df["Outcome"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)


# -----------------------------
# Scale
# -----------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# -----------------------------
# Model (faster solver)
# -----------------------------

model = LogisticRegression(
    max_iter=200,
    solver="liblinear"
)

print("Training model...")

model.fit(X_train, y_train)


# -----------------------------
# Save model
# -----------------------------

pickle.dump(model, open("diabetes_model.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))

print("Model saved")
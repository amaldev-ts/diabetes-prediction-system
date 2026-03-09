from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("diabetes_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))


# ---------------- PAGE 1 ----------------

@app.route("/", methods=["GET", "POST"])
def page1():

    if request.method == "POST":

        name = request.form["name"]
        age = float(request.form["age"])
        gender = int(request.form["gender"])

        return redirect(
            url_for(
                "page2",
                name=name,
                age=age,
                gender=gender
            )
        )

    return render_template("page1.html")


# ---------------- PAGE 2 ----------------

@app.route("/page2")
def page2():

    name = request.args.get("name")
    age = request.args.get("age")
    gender = request.args.get("gender")

    return render_template(
        "page2.html",
        name=name,
        age=age,
        gender=gender
    )


# ---------------- PREDICT ----------------

@app.route("/predict", methods=["POST"])
def predict():

    name = request.form["name"]
    age = float(request.form["age"])
    gender = int(request.form["gender"])

    glucose = float(request.form["glucose"])
    bp = float(request.form["bp"])

    weight = float(request.form["weight"])
    height_cm = float(request.form["height"])

    height = height_cm / 100

    bmi = weight / (height * height)

    if gender == 1:
        preg = float(request.form["preg"])
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

    pred = model.predict(data)[0]

    prob = model.predict_proba(data)[0]

    diabetic_prob = round(prob[1] * 100, 2)
    normal_prob = round(prob[0] * 100, 2)

    result = "Diabetic" if pred == 1 else "Not Diabetic"

    return render_template(
        "result.html",
        name=name,
        bmi=round(bmi, 2),
        result=result,
        dprob=diabetic_prob,
        nprob=normal_prob
    )


# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)
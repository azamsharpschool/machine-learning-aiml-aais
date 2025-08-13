from flask import Flask, render_template, request, redirect, url_for, flash
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("models/linear_regression_sqft_model.joblib")

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/predict")
def predict():
    sqft_str = request.form.get("sqft", "").strip()

    if not sqft_str:
        flash("Please enter square feet.", "error")
        return redirect(url_for("home"))

    try:
        sqft_val = float(sqft_str)
        if sqft_val <= 0:
            raise ValueError("Invalid sqft")
    except Exception:
        flash("Square feet must be a positive number.", "error")
        return redirect(url_for("home"))

    price = model.predict(np.array([[sqft_val]]))[0]

    return render_template("result.html", sqft=int(sqft_val), price=round(price, 2))

if __name__ == "__main__":
    app.run(debug=True)

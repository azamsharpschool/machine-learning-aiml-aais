from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load your saved pipeline (preprocessor + RandomForestRegressor)
model = joblib.load("model_pipeline.pkl")

# These are the features your model was trained on
FEATURE_COLUMNS = [
    "Area",
    "Age",
    "Location",
    "Condition",
    "Garage",
    "Bedrooms",
    "Bathrooms",
    "Floors"
]


CURRENT_YEAR = 2025  # same as in your notebook

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    form_data = {}

    if request.method == "POST":
        # Read form inputs
        area = float(request.form.get("area", 0))
        year_built = int(request.form.get("year_built", 2000))
        location = request.form.get("location", "")
        condition = request.form.get("condition", "")
        garage = request.form.get("garage", "")
        bedrooms = int(request.form.get("bedrooms", 0))
        bathrooms = int(request.form.get("bathrooms", 0))
        floors = int(request.form.get("floors", 1))


        # Compute Age exactly like the notebook: Age = 2025 - YearBuilt
        age = CURRENT_YEAR - year_built

        # Save for redisplay in form
        form_data = {
            "area": area,
            "year_built": year_built,
            "location": location,
            "condition": condition,
            "garage": garage,
            "bedrooms": bedrooms, 
            "bathrooms": bathrooms, 
            "floors": floors
        }

        # Create DataFrame in the same shape as training data
        input_df = pd.DataFrame([{
            "Area": area,
            "Age": age,
            "Location": location,
            "Condition": condition,
            "Garage": garage, 
            "Bedrooms": bedrooms, 
            "Bathrooms": bathrooms, 
            "Floors": floors
            
        }], columns=FEATURE_COLUMNS)

        # Predict using the pipeline
        y_pred = model.predict(input_df)[0]
        prediction = round(float(y_pred), 2)

    return render_template("index.html", prediction=prediction, form_data=form_data)


if __name__ == "__main__":
    app.run(debug=True)

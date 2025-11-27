from flask import Flask, render_template, request
import pandas as pd  
import joblib

model = joblib.load("model_pipeline.pkl")

app = Flask(__name__)

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

@app.route("/", methods=["GET", "POST"])
def index(): 

    prediction = None 

    if request.method == "POST": 
        area = int(request.form.get("area"), 0)
        year_built = int(request.form.get("year_built"), 0)
        location = request.form.get("location", "")
        condition = request.form.get("condition", "")
        garage = request.form.get("garage", "")
        bedrooms = int(request.form.get("bedrooms", 0))
        bathrooms = int(request.form.get("bathrooms", 0))
        floors = int(request.form.get("floors", 1))

        age = 2025 - year_built

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

        # create data frame 
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

        # predict 
        y_pred = model.predict(input_df)[0]
        prediction =  round(float(y_pred), 2)
        print(prediction)

    return render_template("index.html", prediction=prediction, form_data=form_data)





if __name__ == "__main__":
    app.run(debug=True)
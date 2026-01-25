
from flask import render_template, request, Flask
import numpy as np 
import pandas as pd 
import joblib 

app = Flask(__name__)
app.debug = True  # Enables auto-reloading

# load the model 
model = joblib.load("customer_purchase_model.joblib")
# load the scaler settings from joblib 
scaler = joblib.load("scaler.joblib")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict(): 
    age = int(request.form["age"])
    salary = int(request.form["salary"])

    input_data = pd.DataFrame([[age, salary]], columns=["Age", "EstimatedSalary"])
    # standardize it 
    input_scaled = scaler.transform(input_data)
    print(input_scaled)

    prediction = model.predict(input_scaled)[0]
    print(prediction)

    return render_template("result.html", age=age, salary=salary, purchased=bool(prediction))

from flask import Flask, render_template, abort 
import sqlite3 
import joblib 
import numpy as np 

app = Flask(__name__)

MODEL_PATH = "breast_cancer_model.joblib"
DATABASE_PATH = "breast_cancer.db"

model = joblib.load(MODEL_PATH)

# Columns in the measurements table (for SQL)
measurement_columns = """
    patient_id,
    mean_radius, mean_texture, mean_perimeter, mean_area,
    mean_smoothness, mean_compactness, mean_concavity, mean_concave_points,
    mean_symmetry, mean_fractal_dimension,
    radius_error, texture_error, perimeter_error, area_error,
    smoothness_error, compactness_error, concavity_error, concave_points_error,
    symmetry_error, fractal_dimension_error,
    worst_radius, worst_texture, worst_perimeter, worst_area,
    worst_smoothness, worst_compactness, worst_concavity, worst_concave_points,
    worst_symmetry, worst_fractal_dimension
"""


def get_db_connection(): 
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row # rows behave like dictionary 
    return conn 

@app.route("/")
def patients(): 
    conn = get_db_connection() 
    rows = conn.execute("SELECT patient_id, first_name, last_name, age FROM patients;").fetchall() 
    conn.close() 
    # pass the rows (patients) to a page where we can display all patients 
    return render_template("index.html", patients=rows)

@app.route("/patients/<int:patient_id>")
def patient_detail(patient_id): 

    conn = get_db_connection() 
    patient = conn.execute("SELECT patient_id, first_name, last_name, age FROM patients WHERE patient_id = ?",(patient_id,)).fetchone()

    if patient is None: 
        conn.close() 
        abort(404)

    # get measurement information from database 
    query = f"""
        SELECT {measurement_columns} FROM breast_cancer_measurements 
        WHERE patient_id = ?
    """

    measurement = conn.execute(query, (patient_id, )).fetchone() 
    conn.close() 

    prediction_label = None 
    prediction_proba = None 

    if measurement is not None: 
        features = [
            measurement["mean_radius"],
            measurement["mean_texture"],
            measurement["mean_perimeter"],
            measurement["mean_area"],
            measurement["mean_smoothness"],
            measurement["mean_compactness"],
            measurement["mean_concavity"],
            measurement["mean_concave_points"],
            measurement["mean_symmetry"],
            measurement["mean_fractal_dimension"],
            measurement["radius_error"],
            measurement["texture_error"],
            measurement["perimeter_error"],
            measurement["area_error"],
            measurement["smoothness_error"],
            measurement["compactness_error"],
            measurement["concavity_error"],
            measurement["concave_points_error"],
            measurement["symmetry_error"],
            measurement["fractal_dimension_error"],
            measurement["worst_radius"],
            measurement["worst_texture"],
            measurement["worst_perimeter"],
            measurement["worst_area"],
            measurement["worst_smoothness"],
            measurement["worst_compactness"],
            measurement["worst_concavity"],
            measurement["worst_concave_points"],
            measurement["worst_symmetry"],
            measurement["worst_fractal_dimension"],
        ]

        X = np.array(features, dtype=float).reshape(1, -1)
        y_pred = model.predict(X)
        
        label_map = {
            0: "Malignant", 
            1: "Beign"
        }

        class_id = int(y_pred[0])
        prediction_label = label_map.get(class_id, str(class_id))
        print(prediction_label)


    return render_template("patient_detail.html", patient=patient,
                            measurement=measurement, prediction_label=prediction_label)

if __name__ == "__main__":
    app.run(debug=True)
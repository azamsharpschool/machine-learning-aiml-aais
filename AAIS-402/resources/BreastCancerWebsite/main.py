from flask import Flask, render_template, abort
import sqlite3
import numpy as np
import joblib

app = Flask(__name__)

# ====== Load model and scaler once at startup ======
MODEL_PATH = "breast_cancer_model.joblib"
SCALER_PATH = "breast_cancer_scaler.joblib"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def get_db_connection():
    conn = sqlite3.connect("breast_cancer_data.db")
    conn.row_factory = sqlite3.Row  # rows behave like dicts
    return conn

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

@app.route("/")
def patients():
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT patient_id, first_name, last_name, age FROM patients"
    ).fetchall()
    conn.close()
    return render_template("index.html", patients=rows)

@app.route("/patients/<int:patient_id>")
def patient_detail(patient_id):
    conn = get_db_connection()

    # ---- 1. Get basic patient info ----
    patient = conn.execute(
        "SELECT patient_id, first_name, last_name, age FROM patients WHERE patient_id = ?",
        (patient_id,)
    ).fetchone()

    if patient is None:
        conn.close()
        abort(404)

    # ---- 2. Get measurements for this patient ----
    query = f"""
        SELECT {measurement_columns}
        FROM breast_cancer_measurements
        WHERE patient_id = ?
    """
    measurement = conn.execute(query, (patient_id,)).fetchone()
    conn.close()

    prediction_label = None
    prediction_proba = None

    if measurement is not None:
        # ---- 3. Build feature vector in the SAME ORDER used for training ----
        # Typically these are the 30 numeric features from the dataset
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

        # ---- 4. Scale the features ----
        X_scaled = scaler.transform(X)

        # ---- 5. Predict with the model ----
        y_pred = model.predict(X_scaled)             # class (e.g., 0/1)
        y_proba = model.predict_proba(X_scaled)      # probabilities

        # If you used sklearn breast cancer dataset, usually:
        # 0 = malignant, 1 = benign. Adjust mapping if needed.
        label_map = {
            0: "Malignant",
            1: "Benign"
        }
        class_id = int(y_pred[0])
        prediction_label = label_map.get(class_id, str(class_id))
        prediction_proba = float(max(y_proba[0]))    # highest class probability

    return render_template(
        "patient_detail.html",
        patient=patient,
        measurement=measurement,
        prediction_label=prediction_label,
        prediction_proba=prediction_proba,
    )

if __name__ == "__main__":
    app.run(debug=True)

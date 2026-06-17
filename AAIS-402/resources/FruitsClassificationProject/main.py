import os
from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

app = Flask(__name__)

# Where uploaded images will be stored
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

img_size = (224, 224)
class_names = ['Apple', 'Banana', 'Grape', 'Mango', 'Strawberry']

# Load model once at startup (MUCH faster)
model = tf.keras.models.load_model("fruits_classifier.keras")


def predict_image(img_path):
    img = tf.keras.utils.load_img(img_path, target_size=img_size)
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)   # shape: (1, 224, 224, 3)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    class_id = np.argmax(score)
    class_name = class_names[class_id]
    confidence = 100 * np.max(score)

    return class_name, confidence


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    image_url = None

    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"

        file = request.files["file"]

        if file.filename == "":
            return "No selected file"

        # Save uploaded image
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # Run prediction
        prediction, confidence = predict_image(filepath)

        # Path for HTML to display image
        image_url = filepath

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        image_url=image_url
    )


if __name__ == "__main__":
    app.run(debug=True)

Absolutely! Here's a **detailed walkthrough** of the complete pipeline you’re building: a **CNN-based Bone Fracture Detector using X-ray images**, without using `ImageDataGenerator`.

---

# 🦴 Bone Fracture Detection from X-Ray Images (Step-by-Step Walkthrough)

---

## 🔧 Goal

To build a **Convolutional Neural Network (CNN)** in TensorFlow/Keras that can:

* Take in an X-ray image
* Predict if it shows a **fracture** or **normal bone**

We'll load and preprocess the data **manually** using `image_dataset_from_directory`, train the model, and make predictions.

---

## 📁 Step 1: Organize the Dataset

Organize your dataset in this structure:

```
dataset/
├── fracture/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── normal/
    ├── image1.jpg
    ├── image2.jpg
    └── ...
```

Each folder contains X-ray images corresponding to that class.

---

## 📦 Step 2: Install Requirements

If you're running locally or in a Colab notebook:

```bash
pip install tensorflow matplotlib
```

---

## 🧼 Step 3: Load and Preprocess the Data

We'll use `image_dataset_from_directory` to automatically:

* Read images
* Assign labels (`fracture` = 0, `normal` = 1)
* Resize images
* Batch the data
* Split into training and validation sets

```python
import tensorflow as tf

train_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset",
    labels="inferred",
    label_mode="binary",
    image_size=(150, 150),
    batch_size=32,
    validation_split=0.2,
    subset="training",
    seed=123
)

val_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset",
    labels="inferred",
    label_mode="binary",
    image_size=(150, 150),
    batch_size=32,
    validation_split=0.2,
    subset="validation",
    seed=123
)
```

---

## ✨ Step 4: Normalize the Images

Images have pixel values between 0–255. We'll normalize them to 0–1 using a `Rescaling` layer:

```python
from tensorflow.keras.layers import Rescaling

normalization_layer = Rescaling(1./255)

train_dataset = train_dataset.map(lambda x, y: (normalization_layer(x), y))
val_dataset = val_dataset.map(lambda x, y: (normalization_layer(x), y))
```

---

## 🧠 Step 5: Build the CNN Model

Now we build a CNN from scratch using Keras’ `Sequential` model:

```python
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

model = Sequential([
    Conv2D(32, (3, 3), activation="relu", input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),

    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D(2, 2),

    Conv2D(128, (3, 3), activation="relu"),
    MaxPooling2D(2, 2),

    Flatten(),
    Dropout(0.5),
    Dense(64, activation="relu"),
    Dense(1, activation="sigmoid")  # binary classification
])
```

---

## ⚙️ Step 6: Compile the Model

Use Adam optimizer and binary crossentropy loss (because we have two classes):

```python
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
```

---

## 🚂 Step 7: Train the Model

This will begin training your CNN:

```python
model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=10
)
```

You’ll see loss/accuracy metrics for both training and validation datasets per epoch.

---

## 🧪 Step 8: Evaluate the Model on Test Data (Optional)

If you have a separate test set:

```
test/
├── fracture/
└── normal/
```

You can load it the same way:

```python
test_dataset = tf.keras.utils.image_dataset_from_directory(
    "test",
    labels="inferred",
    label_mode="binary",
    image_size=(150, 150),
    batch_size=32
)

test_dataset = test_dataset.map(lambda x, y: (normalization_layer(x), y))

model.evaluate(test_dataset)
```

---

## 🔍 Step 9: Make Predictions on a Single X-ray Image

Here’s how to load an image and predict:

```python
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np

def predict_image(image_path):
    img = load_img(image_path, target_size=(150, 150))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # add batch dimension

    prediction = model.predict(img_array)
    print("Prediction:", "Fracture" if prediction[0][0] > 0.5 else "Normal")

# Example usage
predict_image("example_xray.jpg")
```

---

## 💾 Optional: Save the Trained Model

You can export your model for later use:

```python
model.save("fracture_detector_model.h5")
```

And load it later like this:

```python
from tensorflow.keras.models import load_model
model = load_model("fracture_detector_model.h5")
```

---

## ✅ Summary

| Step         | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| 📁 Dataset   | Organized into `fracture` and `normal` folders               |
| 📥 Load      | Used `image_dataset_from_directory` to load and label images |
| 🔄 Normalize | Used `Rescaling(1./255)` to normalize pixels                 |
| 🧠 Model     | Built a CNN using 3 Conv layers + Dense layers               |
| 🧪 Predict   | Loaded image and used `model.predict()`                      |
| 💾 Save      | Used `model.save()` to export trained model                  |

---

Would you like this as a **Google Colab notebook**, **PDF guide**, or both?

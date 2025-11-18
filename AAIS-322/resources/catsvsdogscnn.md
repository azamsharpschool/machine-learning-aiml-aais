import os
import numpy as np
from skimage.io import imread
from skimage.transform import resize
import matplotlib.pyplot as plt

# TensorFlow model tools
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras import layers, models

# -----------------------------
# 1. Load pictures (cats & dogs)
# -----------------------------
DATA_DIR = "data"
CATEGORIES = ["cats", "dogs"]
IMG_SIZE = (224, 224)   # Size the premade model wants

X = []   # will hold the pictures
y = []   # will hold the labels (0 = cat, 1 = dog)

for label, category in enumerate(CATEGORIES):
    folder = os.path.join(DATA_DIR, category)
    for file in os.listdir(folder):
        if not file.lower().endswith((".jpg", ".png", ".jpeg")):
            continue

        img = imread(os.path.join(folder, file))
        img = resize(img, IMG_SIZE)
        
        # Make sure image has 3 color channels
        if img.ndim == 2:
            img = np.stack([img, img, img], axis=-1)
        elif img.shape[2] > 3:
            img = img[:, :, :3]
        
        X.append(img)
        y.append(label)

X = np.array(X, dtype=np.float32)
y = np.array(y)

# The model expects special preprocessing
X = preprocess_input(X)

# -----------------------------
# 2. Split into training/testing
# -----------------------------
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 3. Load the premade model
# -----------------------------
base_model = MobileNetV2(
    weights="imagenet",      # already trained
    include_top=False,       # remove old classifier
    input_shape=(224, 224, 3)
)

base_model.trainable = False   # freeze the premade part

# -----------------------------
# 4. Add our simple classifier
# -----------------------------
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(1, activation="sigmoid")   # cat or dog
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# -----------------------------
# 5. Train the model
# -----------------------------
history = model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=5
)

# -----------------------------
# 6. Predict a new image
# -----------------------------
def predict_image(path):
    img = imread(path)
    img = resize(img, IMG_SIZE)
    
    if img.ndim == 2:
        img = np.stack([img, img, img], axis=-1)
    elif img.shape[2] > 3:
        img = img[:, :, :3]
    
    img_prep = preprocess_input(img.astype(np.float32))
    pred = model.predict(np.expand_dims(img_prep, 0))[0, 0]
    
    label = "dog" if pred > 0.5 else "cat"
    print("Prediction:", label)
    
    plt.imshow(img)
    plt.title(label)
    plt.axis("off")
    plt.show()

# Try predicting:
# predict_image("my_dog.jpg")

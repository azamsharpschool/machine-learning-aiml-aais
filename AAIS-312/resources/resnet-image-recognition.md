
# 🧠 Walkthrough: Image Classification with ResNet50 (ImageNet)

## 🎯 What you’ll learn

* Load a **pretrained ResNet50** model
* Prepare an image in the **exact format** the model expects
* Run inference and get **top‑k** (and **top‑1**) predictions
* Understand shapes like `(None, 224, 224, 3)` and what **parameters** mean
* Avoid common pitfalls (extra batch dims, missing preprocessing, size mismatches)

---

## 📦 Prerequisites

* Python, TensorFlow/Keras installed
* A JPEG/PNG image you want to classify (we’ll call it `your_image.jpg`)

---

## 🪜 Step‑by‑Step Guide

### ✅ Step 1: Imports — the essentials

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
```

**Why these:**

* **NumPy**: array math
* **TensorFlow/Keras**: model + utilities
* **`ResNet50`**: the pretrained network
* **`preprocess_input`**: makes pixels match ResNet50’s training format
* **`decode_predictions`**: converts logits to readable labels
* **`image`**: load/convert a PIL image
* **Matplotlib**: quick visual check

---

### 🧠 Step 2: Load the pretrained model

```python
model = ResNet50(weights="imagenet")  # include_top=True by default
```

**What you get:**

* Input shape: **(None, 224, 224, 3)**

  * `None` = flexible **batch size**
* Output shape: **(None, 1000)** (scores for 1,000 ImageNet classes)
* The final layer is `predictions (Dense)` with **1000** units

---

### 🖼️ Step 3: Load and display an image

```python
img = image.load_img("your_image.jpg", target_size=(224, 224))
plt.imshow(img)
plt.axis('off'); plt.show()
```

* `target_size=(224, 224)` ensures the image matches ResNet50’s expected size

---

### 🧪 Step 4: Convert, preprocess, and predict

```python
img_array = image.img_to_array(img)                     # (224, 224, 3)
x = np.expand_dims(img_array, axis=0)                   # (1, 224, 224, 3) add batch dim
x = preprocess_input(x)                                 # ResNet50-specific normalization

preds = model.predict(x)                                # (1, 1000)
top3 = decode_predictions(preds, top=3)[0]
print(top3)
```

**What `preprocess_input` does (for ResNet50):**

* Converts **RGB → BGR**
* Subtracts **ImageNet mean** per channel
  This is crucial—skip it and accuracy drops.

---

### 🥇 Step 5: Get only the highest prediction (Top‑1)

**Option A — via `decode_predictions`:**

```python
best = decode_predictions(preds, top=1)[0][0]
# ('n02504458', 'African_elephant', 0.876)
print(best)
```

**Option B — manual argmax + readable label:**

```python
class_idx = np.argmax(preds)
score = preds[0, class_idx]
label = decode_predictions(preds, top=1)[0][0][1]
print(f"Top-1: {label} ({score:.2%})")
```

---

## 🔍 Understanding shapes & parameters (quick clarity)

* **`(None, 224, 224, 3)`**:
  “A batch (size = None, flexible) of 224×224 RGB images.”

* **Parameters** (weights + biases):
  Think of them as the model’s **knobs**—numbers learned during training.
  ResNet50 has \~**25.6M** parameters. Most are **trainable**; a tiny portion are **non‑trainable** (e.g., running stats in batch norm).

---

## 🧯 Common pitfalls (and fast fixes)

* **Extra batch dimension**
  Error shows shape like `(1, 1, 224, 224, 3)`?
  You added a batch dim twice. Fix:

  ```python
  x = np.squeeze(x, axis=1)  # -> (1, 224, 224, 3)
  ```

* **Skipped preprocessing**
  Always call `preprocess_input(x)` **after** adding the batch dim.

* **Wrong image size**
  Use `target_size=(224, 224)` when loading or resize manually.

* **Color confusion (OpenCV users)**
  OpenCV loads **BGR**; if you’re not using `preprocess_input`, convert to RGB first.
  With `preprocess_input` from `resnet50`, it handles BGR/means for you.

---

## 🚀 Bonus: Use ResNet50 as a feature extractor (transfer learning)

If you’re building your **own classifier** (e.g., cats vs dogs), drop the 1000‑class head and add your layers:

```python
from tensorflow.keras import layers, models

base = ResNet50(weights="imagenet", include_top=False, input_shape=(224, 224, 3))
base.trainable = False  # freeze base for feature extraction

model = models.Sequential([
    base,
    layers.GlobalAveragePooling2D(),
    layers.Dense(1, activation="sigmoid")  # binary; use units=K for K classes + softmax
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
```

Later, **fine‑tune** a few top layers:

```python
base.trainable = True
for layer in base.layers[:-20]:
    layer.trainable = False

model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-5),
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
```

---

## 🧾 Minimal end‑to‑end script (copy–paste ready)

```python
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Load model
model = ResNet50(weights="imagenet")

# Load & prepare image
img = image.load_img("your_image.jpg", target_size=(224, 224))
x = image.img_to_array(img)                 # (224, 224, 3)
x = np.expand_dims(x, axis=0)               # (1, 224, 224, 3)
x = preprocess_input(x)                     # normalize for ResNet50

# Predict
preds = model.predict(x)

# Top-3 and Top-1
print("Top-3:", decode_predictions(preds, top=3)[0])
best = decode_predictions(preds, top=1)[0][0]
print(f"Top-1: {best[1]} ({best[2]:.2%})")
```

---

## 🧠 Key takeaways

* ResNet50 expects **(batch, 224, 224, 3)** and **preprocessed** inputs.
* `decode_predictions` turns logits into **readable labels**.
* “**None**” in shapes = **variable batch size**.
* Parameters are the model’s learned **knobs**; ResNet50 has \~25.6M of them.
* For your own tasks, use **transfer learning**: `include_top=False`, add your head, then fine‑tune.


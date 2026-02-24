
# 🍑🍓 **Deep Learning Fruit Classifier – Full Walkthrough (Keras + Python)**

Dataset: https://www.kaggle.com/datasets/alihasnainch/fruits-dataset-for-classification

[Download Code](FruitsClassificationProject.zip)


Your dataset contains 6 folders:

```
dataset/
    fresh_peaches_done/
    fresh_pomegranates_done/
    fresh_strawberries_done/
    rotten_peaches_done/
    rotten_pomegranates_done/
    rotten_strawberries_done/
```

Each folder represents **one class**, and Keras can automatically label these for you.

---

# 1️⃣ **Dataset Structure & Why It Works**

Keras has a helper function:

```python
tf.keras.utils.image_dataset_from_directory()
```

This function:

* Reads all subfolders inside a directory
* Assigns a label to each folder automatically (0, 1, 2, …)
* Loads the images resized to whatever shape you want
* Builds efficient training batches for you

It removes all the boilerplate of writing your own image loaders.

---

# 2️⃣ **Loading the Dataset (with Auto Train/Validation Split)**

### Code:

```python
import tensorflow as tf
from tensorflow.keras import layers, models

data_dir = "dataset"   # folder containing your 6 class folders
img_size = (180, 180)  # all images will be resized to this
batch_size = 32
```

### Creating the training set:

```python
train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,   # reserve 20% for validation
    subset="training",
    seed=42,
    image_size=img_size,
    batch_size=batch_size
)
```

### Creating the validation set:

```python
val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=img_size,
    batch_size=batch_size
)
```

### Why this works:

* You only need **one directory** (`dataset/`).
* Keras automatically splits the images:

  * 80% training
  * 20% validation
* **The split is consistent** because of `seed=42`.

---

# 3️⃣ **Understanding Class Names**

Keras reads your folder names and creates:

```python
class_names = train_ds.class_names
```

In your case:

```
['fresh_peaches_done',
 'fresh_pomegranates_done',
 'fresh_strawberries_done',
 'rotten_peaches_done',
 'rotten_pomegranates_done',
 'rotten_strawberries_done']
```

These become your model’s output labels.

---

# 4️⃣ **Building a Simple CNN Model**

This is your classifier:

```python
model = models.Sequential([
    layers.Rescaling(1./255, input_shape=img_size + (3,)),  # normalize pixels

    layers.Conv2D(16, 3, activation='relu'),
    layers.MaxPooling2D(),

    layers.Conv2D(32, 3, activation='relu'),
    layers.MaxPooling2D(),

    layers.Conv2D(64, 3, activation='relu'),
    layers.MaxPooling2D(),

    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(num_classes, activation='softmax'),
])
```

### What each layer does:

| Layer                  | Purpose                                        |
| ---------------------- | ---------------------------------------------- |
| **Rescaling**          | Normalize image pixels (0–255 → 0–1)           |
| **Conv2D**             | Learn patterns like colors, shapes, edges      |
| **MaxPooling**         | Downsample images (reduces size + overfitting) |
| **Flatten**            | Convert 2D feature maps → 1D vector            |
| **Dense(64)**          | Learn complex combinations of features         |
| **Dense(num_classes)** | Output probabilities for 6 fruit classes       |

---

# 5️⃣ **Compiling the Model**

```python
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)
```

### Meaning:

* **Adam** → fast, adaptive optimizer widely used in deep learning
* **Sparse categorical crossentropy** → correct loss for integer labels (0–5)
* **Accuracy** → track how often predictions match labels

---

# 6️⃣ **Training the Model**

```python
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=5
)
```

### What happens during training:

* **Epoch** = one full pass through the entire dataset
* At each epoch, Keras prints:

  * loss (how wrong the model is)
  * accuracy (how often it’s right)
  * validation loss (how wrong on unseen data)
  * validation accuracy (performance on unseen data)

Validation accuracy tells you if your model is generalizing well.

---

# 7️⃣ **Saving the Model**

```python
model.save("fruit_classifier.keras")
```

This saves:

* Model architecture
* Trained weights
* Optimizer state
* Class labels order

You can load it anytime.

---

# 8️⃣ **Predicting a New Image**

Now let's classify a new image.

### Load the model:

```python
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("fruit_classifier.keras")
```

### Your class names (same as training):

```python
class_names = [
    'fresh_peaches_done',
    'fresh_pomegranates_done',
    'fresh_strawberries_done',
    'rotten_peaches_done',
    'rotten_pomegranates_done',
    'rotten_strawberries_done'
]
```

### Prediction function:

```python
def predict_image(img_path):
    img = tf.keras.utils.load_img(img_path, target_size=(180, 180))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # (1, 180, 180, 3)
    
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    
    class_id = np.argmax(score)
    class_name = class_names[class_id]
    confidence = 100 * np.max(score)
    
    print(f"Predicted: {class_name} ({confidence:.2f}% confidence)")
```

### Use it:

```python
predict_image("/content/test_peach.jpg")
```

Output example:

```
1/1 ━━━━━━━━━━━━━━━━━━━ 0s 18ms/step
Predicted: rotten_peaches_done (97.22% confidence)
```

---

# 9️⃣ **Training vs. Validation Explained**

| Concept             | Meaning                                                              |
| ------------------- | -------------------------------------------------------------------- |
| **Training data**   | Model learns from this                                               |
| **Validation data** | Model NEVER sees this during learning; it's used ONLY for evaluation |
| **Overfitting**     | Model memorizes training examples but fails on new ones              |
| **Generalization**  | Ability to perform well on unseen data (goal!)                       |

If:

* **Training accuracy goes up**
* But **validation accuracy stays flat or goes down**

→ The model is overfitting.

You can reduce overfitting by:

* More data
* Data augmentation
* Dropout layers
* Smaller model

But your dataset is good-sized (1655 images), so this simple model should already learn well.

---

# 🔟 **Summary of the Process**

### ✔ Load images automatically

### ✔ Split into training / validation

### ✔ Build a simple CNN

### ✔ Train for a few epochs

### ✔ Save the model

### ✔ Predict new fruit images

You now have a full deep-learning image classifier pipeline.



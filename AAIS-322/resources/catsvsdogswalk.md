
# 🐱🐶 Cats vs Dogs Classifier — Full Walkthrough

This notebook builds a **simple image classifier** that distinguishes cats from dogs using **Logistic Regression** from scikit-learn.
Although logistic regression is not normally used for images, this example shows the full ML pipeline:

1. Load images
2. Preprocess
3. Flatten
4. Train
5. Evaluate
6. Make predictions on new images

Let’s walk through each part step-by-step.

---

# 1️⃣ Import Libraries

```python
import os 
from skimage.io import imread
from skimage.transform import resize
```

### ✔ What each library does:

* `os` — used to list files in directories.
* `skimage.io.imread` — loads an image into a NumPy array.
* `skimage.transform.resize` — resizes images to a consistent resolution.

**Why resizing?**
Machine learning models require all input vectors to have **the same size**.
Your model uses **64×64 grayscale** images.

---

# 2️⃣ Load Images and Build X and y

```python
X = [] 
y = [] 

for category in ["cats", "dogs"]: 
    folder = os.path.join("data", category)
    
    for file in os.listdir(folder):
        img_path = os.path.join(folder, file)
        img = imread(img_path)           # read the image
        img = resize(img, (64, 64))      # resize to 64×64
        img = img[:, :, 0]               # convert to grayscale (use 1 channel)
        
        X.append(img.flatten())          # flatten to vector length 4096
        y.append(category)
```

### ✔ What this section does

* Loops through two folders:

  ```
  data/cats/
  data/dogs/
  ```
* For each image:

  * Loads the image
  * Resizes it to 64×64
  * Converts to grayscale by selecting channel 0
  * Flattens it into a **1D array of length 4096**
  * Stores it in `X`
* Adds the label `"cats"` or `"dogs"` to `y`

### ✔ Why flatten?

Models like logistic regression require 1D feature vectors:

`64 × 64 = 4096 values per image`

---

# 3️⃣ Split into Train and Test Sets

```python
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)
```

### ✔ What this does

* Splits the dataset:

  * **80%** for training
  * **20%** for testing
* Ensures we can evaluate on unseen images

---

# 4️⃣ Train the Logistic Regression Model

```python
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(max_iter=8000) 
clf.fit(X_train, y_train)
```

### ✔ Why `max_iter=8000`?

Flattened images create **4096 features**, which is large for logistic regression.
The algorithm needs more iterations to converge.

### ✔ What the model learns?

It tries to find a linear boundary in 4096-dimensional space that separates:

* cats
* dogs

This is very simple compared to CNNs, but good for educational purposes.

---

# 5️⃣ Evaluate the Model

```python
clf.score(X_test, y_test)
```

This returns the **accuracy** on unseen test images.

---

# 6️⃣ Visualize Sample Images

```python
import matplotlib.pyplot as plt 

for index in range(0, 10):
    plt.subplot(2, 5, index + 1)
    plt.imshow(X_test[index].reshape(64,64), cmap='gray')
    plt.axis("off")

plt.show()
```

### ✔ What this does

* Displays the first 10 test images
* Reshapes vector 4096 → 64×64
* Shows them in grayscale
* Useful for visual inspection

---

# 7️⃣ Process a New Image for Prediction

```python
import numpy as np 

IMG_SIZE = (64, 64)

def preprocess_image(path):
    img = imread(path)
    img = resize(img, IMG_SIZE)
    img = img[:, :, 0]                     # grayscale
    return img.flatten().astype(np.float32)
```

### ✔ Why this function is needed?

To classify *any new image*:

* Load it
* Resize to 64×64
* Grayscale
* Flatten
* Convert to float

The preprocessed vector matches the format used for training.

---

# 8️⃣ Predict a New Image

```python
x_new = preprocess_image("cat.png").reshape(1, -1)  # (1, 4096)
pred_label = clf.predict(x_new)[0]
print(pred_label)
```

### ✔ Steps happening here

1. Preprocess image → vector shape (4096,)
2. Reshape to (1, 4096) because scikit-learn expects batches
3. Use the trained model to predict
4. Prints `"cats"` or `"dogs"`

---

# 🎉 Final Summary

✔ Loads and preprocesses cat/dog images
✔ Converts them to grayscale 64×64
✔ Flattens images into 4096-pixel vectors
✔ Uses logistic regression for classification
✔ Evaluates accuracy
✔ Displays sample images
✔ Predicts new images with preprocessing



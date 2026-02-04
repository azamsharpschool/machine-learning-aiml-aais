
## What this notebook does (big picture)

You are building a **cats vs dogs image classifier** using:

* Basic image processing
* A simple machine learning model (Logistic Regression)
* Python + scikit-learn

At a high level, the steps are:

1. Load images from disk
2. Convert images into numbers the computer can understand
3. Train a model to recognize cats vs dogs
4. Test how well the model performs
5. Predict the label of a brand new image

---

## Step 1: Import required libraries

```python
import os 
from skimage.io import imread
from skimage.transform import resize
```

### What’s happening here?

* `os`
  Used to **navigate folders and files** on your computer.

* `imread`
  Reads an image file (PNG, JPG, etc.) and converts it into a **NumPy array** of pixel values.

* `resize`
  Forces all images to be the **same size**, which is critical for machine learning.

Why resizing matters:
ML models require **fixed-length inputs**. A 300×300 image and a 100×100 image cannot be fed into the same model unless they are resized to the same dimensions.

---

## Step 2: Quick sanity check

```python
print("testing...")
```

This is just a quick check to confirm the notebook cell runs correctly. Nothing ML-related here.

---

## Step 3: Load and preprocess training images

```python
X = [] 
y = [] 

for category in ["cats", "dogs"]: 
    for filename in os.listdir(f"train/{category}"): 
        img = imread(os.path.join(f"train/{category}", filename), as_gray=True) 
        img = resize(img, (64, 64)) 
        X.append(img.flatten()) 
        y.append(category)
```

This is the **most important block in the notebook**.

### Folder structure expectation

Your dataset should look like this:

```
train/
  cats/
    cat1.jpg
    cat2.jpg
  dogs/
    dog1.jpg
    dog2.jpg
```

### Line-by-line explanation

* `X = []`
  Will store **image data (features)**

* `y = []`
  Will store **labels** (`"cats"` or `"dogs"`)

---

### Looping through categories

```python
for category in ["cats", "dogs"]:
```

This lets you:

* Automatically label images
* Avoid writing separate code for cats and dogs

---

### Reading each image

```python
img = imread(path, as_gray=True)
```

* Converts image to **grayscale**
* Grayscale = 1 value per pixel instead of 3 (RGB)
* Simpler and faster for beginners

---

### Resizing images

```python
img = resize(img, (64, 64))
```

Every image becomes **64 × 64 pixels**, no matter the original size.

That gives:

```
64 × 64 = 4096 pixels
```

---

### Flattening the image

```python
img.flatten()
```

Transforms:

```
64 x 64 image
↓
1D array of length 4096
```

Why?
Logistic Regression expects **rows of numbers**, not 2D images.

---

### Storing data

```python
X.append(img.flatten())
y.append(category)
```

* `X`: numerical image data
* `y`: corresponding label

At the end:

* `X` → list of image feature vectors
* `y` → list of `"cats"` or `"dogs"`

---

## Step 4: Inspect the data

```python
print(X)
print(y)
```

This is just for **debugging and understanding**:

* `X` should be a list of long numeric arrays
* `y` should look like:

  ```python
  ['cats', 'cats', 'dogs', 'dogs', ...]
  ```

---

## Step 5: Split data into training and testing sets

```python
from sklearn.model_selection import train_test_split 

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)
```

### Why do we do this?

* **Training set** → model learns from this
* **Test set** → model is evaluated on unseen data

`test_size=0.2` means:

* 80% training data
* 20% testing data

This prevents the model from just memorizing images.

---

## Step 6: Train the model

```python
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(max_iter=8000) 
clf.fit(X_train, y_train)
```

### What is Logistic Regression?

Despite the name, it is a **classification algorithm**, not regression.

It learns:

> “Given these pixel values, how likely is this image a cat or a dog?”

### Why `max_iter=8000`?

* Image data is large (4096 features)
* Logistic Regression may need more iterations to converge

---

## Step 7: Evaluate accuracy

```python
clf.score(X_test, y_test)
```

This returns a value like:

```
0.72
```

Which means:

> The model correctly classified 72% of test images

---

## Step 8: See raw predictions

```python
clf.predict(X_test)
```

Returns something like:

```python
['cats', 'dogs', 'cats', ...]
```

These are the predicted labels for test images.

---

## Step 9: Visualize test images

```python
import matplotlib.pyplot as plt 

for index in range(0, 10): 
    plt.subplot(1, 10, index + 1) 
    plt.imshow(X_test[index].reshape(64,64), cmap='gray') 
    plt.axis("off")

plt.show()
```

### What this does

* Displays the **first 10 test images**
* Helps you visually verify what the model is predicting

The key line:

```python
X_test[index].reshape(64,64)
```

This converts the flattened image back into a 2D image so it can be displayed.

---

## Step 10: Create a reusable image preprocessing function

```python
import numpy as np 

IMG_SIZE = (64, 64)

def preprocess_image(path: str) -> np.ndarray:
    img = imread(path, as_gray=True)
    img = resize(img, IMG_SIZE, anti_aliasing=True)
    return img.flatten().astype(np.float32)
```

### Why this function exists

You **must preprocess new images the same way** as training images.

This function guarantees:

* Same size
* Same grayscale conversion
* Same flattening

---

## Step 11: Predict a brand new image

```python
x_new = preprocess_image("cat.png").reshape(1, -1)
pred_label = clf.predict(x_new)[0]
print(pred_label)
```

### Key details

* `.reshape(1, -1)`
  The model expects **2D input**:

  ```
  (number_of_images, number_of_features)
  ```

* `clf.predict(x_new)`
  Returns a list, so `[0]` extracts the label

Example output:

```
cats
```

🎉 Your model just classified a real image!

---

## Final mental model to remember

1. Images → numbers
2. Numbers → fixed size
3. Fixed size → ML model
4. ML model → predictions

This notebook is an **excellent foundation** for:

* CNNs later
* Transfer learning
* Real-world image classification systems


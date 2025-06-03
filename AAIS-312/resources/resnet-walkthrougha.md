
## ✅ 1. **Import Necessary Libraries**

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
```

### 🔍 What This Does:

* **NumPy** is used for numerical operations.
* **TensorFlow / Keras** provides model loading and preprocessing tools.
* **Matplotlib** helps visualize the image.
* `decode_predictions` converts model outputs into human-readable labels.

---

## ✅ 2. **Load the Pre-trained ResNet50 Model**

```python
resnet_model = ResNet50(weights="imagenet")
```

### 🔍 Notes:

* This loads the ResNet50 architecture with **weights trained on ImageNet** (a dataset of 1.4M+ images across 1000 classes).
* The model is ready for inference.

---

## ✅ 3. **View the Model Summary**

```python
resnet_model.summary()
```

### 🔍 What You See:

* A detailed layer-by-layer breakdown of the network.
* Includes **Convolutional layers**, **Batch Normalization**, **ReLU**, **Pooling**, and **Residual Additions**.
* Ends with:

  * A **Global Average Pooling** layer.
  * A **Dense (Softmax)** layer outputting predictions for 1000 classes.
* Total parameters: **\~25.6 million**

---

## ✅ 4. **Load and Display an Image**

```python
img_path = "/content/sample_data/dog.png"
img = image.load_img(img_path, target_size=(224, 224))
plt.axis("off")
plt.imshow(img)
```

### 🔍 Details:

* Loads an image and **resizes it to 224x224**, the input size required by ResNet50.
* `plt.imshow()` displays the image with axes turned off.

---

## ✅ 5. **Convert the Image to a Numpy Array**

```python
img_array = image.img_to_array(img)
```

### 🔍 Output:

* Shape: `(224, 224, 3)` → height, width, RGB channels.
* Pixel values range from 0 to 255 (float32).

---

## ✅ 6. **Add Batch Dimension**

```python
img_array = np.expand_dims(img_array, axis=0)
```

### 🔍 Why:

* ResNet50 expects input shape of **(batch\_size, height, width, channels)**.
* After this: `(1, 224, 224, 3)`

---

## ✅ 7. **Preprocess the Input**

```python
img_array = preprocess_input(img_array)
```

### 🔍 What Happens:

* This step **normalizes pixel values** to match the scale ResNet50 was trained on.
* The transformation typically subtracts the ImageNet dataset mean and converts from RGB to BGR.

---

## ✅ 8. **Make a Prediction**

```python
predictions = resnet_model.predict(img_array)
```

### 🔍 Output:

* A NumPy array of shape `(1, 1000)`.
* Contains **probabilities** for each of the 1000 ImageNet classes.

---

## ✅ 9. **Decode the Predictions**

```python
decoded_predictions = decode_predictions(predictions, top=10)[0]
```

### 🔍 Output:

A list of tuples like:

```python
[('n02099601', 'golden_retriever', 0.9423), ...]
```

* `n02099601`: Class ID.
* `'golden_retriever'`: Human-readable label.
* `0.9423`: Confidence score.

---

## ✅ 10. **Example Output Explained**

```python
[
 ('n02099601', 'golden_retriever', 0.9423127),
 ('n02099712', 'Labrador_retriever', 0.05201903),
 ('n02108551', 'Tibetan_mastiff', 0.0007862973),
 ...
]
```

### 🔍 Meaning:

* The model **confidently predicts** the image is a **Golden Retriever** with \~94% confidence.
* Other similar dog breeds and even unrelated classes (like `television`) show up with much lower probabilities.

---

## ✅ Summary

| Step | Action                              |
| ---- | ----------------------------------- |
| 1    | Import required libraries           |
| 2    | Load pre-trained ResNet50 model     |
| 3    | Inspect model architecture          |
| 4    | Load and display the image          |
| 5-6  | Convert and reshape image for input |
| 7    | Preprocess the image                |
| 8    | Get predictions                     |
| 9    | Decode the top classes              |
| 10   | Interpret results                   |

---

## ✅ Next Steps

You can:

* Try with different images.
* Use Grad-CAM to **visualize attention**.
* Replace the top layer to fine-tune on your own dataset (transfer learning).
* Export predictions or integrate into a Flask/Streamlit app.


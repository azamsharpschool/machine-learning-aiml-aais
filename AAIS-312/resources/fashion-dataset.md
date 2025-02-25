Here's a detailed walkthrough of the **Exercise: Training a Neural Network on the Fashion MNIST Dataset** using TensorFlow and Keras.

---

# **Exercise: Training a Neural Network on the Fashion MNIST Dataset**

## **Objective**
In this exercise, you will build, compile, and train a neural network to classify images from the **Fashion MNIST dataset** using **TensorFlow** and **Keras**. This will help you understand the basics of **neural networks, data preprocessing, and model evaluation**.

---

## **Step 1: Import Necessary Libraries**

Before starting, ensure that you have **TensorFlow** installed in your environment. You can install it using:

```bash
pip install tensorflow
```

Now, import the necessary libraries:

```python
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
```

---

## **Step 2: Load and Explore the Dataset**

The **Fashion MNIST dataset** consists of **70,000 grayscale images** of size **28x28 pixels**, with **10 categories** representing different types of clothing.

### **Load the Dataset**
```python
# Load the Fashion MNIST dataset
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
```

### **Explore the Data**
Print the shapes of training and testing datasets:
```python
print(f"Training images shape: {train_images.shape}")  # (60000, 28, 28)
print(f"Training labels shape: {train_labels.shape}")  # (60000,)
print(f"Testing images shape: {test_images.shape}")    # (10000, 28, 28)
print(f"Testing labels shape: {test_labels.shape}")    # (10000,)
```

### **Plot a Few Sample Images**
```python
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

plt.figure(figsize=(10,5))
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(train_images[i], cmap='gray')
    plt.title(class_names[train_labels[i]])
    plt.axis('off')
plt.show()
```

---

## **Step 3: Normalize the Data**
Neural networks perform better when input values are **scaled**. The pixel values in the dataset range from **0 to 255**, so we normalize them to be between **0 and 1**.

```python
train_images = train_images / 255.0
test_images = test_images / 255.0
```

---

## **Step 4: Build the Neural Network Model**
Now, we define a **Sequential** model in Keras.

```python
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # Convert 28x28 into 1D array of 784 elements
    keras.layers.Dense(128, activation='relu'),  # Hidden layer with 128 neurons and ReLU activation
    keras.layers.Dense(10, activation='softmax') # Output layer with 10 neurons for 10 classes
])
```

---

## **Step 5: Compile the Model**
We need to compile the model by defining:
- **Optimizer**: Adam (adaptive learning rate optimization).
- **Loss function**: Sparse categorical cross-entropy (suitable for integer labels).
- **Metric**: Accuracy (to track how well the model performs).

```python
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```

---

## **Step 6: Train the Model**
Now, we train the model using **fit()**, specifying the training data and the number of **epochs**.

```python
model.fit(train_images, train_labels, epochs=10)
```

> 🔹 **Epochs**: The number of times the model will see the entire dataset. 10 epochs is a good starting point.

---

## **Step 7: Evaluate the Model**
After training, evaluate the model on the **test set** to check how well it generalizes.

```python
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f'\nTest Accuracy: {test_acc:.4f}')
```

> The accuracy might be slightly lower on the test set due to overfitting.

---

## **Step 8: Make Predictions**
Now, we use the trained model to make **predictions** on test images.

```python
predictions = model.predict(test_images)
```

Each **prediction** is a probability distribution over the **10 categories**.

```python
# Print predicted label for first test image
print(f"Predicted label: {np.argmax(predictions[0])}")
print(f"Actual label: {test_labels[0]}")
```

---

## **Step 9: Display Predictions with Test Images**
To visually inspect predictions, let's plot **test images** with **predicted and actual labels**.

```python
def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap='gray')

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel(f"{class_names[predicted_label]} ({class_names[true_label]})", color=color)

# Plot first 10 test images with predictions
plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i+1)
    plot_image(i, predictions[i], test_labels, test_images)
plt.show()
```

---

## **Conclusion**
In this exercise, you:
✅ Loaded and explored the **Fashion MNIST dataset**  
✅ Normalized the pixel values for better training  
✅ Built a **neural network** using Keras with **Flatten, Dense (ReLU), and Dense (Softmax) layers**  
✅ Compiled the model with **Adam optimizer** and **Sparse Categorical Cross-Entropy loss**  
✅ Trained the model and evaluated its performance on test data  
✅ Made **predictions** and displayed them alongside actual labels  

This is a fundamental example of deep learning **image classification** using TensorFlow and Keras. You can improve performance by experimenting with:
- Adding **more layers** (e.g., convolutional layers for feature extraction)
- Using **data augmentation** to prevent overfitting
- Tweaking **learning rate, batch size, or optimizer**

🚀 **Next Steps**: Try using a **Convolutional Neural Network (CNN)** for better accuracy on the Fashion MNIST dataset.

Would you like a version of this for Jupyter Notebook with markdown formatting?
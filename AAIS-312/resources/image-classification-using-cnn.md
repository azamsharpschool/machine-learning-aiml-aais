### Walkthrough: Deep Learning for Image Classification Using CNN on CIFAR-10 Dataset

This walkthrough guides you through building a Convolutional Neural Network (CNN) to classify images from the CIFAR-10 dataset using TensorFlow/Keras.

---

### **Objective**
Train a CNN to classify 32x32 color images from 10 classes (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck) in the CIFAR-10 dataset.

---

### **Steps**

#### **Step 1: Data Preparation**
1. **Load the CIFAR-10 Dataset:** CIFAR-10 is available directly in Keras.
2. **Normalize the Images:** Scale pixel values between 0 and 1 for better performance.
3. **One-Hot Encode Labels:** Convert class labels (0-9) into one-hot encoded vectors.

```python
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical

# Load CIFAR-10 dataset
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# Normalize pixel values
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# One-hot encode labels
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
```

---

#### **Step 2: Build the CNN Model**
1. **Add Convolutional Layers:** Extract features from images.
2. **Add Pooling Layers:** Reduce the size of feature maps.
3. **Add Dropout Layers:** Prevent overfitting.
4. **Fully Connected Layers:** Combine extracted features for classification.
5. **Output Layer:** Use softmax for multi-class classification.

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Build the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')  # 10 classes
])
```

---

#### **Step 3: Compile the Model**
Use:
- **Loss Function:** Categorical cross-entropy for multi-class classification.
- **Optimizer:** Adam for efficient weight updates.
- **Metrics:** Accuracy to evaluate performance.

```python
# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```

---

#### **Step 4: Train the Model**
Train the CNN on the training data with validation during training to monitor performance.

```python
# Train the model
history = model.fit(X_train, y_train, epochs=20, batch_size=64, validation_split=0.2)
```

---

#### **Step 5: Evaluate the Model**
Evaluate the model on the test set to report accuracy and loss. Generate a classification report and confusion matrix for detailed performance metrics.

```python
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

# Evaluate on test data
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

# Generate predictions
y_pred = np.argmax(model.predict(X_test), axis=1)
y_true = np.argmax(y_test, axis=1)

# Classification report and confusion matrix
print(classification_report(y_true, y_pred))
print(confusion_matrix(y_true, y_pred))
```

---

#### **Step 6: Visualize Results**
Show examples of correctly and incorrectly classified images. Discuss the model’s strengths and weaknesses.

```python
import matplotlib.pyplot as plt

# Visualize correctly classified images
correct_indices = np.where(y_pred == y_true)[0]
plt.figure(figsize=(10, 5))
for i, idx in enumerate(correct_indices[:5]):
    plt.subplot(1, 5, i+1)
    plt.imshow(X_test[idx])
    plt.title(f"Predicted: {y_pred[idx]}\nTrue: {y_true[idx]}")
    plt.axis('off')
plt.show()

# Visualize incorrectly classified images
incorrect_indices = np.where(y_pred != y_true)[0]
plt.figure(figsize=(10, 5))
for i, idx in enumerate(incorrect_indices[:5]):
    plt.subplot(1, 5, i+1)
    plt.imshow(X_test[idx])
    plt.title(f"Predicted: {y_pred[idx]}\nTrue: {y_true[idx]}")
    plt.axis('off')
plt.show()
```

---

### **Full Code**
```python
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load and preprocess the data
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Step 2: Build the CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

# Step 3: Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Step 4: Train the model
history = model.fit(X_train, y_train, epochs=20, batch_size=64, validation_split=0.2)

# Step 5: Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
y_pred = np.argmax(model.predict(X_test), axis=1)
y_true = np.argmax(y_test, axis=1)
print(classification_report(y_true, y_pred))
print(confusion_matrix(y_true, y_pred))

# Step 6: Visualize results
correct_indices = np.where(y_pred == y_true)[0]
plt.figure(figsize=(10, 5))
for i, idx in enumerate(correct_indices[:5]):
    plt.subplot(1, 5, i+1)
    plt.imshow(X_test[idx])
    plt.title(f"Pred: {y_pred[idx]}, True: {y_true[idx]}")
    plt.axis('off')
plt.show()

incorrect_indices = np.where(y_pred != y_true)[0]
plt.figure(figsize=(10, 5))
for i, idx in enumerate(incorrect_indices[:5]):
    plt.subplot(1, 5, i+1)
    plt.imshow(X_test[idx])
    plt.title(f"Pred: {y_pred[idx]}, True: {y_true[idx]}")
    plt.axis('off')
plt.show()
```

---

### **Key Takeaways**
1. **CIFAR-10 Dataset:** Small, diverse dataset for image classification.
2. **CNN Layers:** Extract features and classify efficiently.
3. **Evaluation:** Provides detailed insights using accuracy, classification reports, and confusion matrices.
4. **Visualization:** Highlights strengths and weaknesses with sample predictions.

Let me know if you'd like further refinements!
### Walkthrough: Iris Flower Recognition with TensorFlow and Keras

This exercise walks you through building a neural network to classify iris flower species using the Iris dataset. We’ll cover setup, data preparation, model creation, training, and evaluation.

---

### **Step 1: Setup the Environment**
1. **Install TensorFlow:**
   If you don’t have TensorFlow installed, use the following command:
   ```bash
   pip install tensorflow
   ```

2. **Import Required Libraries:**
   Import all the necessary libraries for this exercise:
   ```python
   import tensorflow as tf
   from tensorflow.keras.models import Sequential
   from tensorflow.keras.layers import Dense
   from sklearn.datasets import load_iris
   from sklearn.model_selection import train_test_split
   from sklearn.preprocessing import OneHotEncoder
   import numpy as np
   import matplotlib.pyplot as plt
   ```

---

### **Step 2: Load and Prepare the Dataset**
1. **Load the Iris Dataset:**
   The dataset contains four features (sepal length, sepal width, petal length, petal width) and three classes (Setosa, Versicolor, Virginica).
   ```python
   iris = load_iris()
   data = iris.data
   target = iris.target
   ```

2. **One-Hot Encode the Target:**
   Convert class labels (0, 1, 2) into one-hot encoded vectors:
   ```python
   encoder = OneHotEncoder(sparse=False)
   target = encoder.fit_transform(target.reshape(-1, 1))
   ```

3. **Split Data into Training and Testing Sets:**
   Split the dataset into 80% training and 20% testing:
   ```python
   train_data, test_data, train_labels, test_labels = train_test_split(
       data, target, test_size=0.2, random_state=42)
   ```

---

### **Step 3: Build the Neural Network**
1. **Define the Model:**
   Create a sequential model with:
   - **Input layer:** 4 features from the dataset.
   - **Hidden layers:** Two layers with 10 neurons each and ReLU activation.
   - **Output layer:** 3 neurons (one for each class) with a softmax activation function.
   ```python
   model = Sequential([
       Dense(10, activation='relu', input_shape=(4,)),  # Input layer
       Dense(10, activation='relu'),                   # Hidden layer
       Dense(3, activation='softmax')                  # Output layer
   ])
   ```

2. **Compile the Model:**
   Specify the optimizer, loss function, and evaluation metric:
   ```python
   model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
   ```

---

### **Step 4: Train the Model**
1. Train the model using the training data for 50 epochs. Use 20% of the training data for validation.
   ```python
   history = model.fit(train_data, train_labels, epochs=50, validation_split=0.2)
   ```

---

### **Step 5: Evaluate the Model**
1. Test the model on unseen data and calculate accuracy:
   ```python
   test_loss, test_accuracy = model.evaluate(test_data, test_labels)
   print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
   ```

---

### **Step 6: Visualize Training Results**
1. Plot training and validation accuracy over epochs:
   ```python
   acc = history.history['accuracy']
   val_acc = history.history['val_accuracy']
   loss = history.history['loss']
   val_loss = history.history['val_loss']

   epochs = range(len(acc))

   # Plot accuracy
   plt.plot(epochs, acc, 'r', label='Training accuracy')
   plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
   plt.title('Training and Validation Accuracy')
   plt.legend(loc=0)
   plt.figure()

   # Plot loss
   plt.plot(epochs, loss, 'r', label='Training loss')
   plt.plot(epochs, val_loss, 'b', label='Validation loss')
   plt.title('Training and Validation Loss')
   plt.legend(loc=0)
   plt.show()
   ```

---

### **Step 7: Experiment and Improve**
1. Adjust hyperparameters and observe changes:
   - Increase or decrease the number of neurons or layers.
   - Change activation functions (e.g., try Tanh instead of ReLU).
   - Increase epochs or alter the learning rate in the Adam optimizer.

---

### **Conclusion**
By completing this exercise, you’ve built a neural network to classify iris flowers into three species using TensorFlow and Keras. You’ve learned how to preprocess data, define a model, and evaluate its performance.

This is a foundational project in deep learning, and you can extend it by experimenting with different architectures or trying other datasets. Let me know if you’d like further explanations or enhancements!
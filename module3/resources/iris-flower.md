
### Deep Learning Exercise: Iris Flower Recognition with TensorFlow and Keras

#### Objective:
- Build and train a simple neural network to classify iris flower species.

#### Prerequisites:
- Basic knowledge of Python programming.
- Familiarity with TensorFlow and Keras libraries.

#### Dataset:
- Use the **Iris dataset** available from the UCI Machine Learning Repository or directly from `sklearn.datasets`.

#### Exercise Steps:

1. **Setup the Environment:**

   Install TensorFlow if you haven't already:

   ```python
   !pip install tensorflow
   ```

   Import necessary libraries:

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

2. **Load and Prepare the Dataset:**

   ```python
   # Load the Iris dataset
   iris = load_iris()
   data = iris.data
   target = iris.target

   # One-hot encode the target labels
   encoder = OneHotEncoder(sparse=False)
   target = encoder.fit_transform(target.reshape(-1, 1))

   # Split the dataset into training and testing sets
   train_data, test_data, train_labels, test_labels = train_test_split(data, target, test_size=0.2, random_state=42)
   ```

3. **Build the Model:**

   ```python
   model = Sequential([
       Dense(10, activation='relu', input_shape=(4,)),  # Input layer with 4 features
       Dense(10, activation='relu'),  # Hidden layer
       Dense(3, activation='softmax')  # Output layer with 3 classes
   ])

   model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
   ```

4. **Train the Model:**

   ```python
   history = model.fit(train_data, train_labels, epochs=50, validation_split=0.2)
   ```

5. **Evaluate the Model:**

   ```python
   test_loss, test_accuracy = model.evaluate(test_data, test_labels)
   print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
   ```

6. **Visualize Training Results:**

   ```python
   acc = history.history['accuracy']
   val_acc = history.history['val_accuracy']
   loss = history.history['loss']
   val_loss = history.history['val_loss']

   epochs = range(len(acc))

   plt.plot(epochs, acc, 'r', label='Training accuracy')
   plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
   plt.title('Training and validation accuracy')
   plt.legend(loc=0)
   plt.figure()

   plt.plot(epochs, loss, 'r', label='Training loss')
   plt.plot(epochs, val_loss, 'b', label='Validation loss')
   plt.title('Training and validation loss')
   plt.legend(loc=0)
   plt.show()
   ```

This exercise is designed to be simple and easy to follow for absolute beginners. It uses a straightforward neural network to classify iris flowers based on their features. Students can experiment by adjusting the number of neurons, layers, epochs, and other hyperparameters to see how the model's performance changes.
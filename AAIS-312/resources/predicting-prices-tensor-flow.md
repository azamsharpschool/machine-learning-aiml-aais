Here's a **step-by-step walkthrough** for a **deep learning exercise** on predicting house prices using Python and TensorFlow/Keras. This exercise will guide you through loading data, preprocessing, building a neural network, training the model, and evaluating performance.

---

## **Step 1: Install Required Libraries**
Ensure you have TensorFlow, Pandas, NumPy, and Matplotlib installed:

```bash
pip install tensorflow pandas numpy matplotlib scikit-learn
```

---

## **Step 2: Import Necessary Libraries**
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras
```

---

## **Step 3: Load the Dataset**
For this exercise, we will use a synthetic housing dataset. If you have a dataset (e.g., **California Housing dataset**), you can replace this part.

```python
# Load dataset (using California Housing dataset)
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Price'] = data.target  # Target variable

# Display first few rows
print(df.head())
```

---

## **Step 4: Preprocess the Data**
- Normalize features using **StandardScaler**
- Split data into training & test sets

```python
# Split features and target
X = df.drop(columns=['Price']).values
y = df['Price'].values

# Split dataset into training (80%) and test (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

---

## **Step 5: Build the Neural Network Model**
We will use a **simple feedforward neural network** with:
- **Three dense layers**
- **ReLU activation for hidden layers**
- **Mean Squared Error (MSE) as loss function**
- **Adam optimizer**

```python
# Define the neural network
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1)  # Output layer (single neuron for regression)
])

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Display model summary
model.summary()
```

---

## **Step 6: Train the Model**
Train the model for **100 epochs** and visualize training progress.

```python
# Train the model
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, batch_size=32, verbose=1)
```

---

## **Step 7: Evaluate the Model**
Check the **Mean Absolute Error (MAE)** on test data.

```python
# Evaluate performance on test data
test_loss, test_mae = model.evaluate(X_test, y_test)
print(f"Test MAE: {test_mae:.2f}")
```

---

## **Step 8: Plot Training Performance**
Visualize how the loss decreases over epochs.

```python
# Plot loss over epochs
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss (MSE)')
plt.legend()
plt.show()
```

---

## **Step 9: Make Predictions**
Predict prices using the trained model.

```python
# Make predictions on test set
predictions = model.predict(X_test)

# Display some predictions vs actual values
for i in range(5):
    print(f"Predicted: {predictions[i][0]:.2f}, Actual: {y_test[i]:.2f}")
```

---



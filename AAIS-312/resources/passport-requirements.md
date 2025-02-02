Here's a step-by-step **walkthrough** for building a simple **TensorFlow model** to predict whether a country requires a visa.

---

## **Step 1: Install Required Libraries**
Ensure you have **TensorFlow**, **NumPy**, and **Scikit-learn** installed.

```bash
pip install tensorflow numpy scikit-learn
```

---

## **Step 2: Import Necessary Libraries**
```python
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
```

---

## **Step 3: Prepare the Data**
We have an array of countries and their corresponding **visa requirements** (1 = visa required, 0 = no visa required).

```python
# Data
passports = np.array(["us", "oman", "us", "us", "oman", "us", "oman", "us"])
visa_required = np.array([0, 1, 0, 0, 1, 0, 1, 0])  # Target labels
```

---

## **Step 4: Encode Categorical Data**
Since neural networks work with numerical data, we need to convert country names into **numerical values** using **Label Encoding**.

```python
# Convert categorical countries to numerical labels
encoder = LabelEncoder()
passports_encoded = encoder.fit_transform(passports)  # Convert "us" to 0, "oman" to 1

print("Encoded Countries:", passports_encoded)  # Example Output: [0 1 0 0 1 0 1 0]
```

---

## **Step 5: Build the Neural Network**
We create a simple **feedforward neural network** with:
- **1 input neuron** (country code)
- **1 dense layer** with 4 neurons
- **1 output neuron** (predicting visa requirement: 0 or 1)
- **Sigmoid activation** since it's a binary classification problem
- **Binary cross-entropy** as the loss function

```python
# Define the model
model = keras.Sequential([
    keras.layers.Dense(4, activation='relu', input_shape=(1,)),  # Hidden layer
    keras.layers.Dense(1, activation='sigmoid')  # Output layer (binary classification)
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Display model summary
model.summary()
```

---

## **Step 6: Train the Model**
We train the model for **100 epochs**.

```python
# Train the model
model.fit(passports_encoded, visa_required, epochs=100, verbose=1)
```

---

## **Step 7: Make Predictions**
Now, let's predict whether a given country **requires a visa**.

```python
# Function to check visa requirement
def check_visa(country):
    encoded_country = encoder.transform([country])[0]  # Convert country name to numeric value
    prediction = model.predict(np.array([encoded_country]))  # Make prediction
    return int(prediction[0] > 0.5)  # Return 1 (visa required) or 0 (no visa required)

# Test predictions
print("US Visa Requirement:", check_visa("us"))  # Expected Output: 0
print("Oman Visa Requirement:", check_visa("oman"))  # Expected Output: 1
```

---

## **Step 8: Save and Load the Model**
Save the trained model for future use.

```python
# Save the model
model.save("visa_prediction_model.h5")

# Load the model
loaded_model = keras.models.load_model("visa_prediction_model.h5")
print("Model loaded successfully!")
```

---

## **Next Steps**
- **Expand dataset** with more countries
- **Use word embeddings** (e.g., TensorFlow’s `TextVectorization`) instead of label encoding
- **Deploy the model** as an API using FastAPI or Flask
- **Improve accuracy** by adding more layers or trying different activation functions

---

This is a **simple but effective deep learning model** for predicting visa requirements! 🚀 Let me know if you need **modifications or explanations!**
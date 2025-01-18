### Walkthrough: Logistic Regression with Deep Learning

This walkthrough will guide you through building a logistic regression model using TensorFlow and Keras to predict if a person will sleep well based on their coffee consumption and fitness level.

---

### **Step 1: Install Necessary Libraries**
First, ensure you have the required libraries installed. Open your terminal or command prompt and execute:

```bash
conda install tensorflow pandas
```

This will install TensorFlow for deep learning and pandas for data manipulation.

---

### **Step 2: Save the Data**
Copy the following data into a CSV file named `coffee_sleep_data.csv`. This file will serve as the dataset for our model.

```csv
cups_of_coffee,fitness,will_sleep
5,87,1
2,76,1
1,96,1
4,73,1
1,50,1
0,62,1
3,63,1
2,29,0
7,51,0
3,38,0
8,20,0
6,80,1
2,15,0
3,75,1
4,30,0
5,45,0
1,91,1
7,54,0
3,48,0
6,88,1
0,66,1
1,52,1
8,14,0
4,43,0
2,34,0
5,72,0
1,99,1
6,77,1
2,44,0
7,61,0
3,55,0
8,20,0
6,83,1
2,41,0
1,95,1
0,59,1
4,33,0
7,50,0
3,40,0
8,27,0
5,67,0
6,82,1
1,60,1
2,35,0
7,48,0
3,56,0
```

---

### **Step 3: Load and Prepare the Data**
1. **Load Data:** Use pandas to load the CSV file.
2. **Separate Features and Target:** Identify the predictors (`cups_of_coffee` and `fitness`) and the target variable (`will_sleep`).
3. **Split Data:** Split the data into training and testing sets.
4. **Standardize Features:** Standardize the feature values for better performance.

Code:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the data
data = pd.read_csv('coffee_sleep_data.csv')

# Separate features and target variable
X = data[['cups_of_coffee', 'fitness']]
y = data['will_sleep']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

---

### **Step 4: Build the Logistic Regression Model**
1. Define a **sequential model** using Keras.
2. Add a **dense layer** with:
   - One neuron (logistic regression requires a single output).
   - A **sigmoid activation function** to output probabilities.

Code:

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define the model
model = Sequential([
    Dense(1, activation='sigmoid', input_shape=(2,))
])
```

---

### **Step 5: Compile the Model**
1. Use the **Adam optimizer** for training.
2. Set the **binary crossentropy** loss function for binary classification.
3. Specify **accuracy** as a metric to monitor performance.

Code:

```python
# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

---

### **Step 6: Train the Model**
1. Train the model using the training data.
2. Use a validation split to monitor the model's performance during training.

Code:

```python
# Train the model
history = model.fit(X_train, y_train, validation_split=0.2, epochs=50, batch_size=8)
```

---

### **Step 7: Evaluate the Model**
1. Evaluate the model on the test data to see how well it performs.
2. Print the test accuracy.

Code:

```python
# Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
```

---

### **Step 8: Make Predictions**
1. Use the model to predict probabilities for the test data.
2. Convert probabilities to binary classes (0 or 1) using a threshold of 0.5.
3. Print the predictions alongside the actual labels for comparison.

Code:

```python
# Make predictions
predictions = model.predict(X_test)
predicted_classes = (predictions > 0.5).astype(int)

# Print predictions and actual classes
comparison = pd.DataFrame({'Actual': y_test.values, 'Predicted': predicted_classes.flatten()})
print(comparison)
```

---

### **Conclusion**
You've built and trained a logistic regression model using deep learning! This exercise demonstrates how deep learning can be applied to simple binary classification problems. Feel free to experiment with more data or tweak the model parameters to see how they affect performance.
### Walkthrough: Predicting Employee Attrition with Missing Values

In this exercise, we will build a logistic regression model to predict employee attrition while handling missing data. This walkthrough includes steps to load, preprocess, and model the data.

---

### **Step 1: Save the Data**
Save the following data into a CSV file named `employee_attrition_data_with_missing_values.csv`:

```csv
age,satisfaction_level,number_of_projects,average_monthly_hours,attrition
34,0.45,5,220,0
29,0.80,3,,0
41,0.30,6,250,1
,0.70,2,170,0
50,0.25,7,280,1
35,0.60,4,210,
43,0.40,5,240,1
30,0.85,3,190,0
38,,4,230,0
49,0.20,6,260,1
32,0.75,,200,0
36,0.50,4,220,0
40,0.35,5,,1
28,0.90,2,180,0
45,0.30,6,270,1
33,,4,210,0
37,0.50,5,240,0
46,0.25,7,280,1
31,0.80,3,200,0
39,0.55,4,230,0
42,0.35,6,260,1
26,0.85,2,170,0
44,0.30,5,270,1
48,,7,290,1
```

---

### **Step 2: Load and Prepare the Data**
1. **Load the Data:** Use pandas to load the dataset.
2. **Handle Missing Values:** Decide how to handle missing values:
   - Impute missing values with the mean/median.
   - Drop rows with too many missing values (if necessary).
3. **Separate Features and Target Variable:** Split the dataset into input features (`age`, `satisfaction_level`, `number_of_projects`, `average_monthly_hours`) and the target variable (`attrition`).
4. **Split Data:** Divide the dataset into training and testing sets.
5. **Standardize Features:** Use `StandardScaler` to normalize the features.

Code:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Load the data
data = pd.read_csv('employee_attrition_data_with_missing_values.csv')

# Handle missing values
imputer = SimpleImputer(strategy='mean')
data.iloc[:, :-1] = imputer.fit_transform(data.iloc[:, :-1])  # Impute missing values for features
data['attrition'] = data['attrition'].fillna(0)  # Assume missing attrition values are "not leaving"

# Separate features and target variable
X = data[['age', 'satisfaction_level', 'number_of_projects', 'average_monthly_hours']]
y = data['attrition']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

---

### **Step 3: Build the Logistic Regression Model**
1. Define a **sequential model** using Keras.
2. Add a dense layer with:
   - One neuron.
   - Sigmoid activation function.

Code:

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define the model
model = Sequential([
    Dense(1, activation='sigmoid', input_shape=(4,))
])
```

---

### **Step 4: Compile the Model**
1. Use the **Adam optimizer** for efficient training.
2. Set the **binary crossentropy** loss function for binary classification.
3. Specify **accuracy** as a metric.

Code:

```python
# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

---

### **Step 5: Train the Model**
1. Train the model using the training data.
2. Use a validation split to monitor the model's performance during training.

Code:

```python
# Train the model
history = model.fit(X_train, y_train, validation_split=0.2, epochs=50, batch_size=8)
```

---

### **Step 6: Evaluate the Model**
1. Evaluate the model’s performance on the test dataset.
2. Print the test accuracy.

Code:

```python
# Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
```

---

### **Step 7: Make Predictions**
1. Predict probabilities for the test data.
2. Convert probabilities to binary classes using a threshold of 0.5.
3. Compare predicted classes with actual classes.

Code:

```python
# Make predictions
predictions = model.predict(X_test)
predicted_classes = (predictions > 0.5).astype(int)

# Print predictions alongside actual values
comparison = pd.DataFrame({'Actual': y_test.values, 'Predicted': predicted_classes.flatten()})
print(comparison)
```

---

### **Conclusion**
This exercise demonstrates how to handle missing data and use logistic regression with deep learning to predict employee attrition. Key steps include:
- Handling missing values effectively.
- Normalizing features for better model performance.
- Building and evaluating a logistic regression model using TensorFlow/Keras.

Feel free to experiment with the model by adding more layers or trying different imputation techniques! Let me know if you need additional clarification or enhancements.
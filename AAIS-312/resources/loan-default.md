### Walkthrough: Predicting Loan Default with Missing Values

In this exercise, we will build a logistic regression model to predict whether a loan applicant will default on their loan using TensorFlow and Keras. The dataset contains missing values, and we will handle them as part of the preprocessing steps.

---

### **Step 1: Save the Dataset**
Save the following data into a file named `loan_default_data_with_missing_values.csv`:

```csv
loan_amount,interest_rate,income,credit_score,loan_default
15000,5.5,55000,700,0
20000,6.0,62000,,0
25000,,48000,680,1
30000,4.5,75000,740,0
10000,5.0,45000,650,1
22000,6.5,53000,710,
,7.2,47000,670,1
18000,5.8,60000,730,0
24000,6.8,51000,690,1
32000,4.0,,750,0
16000,5.3,58000,710,0
28000,7.5,46000,,1
14000,5.7,57000,720,0
26000,6.7,49000,680,1
19000,5.9,59000,700,0
31000,4.2,77000,740,0
12000,,44000,650,1
23000,6.3,52000,710,0
17000,5.4,,730,0
29000,7.1,48000,690,1
```

---

### **Step 2: Load and Prepare the Data**

1. **Load the Data:** Import the dataset into a pandas DataFrame.
2. **Handle Missing Values:** Impute missing values with the column mean for numerical columns.
3. **Separate Features and Target Variable:** Split the dataset into:
   - **Features:** `loan_amount`, `interest_rate`, `income`, `credit_score`.  
   - **Target:** `loan_default`.
4. **Split Data:** Divide the dataset into training and testing sets.
5. **Standardize Features:** Normalize the feature data for better model performance.

Code:
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('loan_default_data_with_missing_values.csv')

# Handle missing values
imputer = SimpleImputer(strategy='mean')
data.iloc[:, :-1] = imputer.fit_transform(data.iloc[:, :-1])  # Impute features
data['loan_default'] = data['loan_default'].fillna(0)  # Assume missing target values are non-default

# Separate features and target variable
X = data[['loan_amount', 'interest_rate', 'income', 'credit_score']]
y = data['loan_default']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

---

### **Step 3: Build the Logistic Regression Model**

1. **Define the Model:**
   Create a simple neural network with:
   - **Input Layer:** 4 features (`loan_amount`, `interest_rate`, `income`, `credit_score`).
   - **Output Layer:** 1 neuron with a sigmoid activation function for binary classification.

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

1. **Optimizer:** Use the Adam optimizer for efficient training.
2. **Loss Function:** Binary crossentropy is ideal for binary classification problems.
3. **Metric:** Use accuracy to evaluate the model’s performance.

Code:
```python
# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

---

### **Step 5: Train the Model**

1. Train the model with:
   - Training data.
   - 20% of the training data used as validation data.
   - 50 epochs to allow the model to learn the relationships.

Code:
```python
# Train the model
history = model.fit(X_train, y_train, validation_split=0.2, epochs=50, batch_size=8)
```

---

### **Step 6: Evaluate the Model**

1. Test the model’s accuracy on unseen data to evaluate its generalization ability.

Code:
```python
# Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
```

---

### **Step 7: Make Predictions**

1. Predict probabilities for the test data.
2. Convert probabilities to binary classes (0 or 1) using a threshold of 0.5.
3. Compare predicted classes with actual labels.

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
This walkthrough demonstrates how to:
1. Handle missing data using imputation.
2. Build, train, and evaluate a logistic regression model using TensorFlow/Keras.
3. Use the model to make predictions and compare them with actual values.

You can extend this example by:
- Adding more features.
- Using different imputation strategies.
- Experimenting with deeper neural network architectures.

Let me know if you'd like more details or modifications!
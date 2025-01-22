Here’s a **step-by-step walkthrough** for understanding logistic regression with a **real-world example**:

- [Download Dataset](logistic_regression_dataset.csv)

---

### **Objective**  
We’ll build a logistic regression model to predict whether a customer will purchase a product based on their age and estimated salary.  

---

### **Step 1: Understand Logistic Regression**

Logistic regression is used for **binary classification problems** (e.g., yes/no, 0/1, true/false). Unlike linear regression, logistic regression outputs probabilities that are transformed into a binary output using a **sigmoid function**.

- **Sigmoid function**:  
  \[
  \sigma(z) = \frac{1}{1 + e^{-z}}
  \]  
  Converts any real value into a range between 0 and 1.  

- **Binary classification rule**:  
  If \( \sigma(z) > 0.5 \), predict **1**; otherwise, predict **0**.  

---

### **Step 2: Real-World Example**

We’ll predict if a customer will buy a product based on:
- **Features**: Age, Estimated Salary.
- **Target**: Purchased (1 for yes, 0 for no).

#### **Dataset Example**  
| Age | Estimated Salary | Purchased |
|-----|------------------|-----------|
| 22  | 19000            | 0         |
| 25  | 20000            | 0         |
| 47  | 50000            | 1         |
| 52  | 60000            | 1         |
| 29  | 43000            | 0         |

---

### **Step 3: Load and Prepare Data**

#### Import necessary libraries:
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
```

#### Load the dataset:
```python
# Example dataset
data = {
    "Age": [22, 25, 47, 52, 29],
    "EstimatedSalary": [19000, 20000, 50000, 60000, 43000],
    "Purchased": [0, 0, 1, 1, 0]
}

df = pd.DataFrame(data)
```

#### Split the data into training and testing sets:
```python
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

#### Scale the features (important for logistic regression):
```python
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

---

### **Step 4: Train the Logistic Regression Model**

#### Fit the model:
```python
model = LogisticRegression()
model.fit(X_train, y_train)
```

#### Check model coefficients:
```python
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")
```

---

### **Step 5: Make Predictions**

#### Predict on the test set:
```python
y_pred = model.predict(X_test)
```

#### Predict probabilities:
```python
y_proba = model.predict_proba(X_test)
print("Predicted probabilities:\n", y_proba)
```

---

### **Step 6: Evaluate the Model**

#### Accuracy Score:
```python
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
```

#### Confusion Matrix:
```python
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)
```

#### Classification Report:
```python
print("Classification Report:\n", classification_report(y_test, y_pred))
```

---

### **Step 7: Interpret the Results**

1. **Coefficients**:  
   Positive coefficients indicate a positive relationship between the feature and the target variable. Negative coefficients suggest an inverse relationship.

2. **Confusion Matrix**:  
   Analyze how many predictions are correct:
   - True Positives (TP): Correctly predicted "purchased."
   - True Negatives (TN): Correctly predicted "not purchased."
   - False Positives (FP): Incorrectly predicted "purchased."
   - False Negatives (FN): Incorrectly predicted "not purchased."

3. **Predicted Probabilities**:  
   Use these for applications requiring confidence levels, e.g., marketing campaigns targeting high-probability customers.

---

### **Real-World Use Case: Marketing Campaign**

Using this model:
- **Input**: Age and salary of a customer.
- **Output**: Probability of purchase.  
  Example: If \( \sigma(z) = 0.8 \), target the customer with promotional offers.

---

This walkthrough should help you understand logistic regression’s practical implementation. Let me know if you’d like to explore visualization or hyperparameter tuning!
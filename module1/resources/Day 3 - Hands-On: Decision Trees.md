Here is a solution for building a **Decision Tree Classifier** using **scikit-learn**, along with a sample dataset for determining loan approval.

---

### **Solution: Decision Trees for Loan Approval**

1. **Objective**:
   - Train a decision tree classifier to determine loan approval based on input features like income, credit score, loan amount, and employment status.

2. **Framework**:
   - **scikit-learn** is used for creating and training the decision tree, as well as for visualization.

---

### **Sample Dataset**

Here’s a small dataset for demonstration:

| Income (k$) | Credit Score | Loan Amount (k$) | Employment Status | Loan Approved |
|-------------|--------------|-------------------|-------------------|---------------|
| 50          | 700          | 20                | Full-time         | Yes           |
| 30          | 650          | 15                | Part-time         | No            |
| 80          | 750          | 50                | Full-time         | Yes           |
| 40          | 600          | 30                | Unemployed        | No            |
| 70          | 720          | 40                | Full-time         | Yes           |
| 20          | 580          | 10                | Part-time         | No            |

---

### **Implementation in Python**

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Create the sample dataset
data = {
    'Income': [50, 30, 80, 40, 70, 20],
    'Credit_Score': [700, 650, 750, 600, 720, 580],
    'Loan_Amount': [20, 15, 50, 30, 40, 10],
    'Employment_Status': ['Full-time', 'Part-time', 'Full-time', 'Unemployed', 'Full-time', 'Part-time'],
    'Loan_Approved': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Encode categorical variables
encoder = LabelEncoder()
df['Employment_Status'] = encoder.fit_transform(df['Employment_Status'])
df['Loan_Approved'] = encoder.fit_transform(df['Loan_Approved'])

# Define features and target
X = df[['Income', 'Credit_Score', 'Loan_Amount', 'Employment_Status']]
y = df['Loan_Approved']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the decision tree model
model = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
model.fit(X_train, y_train)

# Visualize the decision tree
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=X.columns, class_names=['No', 'Yes'], filled=True, rounded=True)
plt.title('Decision Tree for Loan Approval')
plt.show()

# Test the model
predictions = model.predict(X_test)
accuracy = model.score(X_test, y_test)

print("Predictions:", predictions)
print("Accuracy:", accuracy)
```

---

### **Explanation**

1. **Data Preparation**:
   - A dataset is created with features (`Income`, `Credit_Score`, `Loan_Amount`, `Employment_Status`) and a target (`Loan_Approved`).
   - Categorical data (`Employment_Status`, `Loan_Approved`) is encoded into numerical values using `LabelEncoder`.

2. **Model Training**:
   - The dataset is split into training and testing sets using `train_test_split`.
   - A `DecisionTreeClassifier` with Gini impurity is trained on the data.

3. **Visualization**:
   - The decision tree is visualized using `plot_tree` to understand its structure and decision-making process.

4. **Testing and Evaluation**:
   - The model's predictions are tested on the test set, and its accuracy is computed.

---

### **Output**

- **Decision Tree Visualization**:
  - A clear tree structure showing splits based on features like `Income`, `Credit_Score`, etc.
- **Predictions**:
  - Example: `[1, 0]` where `1=Yes` and `0=No`.
- **Accuracy**:
  - The accuracy score of the classifier on the test data.

---

This solution can be extended by using larger datasets, optimizing hyperparameters, and implementing cross-validation for better performance. Let me know if you'd like a downloadable file or further explanations!
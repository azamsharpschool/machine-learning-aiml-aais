### **Walkthrough: Real-World Scenario for Decision Trees in Classification**

---

**Scenario:** **Classifying Loan Applicants Based on Creditworthiness**

---

### **Objective:**  
Use a decision tree to classify loan applicants as "Approve" or "Reject" based on their financial information and other attributes.

---

### **Background:**
Banks often need to decide whether to approve a loan application. A decision tree model can analyze past loan data to create a classification rule that predicts approval or rejection based on applicant attributes such as income, credit score, loan amount, and debt-to-income ratio.

---

### **Dataset Description:**
The dataset contains information about previous applicants:

| **Applicant ID** | **Income ($)** | **Credit Score** | **Loan Amount ($)** | **Debt-to-Income Ratio (%)** | **Loan Status** |
|-------------------|----------------|------------------|----------------------|-----------------------------|-----------------|
| 1                 | 50,000         | 700              | 10,000              | 20                          | Approve         |
| 2                 | 30,000         | 650              | 20,000              | 40                          | Reject          |
| 3                 | 80,000         | 750              | 15,000              | 15                          | Approve         |
| 4                 | 25,000         | 600              | 5,000               | 50                          | Reject          |

**Features:**  
- **Income:** Annual income of the applicant.  
- **Credit Score:** A numerical representation of the applicant's credit history.  
- **Loan Amount:** Amount requested by the applicant.  
- **Debt-to-Income Ratio:** Percentage of monthly income used to pay debts.

**Target:**  
- **Loan Status:** Whether the loan application was "Approve" or "Reject."

---

### **Step-by-Step Walkthrough**

---

#### **Step 1: Load the Dataset**
Start by loading the dataset into Python:

```python
import pandas as pd

# Sample dataset
data = {
    'Income': [50000, 30000, 80000, 25000],
    'Credit Score': [700, 650, 750, 600],
    'Loan Amount': [10000, 20000, 15000, 5000],
    'Debt-to-Income Ratio': [20, 40, 15, 50],
    'Loan Status': ['Approve', 'Reject', 'Approve', 'Reject']
}

df = pd.DataFrame(data)
```

---

#### **Step 2: Encode the Target Variable**
Since "Loan Status" is categorical, encode it into numeric values:

```python
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
df['Loan Status'] = encoder.fit_transform(df['Loan Status'])  # Approve: 1, Reject: 0
```

---

#### **Step 3: Train-Test Split**
Split the dataset into training and testing sets:

```python
from sklearn.model_selection import train_test_split

X = df[['Income', 'Credit Score', 'Loan Amount', 'Debt-to-Income Ratio']]  # Features
y = df['Loan Status']  # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
```

---

#### **Step 4: Train a Decision Tree Classifier**
Train a decision tree classifier using Scikit-learn:

```python
from sklearn.tree import DecisionTreeClassifier

# Create and train the decision tree
classifier = DecisionTreeClassifier(max_depth=3, random_state=42)
classifier.fit(X_train, y_train)
```

---

#### **Step 5: Visualize the Decision Tree**
Visualize the decision tree to understand the classification rules:

```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plot_tree(classifier, feature_names=X.columns, class_names=['Reject', 'Approve'], filled=True)
plt.show()
```

The visualization will show rules like:  
- If **Credit Score ≥ 700**, then "Approve."  
- Else, if **Debt-to-Income Ratio < 30**, then "Approve."  
- Otherwise, "Reject."

---

#### **Step 6: Test the Model**
Evaluate the model's performance on the test data:

```python
from sklearn.metrics import accuracy_score

y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%")
```

---

### **Real-World Insights**

1. **Interpretable Results:**  
   Decision trees provide clear rules (e.g., "Approve if Credit Score ≥ 700"). These rules are easily explainable to stakeholders.

2. **Flexibility:**  
   The tree can handle both numeric (Income, Credit Score) and categorical data.

3. **Scalability:**  
   The method can be applied to much larger datasets for real-world scenarios.

---

### **Extension:**
- Try tuning hyperparameters like `max_depth` or `min_samples_split` to improve the model.  
- Apply the model to predict the status of new loan applicants with unseen data.

---

### **Outcome:**  
Students will learn how decision trees classify data, visualize decision-making rules, and evaluate the model's accuracy in a real-world problem.
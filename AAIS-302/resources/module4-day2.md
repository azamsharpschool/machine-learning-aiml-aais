### Walkthrough: Real-Life Example of Decision Trees – Loan Approval

This walkthrough will guide you step-by-step through implementing a simple decision tree to decide whether a loan application should be approved or rejected based on a few factors.

[Download Dataset](loan_decision_data.csv)

---

### **Scenario**

You are a loan officer. Your task is to decide whether to approve or reject loan applications. The decision is based on the following criteria:

1. **Applicant Income**: Greater than $50,000.  
2. **Credit Score**: Greater than 700.  
3. **Loan Amount**: Less than or equal to $100,000.

---

### **Step 1: Create the Decision Tree Structure**

The decision tree for this scenario would look like this:

```
          [Income > 50k?]
             /      \
          Yes        No
         /             \
 [Credit Score > 700?]  Reject
         /       \
      Yes        No
     /            \
[Loan <= 100k?]  Reject
    /     \
 Approve  Reject
```

---

### **Step 2: Understand the Dataset**

Your dataset might look like this:

| Income  | Credit Score | Loan Amount | Decision  |
|---------|--------------|-------------|-----------|
| 60,000  | 750          | 90,000      | Approve   |
| 40,000  | 710          | 50,000      | Reject    |
| 55,000  | 680          | 80,000      | Reject    |
| 70,000  | 720          | 120,000     | Reject    |
| 65,000  | 800          | 95,000      | Approve   |

---

### **Step 3: Define the Decision Rules**

Translate the decision tree logic into plain rules:

1. If income <= $50,000 → Reject.  
2. If income > $50,000:  
   - If credit score <= 700 → Reject.  
   - If credit score > 700:  
     - If loan amount > $100,000 → Reject.  
     - Otherwise → Approve.

---

### **Step 4: Build the Decision Tree in Python**

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas as pd

# Step 4.1: Create the dataset
data = {
    "Income": [60000, 40000, 55000, 70000, 65000],
    "CreditScore": [750, 710, 680, 720, 800],
    "LoanAmount": [90000, 50000, 80000, 120000, 95000],
    "Decision": [1, 0, 0, 0, 1]  # 1 = Approve, 0 = Reject
}

df = pd.DataFrame(data)

# Step 4.2: Define features and target
X = df[["Income", "CreditScore", "LoanAmount"]]
y = df["Decision"]

# Step 4.3: Create and train the model
model = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
model.fit(X, y)

# Step 4.4: Visualize the tree
tree.plot_tree(model, feature_names=["Income", "CreditScore", "LoanAmount"], class_names=["Reject", "Approve"], filled=True)
```

---

### **Step 5: Predict Loan Decisions**

Test the decision tree with new data:

```python
# New applicants
new_applicants = pd.DataFrame({
    "Income": [45000, 75000, 65000],
    "CreditScore": [720, 650, 800],
    "LoanAmount": [85000, 120000, 95000]
})

# Predict
predictions = model.predict(new_applicants)
print(predictions)  # Output: [0, 0, 1]
```

**Interpretation**:  
- Applicant 1: Reject (low income).  
- Applicant 2: Reject (loan amount too high).  
- Applicant 3: Approve (meets all criteria).

---

### **Step 6: Validate the Model**

Check accuracy using the original dataset:

```python
from sklearn.metrics import accuracy_score

# Predict on the training set
y_pred = model.predict(X)

# Calculate accuracy
accuracy = accuracy_score(y, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
```

---

### **Step 7: Explainability with Rules**

Translate the model into human-readable rules:

- If Income ≤ 50,000 → Reject.  
- If Income > 50,000 and Credit Score ≤ 700 → Reject.  
- If Income > 50,000 and Credit Score > 700 and Loan Amount ≤ 100,000 → Approve.  
- Otherwise → Reject.

---

### **Real-Life Applications**

1. **Banking**: Automating loan approvals.  
2. **Healthcare**: Diagnosing diseases based on symptoms.  
3. **E-commerce**: Personalizing product recommendations.

---

### **End of Walkthrough**

This step-by-step process illustrates how decision trees can be applied in real-world scenarios. You’ve built and tested a decision tree, making it easy to understand and visualize decisions.
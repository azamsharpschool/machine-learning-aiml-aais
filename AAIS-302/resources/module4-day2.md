
# 🌳 Logistic Decision-Making with Decision Trees

### Walkthrough: Real-Life Example of Decision Trees – Loan Approval

---

## 🎯 Objective

In this walkthrough, you’ll learn how to use **decision trees** to decide whether a loan should be **approved** or **rejected** based on:

* Income
* Credit Score
* Loan Amount

We’ll walk through how to build, visualize, interpret, and test a decision tree using real-world data and `scikit-learn`.

---

## 🏦 Scenario: You’re a Loan Officer

As a loan officer, your job is to automate the loan decision process using the following business rules:

* ✅ **Income > \$50,000**
* ✅ **Credit Score > 700**
* ✅ **Loan Amount ≤ \$100,000**

Only when **all** criteria are met is the loan approved.

---

## 🔧 Step 1: Visualize the Decision Tree Logic

Here’s how the logic breaks down into a tree:

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

## 📊 Step 2: Dataset Preview

Your dataset might look like this:

| Income | Credit Score | Loan Amount | Decision |
| ------ | ------------ | ----------- | -------- |
| 60000  | 750          | 90000       | Approve  |
| 40000  | 710          | 50000       | Reject   |
| 55000  | 680          | 80000       | Reject   |
| 70000  | 720          | 120000      | Reject   |
| 65000  | 800          | 95000       | Approve  |

We encode `Decision` as:

* **1** = Approve
* **0** = Reject

---

## 🧠 Step 3: Translate Rules into Plain Logic

| Rule                                                         | Outcome |
| ------------------------------------------------------------ | ------- |
| If Income ≤ 50,000                                           | Reject  |
| If Income > 50,000 AND Credit Score ≤ 700                    | Reject  |
| If Income > 50,000 AND Credit Score > 700 AND Loan > 100,000 | Reject  |
| If Income > 50,000 AND Credit Score > 700 AND Loan ≤ 100,000 | Approve |

---

## 🧑‍💻 Step 4: Build the Decision Tree with Python

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas as pd
import matplotlib.pyplot as plt

# Step 4.1: Dataset
data = {
    "Income": [60000, 40000, 55000, 70000, 65000],
    "CreditScore": [750, 710, 680, 720, 800],
    "LoanAmount": [90000, 50000, 80000, 120000, 95000],
    "Decision": [1, 0, 0, 0, 1]  # 1 = Approve, 0 = Reject
}

df = pd.DataFrame(data)

# Step 4.2: Features and target
X = df[["Income", "CreditScore", "LoanAmount"]]
y = df["Decision"]

# Step 4.3: Train the model
model = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
model.fit(X, y)

# Step 4.4: Visualize the tree
plt.figure(figsize=(10, 6))
tree.plot_tree(
    model,
    feature_names=["Income", "CreditScore", "LoanAmount"],
    class_names=["Reject", "Approve"],
    filled=True
)
plt.show()
```

---

## 🔮 Step 5: Make Predictions on New Applicants

```python
# Step 5.1: New data
new_applicants = pd.DataFrame({
    "Income": [45000, 75000, 65000],
    "CreditScore": [720, 650, 800],
    "LoanAmount": [85000, 120000, 95000]
})

# Step 5.2: Predict
predictions = model.predict(new_applicants)
print(predictions)  # Output: [0, 0, 1]
```

### ✅ Interpretation:

| Applicant | Decision | Reason             |
| --------- | -------- | ------------------ |
| #1        | Reject   | Low income         |
| #2        | Reject   | Loan too high      |
| #3        | Approve  | Meets all criteria |

---

## 📈 Step 6: Evaluate the Model

```python
from sklearn.metrics import accuracy_score

# Predict on training data
y_pred = model.predict(X)

# Accuracy
accuracy = accuracy_score(y, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
```

This tells you how well the model performs on known data.

---

## 🔍 Step 7: Extract Rules for Human Readability

You can explain the decision logic in natural language:

```text
If Income ≤ 50,000 → Reject  
Else if Credit Score ≤ 700 → Reject  
Else if Loan Amount > 100,000 → Reject  
Else → Approve  
```

This makes it easy to present your model to non-technical stakeholders.

---

## 💼 Real-World Use Cases

* **Banking**: Loan approval, credit risk assessment
* **Healthcare**: Predicting disease from patient symptoms
* **Retail**: Customer churn prediction
* **Insurance**: Approving claims based on fraud probability

---

## 📌 Summary

| Step | Description                        |
| ---- | ---------------------------------- |
| 1️⃣  | Visualize the decision logic       |
| 2️⃣  | Prepare dataset                    |
| 3️⃣  | Define rules                       |
| 4️⃣  | Train and visualize the tree       |
| 5️⃣  | Test with new data                 |
| 6️⃣  | Evaluate accuracy                  |
| 7️⃣  | Translate into plain-English rules |

---


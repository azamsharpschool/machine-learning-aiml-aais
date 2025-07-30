
# 🧪 Exercise: Predicting Loan Approval with Logistic Regression

[Download Dataset](loan_approval_100_rows.csv)

## 🎯 Objective

In this exercise, you will build a **logistic regression model** to predict whether a person’s **loan will be approved** or not based on their financial profile.

---

## 🧠 Background

You work for a fintech company offering personal loans. Your team wants to automate the decision process by predicting loan approval outcomes using past data.

The dataset includes:

| Income | Credit Score | Loan Amount | Approved |
| ------ | ------------ | ----------- | -------- |
| 55000  | 720          | 10000       | 1        |
| 30000  | 680          | 5000        | 0        |
| ...    | ...          | ...         | ...      |

* **Income**: Annual income in USD
* **Credit Score**: FICO score (300–850 scale)
* **Loan Amount**: Requested loan amount
* **Approved**: Target variable — 1 = Approved, 0 = Not Approved

---

## 🛠️ Instructions

### 🔹 Step 1: Load the Dataset from CSV

Download and load the dataset using `pandas`:

```python
import pandas as pd

# Load the loan approval dataset
df = pd.read_csv("loan_approval_100_rows.csv")

# Preview the dataset
df.head()
```

---

### 🔹 Step 2: Explore the Data

* Check the shape and summary statistics of the dataset.
* Plot histograms for `Income`, `Credit_Score`, and `Loan_Amount`.

---

### 🔹 Step 3: Prepare the Features and Target

* Define `X` as the feature matrix: `["Income", "Credit_Score", "Loan_Amount"]`
* Define `y` as the target: `Approved`

---

### 🔹 Step 4: Split the Data

Use `train_test_split` to divide data into training and testing sets (e.g., 80/20 split).

---

### 🔹 Step 5: Train the Logistic Regression Model

* Use `sklearn.linear_model.LogisticRegression` to fit the model.
* Train it using the training set.

---

### 🔹 Step 6: Make Predictions and Evaluate

* Use the model to predict on the test set.
* Evaluate using:

  * Accuracy
  * Confusion Matrix
  * Classification Report

✅ *Bonus*: Visualize decision boundaries (optional for advanced learners).

---

## 📝 Deliverables

* Notebook or script with:

  * Data creation and exploration
  * Logistic regression training
  * Accuracy and evaluation output


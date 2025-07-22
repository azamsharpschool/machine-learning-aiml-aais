
# 🌲 Random Forest Classifier — Full Walkthrough

### 🧠 Goal: Predict if a user will buy a smartphone


[Download Dataset](Synthetic_Smartphone_Purchase_Dataset.csv)

---

## 📘 What is Random Forest?

Random Forest is a **supervised machine learning algorithm** that combines the predictions of multiple **decision trees** to make a final prediction.

Imagine asking a group of friends (trees) to vote — each gives their opinion (yes or no), and the final decision is based on the majority vote. This approach improves **accuracy** and reduces **overfitting**.

---

## 🔧 Tools You'll Use

* `pandas`: for handling data
* `scikit-learn`: for model training, splitting, and evaluation
* `matplotlib`: for visualizing the trees

---

## 🧪 Scenario:

You’re building a model to predict whether someone will **buy a smartphone**, based on:

* **Age**
* **Income**
* **IsStudent** (Yes/No)

---

## ✅ Step-by-Step Guide

### 🟦 Step 1: Setup Your Dataset

```python
import pandas as pd

data = {
    'Age': [22, 35, 58, 27, 45, 21, 36, 50],
    'Income': [25000, 60000, 85000, 30000, 70000, 18000, 50000, 90000],
    'IsStudent': ['Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No'],
    'Purchased': [1, 1, 0, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)
print(df)
```

🧠 **Explanation**:
We're creating a small sample dataset manually. Each row is a person with their age, income, whether they’re a student, and if they bought a phone (`Purchased` = 1 or 0).

---

### 🟦 Step 2: Convert Categorical Data to Numbers

```python
df['IsStudent'] = df['IsStudent'].map({'Yes': 1, 'No': 0})
```

🧠 **Why?**
Machine learning models only work with numbers. We convert `'Yes'` to `1` and `'No'` to `0`.

---

### 🟦 Step 3: Define Features and Target

```python
X = df[['Age', 'Income', 'IsStudent']]  # Features
y = df['Purchased']                    # Target
```

🧠 **Explanation**:
We separate the **input features** (`X`) from the **label/output** we want to predict (`y`).

---

### 🟦 Step 4: Split the Data

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
```

🧠 **Explanation**:
We split our data into training (75%) and test (25%) sets so we can evaluate the model on data it hasn't seen before.

---

### 🟦 Step 5: Train the Random Forest

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=3, random_state=42)
model.fit(X_train, y_train)
```

🧠 **Explanation**:
We train a Random Forest with **3 trees**. The model learns patterns from the training data.

* `n_estimators=3`: builds 3 different decision trees.
* `random_state`: ensures consistent results each time you run the code.

---

### 🟦 Step 6: Make a Prediction

```python
new_user = pd.DataFrame({
    'Age': [28],
    'Income': [35000],
    'IsStudent': [1]
})

prediction = model.predict(new_user)
print("Will buy smartphone? (1=Yes, 0=No):", prediction[0])
```

🧠 **Explanation**:
We test the model on a **new user**: 28 years old, \$35k income, and a student.
The model returns `1` (yes) or `0` (no) based on what it learned.

---

### 🟦 Step 7: Visualize the Decision Trees

```python
from sklearn import tree
import matplotlib.pyplot as plt

for i, estimator in enumerate(model.estimators_):
    plt.figure(figsize=(10, 5))
    tree.plot_tree(estimator,
                   feature_names=['Age', 'Income', 'IsStudent'],
                   class_names=['No', 'Yes'],
                   filled=True,
                   rounded=True)
    plt.title(f"Tree {i+1}")
    plt.show()
```

🧠 **Explanation**:
Random Forest contains multiple trees. This code loops through each one and draws it so you can **see how the decisions are made**.

---

### 🟦 Step 8: Evaluate the Model

```python
from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
```

🧠 **Explanation**:
We evaluate the model’s performance by checking **how often it got the test data correct**.

---

## 🧠 Key Concepts Recap

| Term           | Meaning                                                              |
| -------------- | -------------------------------------------------------------------- |
| Random Forest  | A collection (ensemble) of decision trees                            |
| Overfitting    | When a model memorizes training data but performs poorly on new data |
| Generalization | The model's ability to perform well on new, unseen data              |
| `n_estimators` | The number of trees in the forest                                    |

---

### 🔄 Try This Exercise

Change the new user's data and predict again:

```python
# Try different combinations
new_user = pd.DataFrame({
    'Age': [52],
    'Income': [95000],
    'IsStudent': [0]
})
```


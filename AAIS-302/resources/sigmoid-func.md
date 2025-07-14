
## 🎓 In-Class Activity: Predicting Exam Pass/Fail Using Logistic Regression

[Download Dataset](exam_scores.csv)


### **Objective:**

Students will learn how the sigmoid function enables logistic regression to make probabilistic predictions. They will apply logistic regression to a dataset of 20,000 students and determine how study time affects exam success.

---

### 📦 Dataset Description

**File name:** `exam_scores.csv`
**Rows:** 20,000
**Columns:**

| Column         | Type  | Description                          |
| -------------- | ----- | ------------------------------------ |
| hours\_studied | float | Number of hours the student studied  |
| passed         | int   | 1 if the student passed, 0 otherwise |

Example (first 5 rows):

```csv
hours_studied,passed
1.5,0
3.2,0
4.5,1
6.8,1
0.9,0
...
```

---

### 🧪 Activity Instructions

#### Part 1: Visualizing the Data

1. Load the CSV file using pandas.
2. Plot a scatterplot of `hours_studied` vs `passed`.
3. Discuss:

   * Is the relationship linear?
   * Where does the class boundary seem to lie?

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('exam_scores.csv')

plt.scatter(df['hours_studied'], df['passed'], alpha=0.2)
plt.xlabel('Hours Studied')
plt.ylabel('Passed (0 or 1)')
plt.title('Study Hours vs Exam Outcome')
plt.show()
```

---

#### Part 2: Fitting a Logistic Regression Model

1. Use `sklearn` to fit a logistic regression model:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X = df[['hours_studied']]
y = df['passed']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
```

2. Print the model’s coefficient and intercept:

```python
print("Coefficient (w1):", model.coef_[0][0])
print("Intercept (w0):", model.intercept_[0])
```

---

#### Part 3: Predicting with the Sigmoid Function

Use the learned model to manually compute the sigmoid output for a student who studied 4 hours:

$$
z = w_0 + w_1 \cdot x
\quad\text{then}\quad
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

```python
import numpy as np

w0 = model.intercept_[0]
w1 = model.coef_[0][0]
x = 4  # hours studied

z = w0 + w1 * x
sigmoid = 1 / (1 + np.exp(-z))
print(f"Predicted probability of passing (4 hours): {sigmoid:.2f}")
```

---

#### Part 4: Evaluating Model Performance

1. Evaluate the model:

```python
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
```

2. Discussion questions:

   * What does the confusion matrix tell us?
   * Is the model fair for students who study fewer hours?

---

### 🔍 Discussion Questions

* Why can't we use linear regression for this problem?
* What role does the sigmoid function play in classification?
* How would the model change if we added more features like “sleep hours” or “stress level”?

---

### ✅ Learning Outcomes

By the end of this activity, students will:

* Understand how the sigmoid function transforms a linear model into a probabilistic classifier.
* Fit a logistic regression model on real data.
* Interpret the model’s predictions and parameters.
* Evaluate classification performance using real-world metrics.

---



# 🧠 Beginner Walkthrough: Understanding Model Evaluation Metrics

📍 *With Real-World Example: Medical Diagnosis*

---

## 🏥 Real-World Scenario: Predicting Heart Disease

Imagine you're building a machine learning model to **predict whether a patient has heart disease** (Positive) or not (Negative).
This is a **binary classification problem** and model evaluation becomes critical — especially in healthcare, where a **wrong prediction** can have serious consequences.

---

## 1. ✅ **Accuracy**

### 🔍 What is it?

Accuracy measures the **overall correctness** of your model.

### 🧮 Formula:

$$
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$$

### 🏥 Example:

Your model tested 100 patients.

* It predicted 90 correctly (both sick and healthy).
* So, **accuracy = 90%**.

But here's the catch:
Out of 100 patients, only 10 actually had heart disease. If your model predicted *“No disease”* for everyone, it would still be 90% accurate—**but completely useless** for detecting disease.

---

## 2. 📊 **Confusion Matrix**

### 🔍 What is it?

A table that tells you **exactly how your predictions break down**.

|                          | **Predicted: Has Disease** | **Predicted: No Disease** |
| ------------------------ | -------------------------- | ------------------------- |
| **Actually Has Disease** | ✅ True Positive (TP)       | ❌ False Negative (FN)     |
| **Actually Healthy**     | ❌ False Positive (FP)      | ✅ True Negative (TN)      |

### 🏥 Example:

Your model makes the following predictions:

* TP = 8 (caught 8 actual sick patients)
* FN = 2 (missed 2 sick patients)
* FP = 5 (said 5 healthy people are sick)
* TN = 85 (correctly predicted 85 healthy people)

```python
from sklearn.metrics import confusion_matrix

y_true = [1, 0, 1, 1, 0, 1, 0, 0]  # actual
y_pred = [1, 0, 1, 0, 0, 1, 1, 0]  # predicted

confusion_matrix(y_true, y_pred)
```

---

## 3. 🎯 **Precision, Recall, and F1 Score**

These are **especially useful in critical fields like medicine**, fraud detection, or spam filtering.

---

### 🎯 Precision

> "When the model says you're sick, how often is it correct?"

$$
\text{Precision} = \frac{TP}{TP + FP}
$$

🏥 High precision = fewer **false alarms** (false positives).
In our example:

$$
\text{Precision} = \frac{8}{8+5} = 0.615 = 61.5\%
$$

---

### 🆘 Recall (Sensitivity)

> "Out of all the people who are sick, how many did the model catch?"

$$
\text{Recall} = \frac{TP}{TP + FN}
$$

🏥 High recall = fewer **missed diagnoses** (false negatives).
In our example:

$$
\text{Recall} = \frac{8}{8+2} = 0.80 = 80\%
$$

---

### ⚖️ F1 Score

> A balance between precision and recall. Helpful when you need to **weigh both false positives and false negatives**.

$$
\text{F1 Score} = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}
$$

```python
from sklearn.metrics import precision_score, recall_score, f1_score

precision_score(y_true, y_pred)
recall_score(y_true, y_pred)
f1_score(y_true, y_pred)
```

---

## 4. 📈 ROC Curve (Optional)

> A **visual tool** to show how your model performs at various thresholds. It compares:

* **True Positive Rate (Recall)**
* **False Positive Rate**

A **perfect model** hugs the top-left corner.
The **AUC (Area Under Curve)** is a number between 0 and 1. Higher = better.

```python
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

fpr, tpr, _ = roc_curve(y_true, y_pred)
plt.plot(fpr, tpr, label="ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Heart Disease Prediction")
plt.legend()
plt.show()

print("AUC:", roc_auc_score(y_true, y_pred))
```

---

## 🧠 Summary Table (with Medical Context)

| Metric    | Meaning                                   | Healthcare Use                                                            |
| --------- | ----------------------------------------- | ------------------------------------------------------------------------- |
| Accuracy  | % of total correct predictions            | Quick snapshot, but may hide issues in imbalanced data                    |
| Precision | % of predicted positives that are correct | Important when **false positives** are costly (e.g., cancer treatment)    |
| Recall    | % of actual positives that were detected  | Crucial when **missing a positive** is dangerous (e.g., missed diagnosis) |
| F1 Score  | Harmonic mean of precision and recall     | Balanced metric for imbalanced datasets                                   |
| ROC Curve | Performance across thresholds             | Visual tool to compare models                                             |

---

## 📌 Suggested Assignment for Students:

1. Use a sample dataset (e.g., heart disease or spam email)
2. Build a logistic regression model
3. Calculate:

   * Confusion Matrix
   * Accuracy
   * Precision, Recall, F1
   * (Optional) ROC Curve
4. Write a short reflection:
   “If this model were used in healthcare, what would be the risks of false positives and false negatives?”


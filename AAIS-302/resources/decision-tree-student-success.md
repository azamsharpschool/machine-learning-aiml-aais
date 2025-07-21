
# 📘 Decision Trees for Student Success Prediction

### Walkthrough: Will a Student Pass the Exam?

[Download Dataset](student_exam_data_20k.csv)

---

## 🎯 Objective

In this walkthrough, you'll use a **decision tree** to predict whether a student will **pass** or **fail** based on:

* Hours Studied
* Attendance Rate (in %)
* Practice Tests Taken

---

## 🎓 Scenario: You’re a Data Analyst at a School

Your task is to build a decision-making system for early intervention. The rules your school has observed from past data are:

* ✅ **Hours Studied > 5**
* ✅ **Attendance Rate > 75%**
* ✅ **Practice Tests ≥ 2**

Only if all conditions are met is a student likely to pass.

---

## 🌲 Step 1: Visualize the Decision Tree Logic

```
         [Hours > 5?]
           /     \
         Yes     No
        /          \
[Attendance > 75%?]  Fail
     /      \
   Yes      No
   /         \
[Tests ≥ 2?] Fail
  /     \
Pass   Fail
```

---

## 📊 Step 2: Dataset Preview

| Hours | Attendance (%) | Practice Tests | Result |
| ----- | -------------- | -------------- | ------ |
| 6     | 80             | 2              | Pass   |
| 4     | 90             | 3              | Fail   |
| 7     | 60             | 2              | Fail   |
| 8     | 85             | 1              | Fail   |
| 10    | 95             | 3              | Pass   |

Encode `Result` as:

* **1** = Pass
* **0** = Fail

---

## 🧠 Step 3: Define the Logic in Plain Language

| Rule                                                     | Outcome |
| -------------------------------------------------------- | ------- |
| If Hours Studied ≤ 5                                     | Fail    |
| If Hours > 5 AND Attendance ≤ 75%                        | Fail    |
| If Hours > 5 AND Attendance > 75% AND Practice Tests < 2 | Fail    |
| If Hours > 5 AND Attendance > 75% AND Practice Tests ≥ 2 | Pass    |

---

## 🧑‍💻 Step 4: Build the Decision Tree in Python

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Step 4.1: Dataset
data = {
    "Hours": [6, 4, 7, 8, 10],
    "Attendance": [80, 90, 60, 85, 95],
    "PracticeTests": [2, 3, 2, 1, 3],
    "Result": [1, 0, 0, 0, 1]
}

df = pd.DataFrame(data)

# Step 4.2: Features and label
X = df[["Hours", "Attendance", "PracticeTests"]]
y = df["Result"]

# Step 4.3: Train model
clf = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
clf.fit(X, y)

# Step 4.4: Visualize tree
plt.figure(figsize=(10, 6))
plot_tree(clf, feature_names=["Hours", "Attendance", "PracticeTests"], 
          class_names=["Fail", "Pass"], filled=True)
plt.show()
```

---

## 🔮 Step 5: Predict Outcomes for New Students

```python
# Step 5.1: New students
new_students = pd.DataFrame({
    "Hours": [3, 9, 7],
    "Attendance": [80, 90, 78],
    "PracticeTests": [2, 1, 2]
})

# Step 5.2: Predictions
predictions = clf.predict(new_students)
print(predictions)  # Output: [0, 0, 1]
```

### ✅ Interpretation

| Student | Decision | Reason                    |
| ------- | -------- | ------------------------- |
| #1      | Fail     | Too few hours studied     |
| #2      | Fail     | Not enough practice tests |
| #3      | Pass     | Meets all criteria        |

---

## 📈 Step 6: Evaluate Model Performance

```python
from sklearn.metrics import accuracy_score

# Predict on training data
y_pred = clf.predict(X)

# Accuracy
accuracy = accuracy_score(y, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
```

---

## 🧾 Step 7: Extract Rules for Educators

```text
If Hours ≤ 5 → Fail  
Else if Attendance ≤ 75 → Fail  
Else if Practice Tests < 2 → Fail  
Else → Pass  
```

This helps school staff understand and trust the model.

---

## 🎯 Real-World Applications

* **Education**: Early academic risk detection
* **Tutoring Platforms**: Adaptive test prep strategies
* **HR Training**: Predict success in training programs
* **Online Courses**: Suggest additional support for at-risk learners

---

## ✅ Summary

| Step | Description                      |
| ---- | -------------------------------- |
| 1️⃣  | Visualize the decision flow      |
| 2️⃣  | Collect and prepare your dataset |
| 3️⃣  | Define rule logic                |
| 4️⃣  | Train and visualize the model    |
| 5️⃣  | Make predictions on new students |
| 6️⃣  | Evaluate performance             |
| 7️⃣  | Translate model into plain rules |


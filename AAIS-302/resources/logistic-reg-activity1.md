
## 🎯 Real-World Scenario: Will a Customer Buy the Product?

You're a marketing analyst. You want to **predict whether a customer will buy a product** based on how much time they spent on your product page.

---

## 🧾 Step 1: Create the Dataset

Here's a small, clean dataset:

| Time on Page (minutes) | Purchased (1 = Yes, 0 = No) |
| ---------------------- | --------------------------- |
| 1                      | 0                           |
| 2                      | 0                           |
| 3                      | 0                           |
| 4                      | 1                           |
| 5                      | 1                           |
| 6                      | 1                           |

In Python (using pandas):

```python
import pandas as pd

# Create dataset
data = pd.DataFrame({
    'time_on_page': [1, 2, 3, 4, 5, 6],
    'purchased': [0, 0, 0, 1, 1, 1]
})
print(data)
```

---

## 🧠 Step 2: What You’re Trying to Learn

You want to learn the relationship between:

* **time\_on\_page** (input `x`)
* **purchased** (output `y`)

Your goal:

> "Given how long a customer stays, can we predict if they’ll buy?"

---

## 🧮 Step 3: Train the Logistic Regression Model

In Python using scikit-learn:

```python
from sklearn.linear_model import LogisticRegression

# Inputs and outputs
X = data[['time_on_page']]  # features (must be 2D)
y = data['purchased']       # labels

# Create and train model
model = LogisticRegression()
model.fit(X, y)
```

---

## 🔍 Step 4: Make Predictions

```python
# Predict for a customer who spent 3.5 minutes on the page
prediction_proba = model.predict_proba([[3.5]])
prediction = model.predict([[3.5]])

print(f"Probability of purchase: {prediction_proba[0][1]:.4f}")
print(f"Predicted outcome: {'Buy' if prediction[0] == 1 else 'Not Buy'}")
```

Example Output:

```
Probability of purchase: 0.6225
Predicted outcome: Buy
```

---

## 📉 Step 5: What’s Happening Behind the Scenes

### 1. Model applies:

```
z = w₀ + w₁ * time_on_page
```

### 2. Then uses sigmoid function:

```
ŷ = 1 / (1 + e^(-z)) → gives a probability
```

### 3. Then rounds:

* If ŷ > 0.5 → Predict 1 (Buy)
* Else → Predict 0 (Not Buy)

---

## ✅ Why Logistic Regression Works Here

* It’s great when your outcome is **binary** (yes/no).
* It gives **probabilities**, not just yes/no answers.
* It’s **interpretable** — you can explain to your boss why the model made a prediction.

---

## 📊 Optional: Visualize It

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate a range of x values
x_values = np.linspace(0, 7, 100).reshape(-1, 1)
y_probas = model.predict_proba(x_values)[:, 1]

plt.scatter(data['time_on_page'], data['purchased'], color='blue', label='Data')
plt.plot(x_values, y_probas, color='red', label='Logistic Curve')
plt.xlabel('Time on Page (minutes)')
plt.ylabel('Probability of Purchase')
plt.title('Logistic Regression: Time vs Purchase')
plt.legend()
plt.grid(True)
plt.show()
```

---

## 🧩 Final Thoughts

| Step | What You Did                               |
| ---- | ------------------------------------------ |
| 1    | Collected realistic data                   |
| 2    | Used logistic regression to model it       |
| 3    | Got a probability prediction               |
| 4    | Interpreted the result in real-world terms |
| 5    | (Optional) Visualized the decision curve   |

---


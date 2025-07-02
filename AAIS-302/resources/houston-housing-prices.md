
# 🏠 Linear Regression with Scikit-learn: Houston Housing Prices

[Download Dataset](Houston_Housing_Prices__20k_Rows_.csv)

## 🧠 Objective

To predict house prices based on square footage using linear regression — one of the simplest and most interpretable models in machine learning.

---

## 📦 Step 1: Install and Import Required Libraries

First, make sure you have all necessary libraries. You can install them via:

```bash
pip install pandas scikit-learn matplotlib
```

Then import them:

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
```

---

## 📄 Step 2: Load the Dataset

If you're using the previously generated `houston_housing_df`, continue. Otherwise, load from CSV:

```python
# Load dataset from CSV (if applicable)
df = pd.read_csv("houston_housing.csv")  # replace with your filename
```

If using the generated DataFrame:

```python
# Assuming this was generated earlier in the notebook
df = houston_housing_df.copy()
```

---

## 🔍 Step 3: Explore the Data

Look at the first few rows and basic stats:

```python
print(df.head())
print(df.describe())
```

This tells you the range of square footage and prices, allowing you to spot any potential anomalies or scaling issues.

---

## 📊 Step 4: Visualize the Data

Plot the relationship between square footage and price:

```python
plt.figure(figsize=(10, 6))
plt.scatter(df['Square_Feet'], df['Price'], alpha=0.3, edgecolor='k')
plt.xlabel('Square Feet')
plt.ylabel('Price ($)')
plt.title('Houston House Prices by Square Footage')
plt.grid(True)
plt.show()
```

**Interpretation**: If the points form a roughly upward trend, that’s a good indicator that linear regression may work.

---

## ✂️ Step 5: Prepare the Data

### Separate the input (feature) and output (target):

```python
X = df[['Square_Feet']]  # Feature matrix must be 2D
y = df['Price']          # Target variable
```

### Split into training and testing sets:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

This ensures the model is trained on 80% of the data and evaluated on the remaining 20%.

---

## 🤖 Step 6: Train the Linear Regression Model

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

This fits a line to the training data:

$$
\text{Price} = \text{Intercept} + (\text{Coefficient} \times \text{Square_Feet})
$$

---

## 🔍 Step 7: View Model Parameters

```python
print(f"Intercept (Base price): ${model.intercept_:.2f}")
print(f"Coefficient (Price per Sq Ft): ${model.coef_[0]:.2f}")
```

> Example Output:
> Intercept: \$12,000
> Coefficient: \$132
> This means a home with 0 sq ft would theoretically cost \$12,000 (not realistic but mathematically true), and each additional square foot adds \$132 to the price.

---

## 📈 Step 8: Make Predictions

Use the test data to make predictions:

```python
y_pred = model.predict(X_test)
```

---

## 📊 Step 9: Visualize Predictions vs Actual

```python
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, alpha=0.3, label='Actual', edgecolor='k')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
plt.xlabel('Square Feet')
plt.ylabel('Price ($)')
plt.title('Predicted vs Actual House Prices')
plt.legend()
plt.grid(True)
plt.show()
```

This shows how well the regression line fits the actual data.

---

## 📏 Step 10: Evaluate the Model

Calculate standard regression metrics:

```python
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:,.2f}")
print(f"Root Mean Squared Error: {rmse:,.2f}")
print(f"R² Score: {r2:.4f}")
```

### Interpretation:

* **RMSE** gives an average dollar error (e.g., ±\$25,000).
* **R² Score** tells how well the model explains variance.

  * 1.0 = perfect prediction
  * 0.0 = no predictive power

---

## 🔮 Step 11: Make a Custom Prediction

How much would a 2,500 sq ft house cost?

```python
custom_sqft = pd.DataFrame({'Square_Feet': [2500]})
predicted_price = model.predict(custom_sqft)

print(f"Predicted price for 2,500 sq ft: ${predicted_price[0]:,.2f}")
```

---

## ✅ Summary

| Step | Action                         |
| ---- | ------------------------------ |
| 1    | Import libraries               |
| 2    | Load dataset                   |
| 3    | Explore and visualize          |
| 4    | Prepare training/testing sets  |
| 5    | Train linear regression model  |
| 6    | Evaluate performance           |
| 7    | Make predictions and visualize |


# 📅 Day 3: Data Normalization & Linear Regression – House Price Prediction

[Download Dataset](house_prices_20k.csv)

### 🎯 **Learning Objectives**

By the end of this walkthrough, you'll be able to:

* Normalize numeric data using Min-Max and Z-Score scaling
* Split a dataset into training and test sets
* Build a simple Linear Regression model to predict house prices
* Evaluate the model using MAE (Mean Absolute Error)

---

## 🛠️ Step 1: Setup and Load the Dataset

Make sure you’ve installed the required libraries:

```bash
pip install pandas scikit-learn matplotlib
```

Then import the necessary modules:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt
```

Now, load the dataset:

```python
df = pd.read_csv('house_prices_20k.csv')  # or 'house_prices.csv'
df.head()
```

---

## 🔍 Step 2: Inspect the Data

Check the structure and look for any missing values:

```python
print(df.info())
print(df.describe())
```

Confirm that both **Size** (independent variable) and **Price** (target variable) are numeric and non-null.

---

## 📐 Step 3: Normalize the “Size” Column

### 🔹 Option 1: **Min-Max Scaling** (Values between 0 and 1)

```python
min_max_scaler = MinMaxScaler()
df['Size_MinMax'] = min_max_scaler.fit_transform(df[['Size']])
```

### 🔹 Option 2: **Z-Score Standardization** (Mean = 0, Std Dev = 1)

```python
z_score_scaler = StandardScaler()
df['Size_ZScore'] = z_score_scaler.fit_transform(df[['Size']])
```

For this walkthrough, we’ll use the Z-Score version for training the model.

---

## 🧪 Step 4: Train/Test Split

Separate the input and output:

```python
X = df[['Size_ZScore']]
y = df['Price']
```

Split the data:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

---

## 🧠 Step 5: Train a Linear Regression Model

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

Get the slope and intercept of the regression line:

```python
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)
```

---

## 📈 Step 6: Make Predictions and Evaluate the Model

### 🔹 Predict on Test Set

```python
y_pred = model.predict(X_test)
```

### 🔹 Evaluate Using MAE

```python
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)
```

This tells us, on average, how far off our price predictions are.

---

## 📊 Step 7: Visualize the Results

Create a scatter plot of the actual vs predicted prices:

```python
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', alpha=0.5, label='Actual')
plt.scatter(X_test, y_pred, color='red', alpha=0.5, label='Predicted')
plt.title('Linear Regression: Actual vs Predicted Prices')
plt.xlabel('Normalized Size (Z-Score)')
plt.ylabel('Price')
plt.legend()
plt.show()
```

You can also plot the regression line over the original data to visualize the fit.

---

## 🧩 Challenge Exercises

1. **Try Min-Max scaling instead of Z-score. Does it improve MAE?**
2. **Add another feature (e.g., Location as a numeric value) and retrain.**
3. **Plot residuals (difference between actual and predicted values).**

---

## 🧠 What You Learned

✔ How to scale data using Min-Max and Z-Score
✔ How to build and train a simple regression model
✔ How to evaluate predictions using MAE
✔ How to visualize and interpret regression results


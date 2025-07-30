
# 🧪 Exercise: One-Hot Encoding with `pd.get_dummies()` for House Price Data

[Download Dataset](house_prices_100_rows.csv)

## 🎯 Objective

In this exercise, you'll learn how to use `pandas.get_dummies()` to transform categorical variables into numerical format using one-hot encoding—an essential step before applying machine learning algorithms.

---

## 📘 Instructions

Follow the steps below to complete the preprocessing task.

---

### 🔹 Step 1: Import the Required Library

```python
import pandas as pd
```

✅ *This will allow you to create and manipulate DataFrames.*

---

### 🔹 Step 2: Create the Dataset

Create the following DataFrame:

| Size   | Location | Price  |
| ------ | -------- | ------ |
| Small  | Urban    | 150000 |
| Medium | Suburban | 200000 |
| Large  | Rural    | 180000 |
| Medium | Urban    | 210000 |
| Small  | Suburban | 160000 |

✅ *Use `pd.DataFrame({...})` with a dictionary of lists.*

---

### 🔹 Step 3: Explore the Data

Print the DataFrame and verify that the `Size` and `Location` columns are **categorical**.

---

### 🔹 Step 4: Apply One-Hot Encoding using `pd.get_dummies()`

* Use `pd.get_dummies()` to encode both the `Size` and `Location` columns.
* Use the `columns` parameter to specify which columns to encode.
* Use `drop_first=True` to avoid multicollinearity by dropping the first category in each column.

✅ *Example Syntax:*

```python
df_encoded = pd.get_dummies(df, columns=["Size", "Location"], drop_first=True)
```

---

### 🔹 Step 5: Inspect the Final DataFrame

* Print the one-hot encoded DataFrame.
* Confirm that all categorical values are now represented as binary (0/1) columns, and the `Price` column remains unchanged.

---

## ✅ Bonus Challenge (Optional)

Use the encoded data to train a simple linear regression model to predict house prices using:

```python
from sklearn.linear_model import LinearRegression
```

---

## 📝 Deliverables

* A Python script or Jupyter notebook that:

  * Imports data
  * Applies one-hot encoding with `pd.get_dummies()`
  * Outputs the final, model-ready DataFrame


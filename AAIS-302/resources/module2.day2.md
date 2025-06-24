
# 📅 **Day 2: Handling Missing Data – Beginner Walkthrough**

---

## 🧠 Why Missing Data Matters

Before you build a model or visualize insights, you must check if your data is **complete and consistent**. Real-world data often has missing or incomplete values, and ignoring them can result in:

* Inaccurate predictions
* Misleading visualizations
* Crashes or errors during model training

> 🧩 **Analogy**: Imagine filling out a job application but skipping your work history. The recruiter won’t have a complete picture of your background—just like a model won't understand incomplete data.

---

## 📦 Use Case: Home Prices Dataset

We’ll work with a small dataset of home listings that includes:

* `Price`: The listed sale price of the house
* `Square_Feet`: Size of the house
* `Bedrooms`: Number of bedrooms
* `Location`: Neighborhood type (e.g., Urban, Rural)

Some of these fields will include **missing values**, simulating a real-world messy dataset.

---

## 🔧 Step 1: Set Up the Environment

### ✅ Install Required Packages

```bash
pip install pandas numpy
```

### ✅ Create the Dataset

You can simulate your own dataset with missing values:

```python
import pandas as pd
import numpy as np

# Create sample home prices dataset with missing values
data = {
    'Price': [300000, 400000, np.nan, 500000, 600000],
    'Square_Feet': [1500, 2000, 2500, np.nan, 3000],
    'Bedrooms': [3, 4, np.nan, 3, 5],
    'Location': ['Suburban', 'Urban', 'Urban', np.nan, 'Rural']
}

df = pd.DataFrame(data)
print(df)
```

---

## 🔍 Step 2: Identify Missing Data

### 🔹 Check for Any Missing Values

```python
print(df.isnull())
```

This returns a DataFrame with `True` or `False` for each missing value.

### 🔹 Count Missing Values in Each Column

```python
print("Missing values summary:")
print(df.isnull().sum())
```

**Expected Output:**

```
Price          1
Square_Feet    1
Bedrooms       1
Location       1
dtype: int64
```

---

## 🧼 Step 3: Strategies for Handling Missing Data

---

### 1. ❌ **Drop Missing Data**

#### Drop Rows (if any value is missing)

```python
df_dropped_rows = df.dropna()
print(df_dropped_rows)
```

| Price  | Square\_Feet | Bedrooms | Location |
| ------ | ------------ | -------- | -------- |
| 300000 | 1500         | 3        | Suburban |
| 400000 | 2000         | 4        | Urban    |
| 600000 | 3000         | 5        | Rural    |

#### Drop Columns (if missing values exist)

```python
df_dropped_columns = df.dropna(axis=1)
print(df_dropped_columns)
```

This removes entire columns with missing values—not recommended unless necessary.

---

### 2. 🔁 **Fill Missing Data (Imputation)**

#### 🔹 Numeric Data – Use **Mean**

```python
df['Price'] = df['Price'].fillna(df['Price'].mean())
df['Square_Feet'] = df['Square_Feet'].fillna(df['Square_Feet'].mean())
```

#### 🔹 Numeric Data – Use **Median**

```python
df['Bedrooms'] = df['Bedrooms'].fillna(df['Bedrooms'].median())
```

#### 🔹 Categorical Data – Use **Mode**

```python
df['Location'] = df['Location'].fillna(df['Location'].mode()[0])
```

📌 `.mean()` works well if the data is normally distributed.
📌 `.median()` is better for skewed data or when outliers exist.
📌 `.mode()` gives the most frequently occurring value.

---

## 🔍 Step 4: Review the Cleaned Dataset

```python
print(df)
```

**Final Output:**

```
      Price  Square_Feet  Bedrooms  Location
0  300000.0       1500.0       3.0  Suburban
1  400000.0       2000.0       4.0     Urban
2  450000.0       2500.0       3.0     Urban
3  500000.0       2250.0       3.0     Urban
4  600000.0       3000.0       5.0     Rural
```

Now the dataset is **complete and consistent**, ready for visualization or modeling.

---

## 🎯 Step 5: Hands-On Challenge

Try these tasks on your own:

1. 🔍 Identify all missing values
2. 🧹 Drop rows with missing values
3. 🔁 Fill numeric columns using the **mean**
4. 🔁 Fill `Location` using the **most common value (mode)**
5. 💾 Save the cleaned dataset:

```python
df.to_csv('home_prices_cleaned.csv', index=False)
```

---

## 🧠 Learning Outcomes

By the end of Day 2, you will:

* Understand how to detect missing data using `.isnull()` and `.sum()`
* Learn different strategies for handling missing values
* Practice using `.dropna()` and `.fillna()` with mean, median, and mode
* Be able to clean messy datasets for real-world use

---

## 🔍 Next Steps

* Explore `sklearn.impute` for machine learning-based imputation
* Try working with real housing datasets (Kaggle, data.gov)
* Combine missing data handling with normalization (coming soon on Day 3!)


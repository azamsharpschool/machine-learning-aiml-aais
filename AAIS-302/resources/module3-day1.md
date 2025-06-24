
# 🚗 Carvana Dataset Walkthrough – Data Exploration, Cleaning & ML Prep

---

## 🎯 **Learning Objectives**

By the end of this walkthrough, you will:

* Understand how to explore and clean a real-world dataset
* Visualize relationships between features like mileage, year, and price
* Prepare and evaluate a simple machine learning model
* Interpret model output with visual tools like residual plots and feature importance

---

## 📄 1. Dataset Overview

The Carvana dataset contains information about used cars listed for sale. It includes:

| Column  | Description                      |
| ------- | -------------------------------- |
| `Name`  | Model name and trim of the car   |
| `Year`  | Manufacturing year               |
| `Miles` | Mileage (number of miles driven) |
| `Price` | Listing price in USD             |

This type of data is common in predictive modeling problems like **used car price prediction**.

---

## 🔍 2. Basic Exploration

Start by inspecting the structure and health of your dataset:

```python
# Basic stats
print(carvana_df.describe())

# Check for missing values
print(carvana_df.isnull().sum())
```

### 📌 What to look for:

* Are any columns missing data?
* Are there unrealistic values (e.g., Year > current year)?
* Are all numeric columns stored in the correct format?

---

## 🧹 3. Data Cleaning

### 🛠️ Fixing an Incorrect Year

Suppose you find a year like `"20173"` in your data:

```python
carvana_df['Year'] = carvana_df['Year'].apply(lambda x: 2017 if x == 20173 else x)
```

### 🔁 Removing Duplicate Records

```python
duplicates = carvana_df.duplicated().sum()
print(f"Duplicate rows: {duplicates}")

# Drop duplicates
carvana_df = carvana_df.drop_duplicates()
```

---

## 📊 4. Data Visualization for Machine Learning

Visualizations can uncover trends, patterns, and outliers — all critical for modeling.

---

### 📈 A. Distribution of Car Prices

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(carvana_df['Price'], kde=True, bins=30)
plt.title('Distribution of Car Prices')
plt.xlabel('Price (USD)')
plt.ylabel('Frequency')
plt.show()
```

🔎 This helps assess:

* Price range
* Skewness (positive skew is common in car prices)
* Outliers

---

### 🔧 B. Price vs. Mileage

```python
sns.scatterplot(x='Miles', y='Price', data=carvana_df)
plt.title('Price vs. Mileage')
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.show()
```

🧠 Expect a **negative correlation**: more miles = lower price.

---

### 📅 C. Count of Cars by Year

```python
sns.countplot(x='Year', data=carvana_df)
plt.title('Number of Cars by Manufacturing Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
```

This shows the age distribution of the cars listed.

---

### 🔥 D. Correlation Heatmap

```python
sns.heatmap(carvana_df[['Year', 'Miles', 'Price']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Between Features')
plt.show()
```

This can inform which features to include in a regression model.

---

## 🧠 5. Visualizations for Machine Learning

Now that we’ve explored the data, let’s use machine learning to:

* Predict price
* Understand feature importance
* Evaluate model accuracy with residuals

---

### 🧪 A. Feature Importance (Random Forest)

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

X = carvana_df[['Year', 'Miles']]
y = carvana_df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(X_train, y_train)
```

#### 📊 Visualize Feature Importance

```python
importances = model.feature_importances_

sns.barplot(x=X.columns, y=importances)
plt.title('Feature Importance for Predicting Price')
plt.show()
```

💡 This helps explain which features matter most — useful in business and data storytelling.

---

### 📉 B. Residual Plot (Model Evaluation)

```python
from sklearn.metrics import mean_squared_error

y_pred = model.predict(X_test)
residuals = y_test - y_pred

sns.scatterplot(x=y_pred, y=residuals)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals vs. Predicted Price')
plt.xlabel('Predicted Price')
plt.ylabel('Residuals')
plt.show()
```

✅ A good model will have **residuals centered around zero** with no clear pattern.

---

## ✅ 6. Wrap-Up and Learning Outcomes

In this walkthrough, you’ve:

* 🧼 Cleaned and corrected errors in real-world car data
* 📊 Used visual tools to explore relationships
* 🔍 Identified meaningful features for modeling
* 🤖 Built a simple model to predict car price
* 📉 Evaluated model performance using residuals

---

## 🧩 Suggested Challenges

1. Add `Brand` as a new feature by splitting the `Name` column.
2. Use `.groupby()` to find the average price by `Year`.
3. Apply Min-Max or Z-score normalization to `Miles` and compare model performance.
4. Try a different regression model (e.g., LinearRegression or XGBoost).


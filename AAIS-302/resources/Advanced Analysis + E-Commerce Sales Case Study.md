
# 📅 Day 4: Advanced Analysis + E-Commerce Sales Case Study

[Download Dataset](ecommerce_sales_20k.csv)

### 🎯 **Learning Objectives**

By the end of this walkthrough, you’ll be able to:

* Load and clean a real-world dataset
* Perform filtering, grouping, and sorting
* Visualize key trends using Pandas and Matplotlib
* Answer business-oriented questions from data
* Prepare summary reports using aggregated insights

---

## 🛒 Case Study: E-Commerce Sales Analysis

You're hired as a junior data analyst at an online retailer. Your manager has given you a sales dataset and asked for insights into **product performance, revenue trends, and regional behavior**.

---

## 🛠️ Step 1: Setup and Load the Dataset

You’ll need these libraries:

```bash
pip install pandas matplotlib seaborn
```

Then import the necessary modules:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

Now, load your dataset:

```python
df = pd.read_csv('ecommerce_sales.csv')
df.head()
```

### 🔹 Sample Schema

| OrderID | Product | Category    | Quantity | Price  | Region     | OrderDate  |
| ------- | ------- | ----------- | -------- | ------ | ---------- | ---------- |
| 1001    | T-Shirt | Apparel     | 2        | 19.99  | West Coast | 2023-01-03 |
| 1002    | Laptop  | Electronics | 1        | 799.99 | Northeast  | 2023-01-05 |

---

## 🔍 Step 2: Explore and Clean the Data

```python
print(df.info())
print(df.describe())
print(df.isnull().sum())
```

### ➤ Tasks

* Ensure `OrderDate` is a `datetime` column:

```python
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
```

* Fill missing values if needed (e.g., `Price`, `Quantity`)

```python
df['Price'].fillna(df['Price'].mean(), inplace=True)
df['Quantity'].fillna(1, inplace=True)
```

---

## 📈 Step 3: Create Derived Columns

Add a `TotalSale` column for better insights:

```python
df['TotalSale'] = df['Quantity'] * df['Price']
```

---

## 📊 Step 4: Answer Key Business Questions

---

### ❓ **1. What is the top-selling product (by quantity)?**

```python
top_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print(top_products.head(10))
```

📌 *Bonus: Visualize top 10 products*

```python
top_products.head(10).plot(kind='bar', title='Top-Selling Products')
plt.ylabel('Total Quantity Sold')
plt.show()
```

---

### ❓ **2. Which category had the most revenue?**

```python
revenue_by_category = df.groupby('Category')['TotalSale'].sum().sort_values(ascending=False)
print(revenue_by_category)
```

📌 *Bonus: Pie chart for revenue distribution*

```python
revenue_by_category.plot(kind='pie', autopct='%1.1f%%', title='Revenue by Category')
plt.ylabel('')
plt.show()
```

---

### ❓ **3. What is the average order value per region?**

```python
avg_order_value = df.groupby('Region')['TotalSale'].mean().sort_values(ascending=False)
print(avg_order_value)
```

📌 *Bonus: Horizontal bar chart*

```python
avg_order_value.plot(kind='barh', title='Average Order Value by Region')
plt.xlabel('Average Order Value ($)')
plt.show()
```

---

### ❓ **4. How do sales vary over time?**

```python
daily_sales = df.groupby('OrderDate')['TotalSale'].sum()
daily_sales.plot(figsize=(12, 5), title='Total Daily Sales')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.grid()
plt.show()
```

📌 *Optional:* Group by month or week for long-term trend:

```python
monthly_sales = df.resample('M', on='OrderDate')['TotalSale'].sum()
monthly_sales.plot(marker='o', title='Monthly Sales Trend')
```

---

## 📦 Step 5: Export Summary Report

```python
summary = df.groupby(['Category', 'Region'])['TotalSale'].sum().reset_index()
summary.to_csv('ecommerce_summary.csv', index=False)
```

---

## 🧩 Mini Project Prompt

Ask learners to choose a dataset of interest (e.g., movies, books, housing, products) and perform:

### ✅ Required:

1. Load the dataset and check for nulls
2. Create at least one new column (e.g., `total`, `score`, `category`)
3. Group by at least one categorical variable
4. Sort and summarize insights
5. Create 1–2 plots

### 📝 Optional Report:

Have learners write a 2–3 paragraph summary of their findings and visualize one business metric.

---

## 🎓 Summary & Reflection

Today you learned how to:

* Clean and enhance a real-world dataset
* Perform multi-level grouping and aggregations
* Answer business questions with data
* Visualize key metrics using Pandas & Matplotlib
* Prepare a shareable summary report


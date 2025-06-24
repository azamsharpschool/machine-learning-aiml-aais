
## 📅 **Real-Life Walkthrough: Day 4 – Bringing It All Together**

**Objective:** Use real sales data to build meaningful insights through filtering, grouping, and visualizations. Ideal for beginners stepping into exploratory data analysis (EDA) using Python and pandas.

### 🔗 Dataset Used:

`customer_shopping_data.csv`

---

### 🔧 **Activity 1: Load and Explore the Dataset**

#### **Step 1: Import Pandas**

```python
import pandas as pd
```

#### **Step 2: Load the CSV File**

```python
sales_data = pd.read_csv("/content/sample_data/customer_shopping_data.csv")
sales_data.head()
```

#### **Step 3: Dataset Overview**

Check the number of records and columns:

```python
len(sales_data)  # Number of rows
sales_data.columns  # List of column names
```

#### **Step 4: Check for Missing Values**

```python
sales_data.isnull().sum()
```

✅ *Purpose:* Clean datasets are critical for accurate analysis. This step checks data quality.

---

### 🔧 **Activity 2: Filtering and Cleaning**

#### **Step 1: Filter High-Value Transactions**

```python
large_sales = sales_data[sales_data["price"] > 4900]
```

✅ *Why?* Focus on sales that generate substantial revenue for insights.

---

### 📊 **Activity 3: Grouping and Aggregation**

#### **Step 1: Total Sales by Product Category**

```python
sales_by_category = sales_data.groupby("product_category")["price"].sum().sort_values(ascending=False)
print(sales_by_category)
```

#### **Step 2: Average Order Value by Gender**

```python
average_order_by_gender = sales_data.groupby("gender")["price"].mean()
print(average_order_by_gender)
```

#### **Step 3: Revenue by Category and Gender**

```python
category_gender = sales_data.groupby(["product_category", "gender"])["price"].sum().unstack()
print(category_gender)
```

---

### 📈 **Activity 4: Visualization**

#### **Step 1: Import Matplotlib**

```python
import matplotlib.pyplot as plt
```

#### **Step 2: Bar Chart – Sales by Category**

```python
sales_by_category.plot(kind="bar", color="skyblue", edgecolor="black", figsize=(10,6))
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.tight_layout()
plt.show()
```

#### **Step 3: Pie Chart – Gender Distribution**

```python
sales_data["gender"].value_counts().plot(kind="pie", autopct='%1.1f%%', startangle=90, figsize=(6, 6))
plt.title("Customer Gender Distribution")
plt.ylabel("")
plt.show()
```

#### **Step 4: Scatter Plot – Age vs Price**

```python
plt.scatter(sales_data["age"], sales_data["price"], alpha=0.5, c="purple")
plt.title("Age vs Price")
plt.xlabel("Age")
plt.ylabel("Spending ($)")
plt.grid(True)
plt.show()
```

---

### ✅ **Activity 5: Summary and Report Generation**

1. **Top-Selling Product Category:** Use the highest value from `sales_by_category`.
2. **Gender with Highest Average Spending:** Use `average_order_by_gender`.
3. **Customer Age Insights:** Review scatterplot – are older customers spending more?

---

### 💡 **Final Mini Project for Learners**

**Goal:** Apply what you’ve learned on the dataset.

**Tasks:**

* Load and clean the dataset.
* Create a summary report:

  * Highest revenue product category
  * Customer demographics (age, gender) vs. spending
  * Pie chart of gender or category split
* Export a PNG chart using:

  ```python
  plt.savefig("final_report_chart.png", dpi=300)
  ```

---

### 🧠 **Key Takeaways**

* Data cleaning ensures reliable analysis.
* Grouping helps summarize trends.
* Visualizations reveal insights hidden in raw data.
* Real datasets help connect theory to practice.


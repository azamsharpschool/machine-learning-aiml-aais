

# 📦 **Day 4: Combining and Reshaping Data Walkthrough**

---

## 🎯 **Lecture Objectives**

By the end of this lesson, you’ll be able to:

✅ Combine multiple datasets using merge and concat
✅ Reshape wide or long datasets using `.pivot()` and `.melt()`
✅ Aggregate data using `.groupby()` for summaries and reports

---

## 🧩 Why This Matters

In real-world data workflows:

* Data often comes from **multiple sources** (e.g., customers table, transactions table).
* You need to **reshape or transform** it for visualizations or machine learning.
* Grouping and summarizing data is essential for decision-making.

> Think of combining data like assembling a puzzle — you’re connecting pieces to see the bigger picture.

---

## 🧱 Section 1: Combining DataFrames

---

### 🔗 1.1 Merging Data with `.merge()`

#### 🧠 Concept:

Merging joins two DataFrames using a common key — similar to **SQL joins**.

#### 🔧 Code Example:

```python
import pandas as pd

# Customer information
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})

# Customer scores
df2 = pd.DataFrame({'ID': [1, 2], 'Score': [95, 88]})

# Merge them on 'ID'
merged_df = pd.merge(df1, df2, on='ID')
print(merged_df)
```

#### 🧾 Output:

```
   ID   Name  Score
0   1  Alice     95
1   2    Bob     88
```

📌 Use `how='left'`, `how='right'`, or `how='outer'` to control join behavior.

---

### ➕ 1.2 Concatenating DataFrames with `pd.concat()`

#### 🧠 Concept:

* Stack multiple DataFrames **vertically** (row-wise) or **horizontally** (column-wise).
* Useful when appending or combining batch data.

#### 🔧 Example:

```python
df1 = pd.DataFrame({'Name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'Score': [95, 88]})

# Combine side-by-side (axis=1)
concat_df = pd.concat([df1, df2], axis=1)
print(concat_df)
```

#### 🧾 Output:

```
    Name  Score
0  Alice     95
1    Bob     88
```

📌 `axis=0` stacks rows; `axis=1` stacks columns. Use `ignore_index=True` when stacking rows.

---

## 🔄 Section 2: Reshaping DataFrames

---

### 🔁 2.1 Reshaping with `.pivot()`

#### 🧠 Concept:

Restructure a DataFrame to turn **row values into columns**, making data easier to analyze or visualize.

#### 🔧 Example:

```python
df = pd.DataFrame({
    'species': ['dog', 'dog', 'cat', 'cat'],
    'measurement': ['height', 'weight', 'height', 'weight'],
    'value': [50, 20, 35, 10]
})

pivot_df = df.pivot(index='species', columns='measurement', values='value')
print(pivot_df)
```

#### 🧾 Output:

```
measurement  height  weight
species                    
cat            35      10
dog            50      20
```

📌 `.pivot()` **fails** if there are duplicate index-column combinations. Use `.pivot_table()` to safely handle aggregation.

---

### 🔄 2.2 Unpivoting with `.melt()`

#### 🧠 Concept:

`.melt()` takes **wide data** and makes it **long**, useful for plotting or normalizing structures.

#### 🔧 Example:

```python
melt_df = pivot_df.reset_index().melt(id_vars='species', value_vars=['height', 'weight'])
print(melt_df)
```

#### 🧾 Output:

```
  species measurement  value
0     cat      height     35
1     dog      height     50
2     cat      weight     10
3     dog      weight     20
```

📌 `.melt()` is powerful when data has columns for each time period or measurement that should be stacked into rows.

---

### 📊 2.3 Grouping and Aggregation with `.groupby()`

#### 🧠 Concept:

Groups rows based on a column, then applies aggregation functions like `mean`, `sum`, `count`, etc.

#### 🔧 Example:

```python
grouped_df = df.groupby('species').agg({'value': 'mean'})
print(grouped_df)
```

#### 🧾 Output:

```
         value
species       
cat       22.5
dog       35.0
```

📌 Use `.reset_index()` if you want to flatten the grouped output for merging or saving.

---

## 🧪 Hands-On Activities

### ✅ Activity 1: Merge on Common Key

```python
df_customers = pd.DataFrame({'CustomerID': [1, 2], 'Name': ['Alice', 'Bob']})
df_orders = pd.DataFrame({'CustomerID': [1, 2], 'Orders': [3, 5]})

df_combined = pd.merge(df_customers, df_orders, on='CustomerID')
```

### ✅ Activity 2: Pivot Your Data

```python
df_sales = pd.DataFrame({
    'Month': ['Jan', 'Jan', 'Feb', 'Feb'],
    'Category': ['Books', 'Toys', 'Books', 'Toys'],
    'Revenue': [200, 150, 250, 100]
})

df_pivot = df_sales.pivot(index='Month', columns='Category', values='Revenue')
```

### ✅ Activity 3: Melt and Tidy

```python
df_melted = df_pivot.reset_index().melt(id_vars='Month')
```

### ✅ Activity 4: Group and Aggregate

```python
df_sales.groupby('Category')['Revenue'].sum()
```

---

## ✅ Summary of Learning Outcomes

| Task                  | Skill Gained                             |
| --------------------- | ---------------------------------------- |
| `merge()`             | Combine datasets with shared keys        |
| `concat()`            | Stack datasets by rows or columns        |
| `pivot()`             | Transform long data into wide format     |
| `melt()`              | Normalize wide data into tidy format     |
| `groupby()` + `agg()` | Aggregate and summarize data efficiently |

---

## 🚀 Bonus Challenge

Download a dataset from [data.gov](https://catalog.data.gov/) or [Kaggle](https://www.kaggle.com/datasets) and:

1. Merge two related tables (e.g., products + sales)
2. Pivot it to show category-wise totals per month
3. Use `.melt()` to reverse the pivot
4. Aggregate results to find top-selling categories


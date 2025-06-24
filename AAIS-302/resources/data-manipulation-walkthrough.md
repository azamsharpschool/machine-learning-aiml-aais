
# 🏡 Getting Started with Pandas: Data Manipulation Walkthrough – House Prices

[Download the Dataset](house_prices_20k.csv)

Welcome to your **first hands-on walkthrough with Pandas**, one of the most powerful libraries in the Python data science toolkit. In this guided activity, you'll explore the fundamentals of loading, exploring, cleaning, and transforming a dataset—specifically one containing **house price information**.

This exercise is designed to mirror the kinds of tasks you'll encounter in real-world data science roles, such as working for real estate platforms, finance firms, or any domain that uses structured datasets.

---

## 🧩 **What You’ll Learn**

* Loading data into a Pandas DataFrame
* Inspecting and understanding the dataset
* Selecting, filtering, and transforming data
* Dealing with missing or inconsistent data
* Aggregating, sorting, and saving results
* Applying your knowledge to real-world style challenges

---

## ✅ Prerequisites

Make sure you have **Python** and **Pandas** installed. We recommend using [Miniconda](https://docs.anaconda.com/free/miniconda/index.html) or [Jupyter Notebooks](https://jupyter.org/) for an interactive experience.

To install Pandas:

```bash
pip install pandas
```

---

## 📥 Step 1: Import Pandas

Start every data project by importing Pandas:

```python
import pandas as pd
```

It’s convention to import Pandas as `pd`, which makes it easier to type.

---

## 📁 Step 2: Load the Dataset

Let’s use this small dataset of house prices for our initial exploration. You can save the following as a CSV file called `house_prices.csv`.

```csv
Id,Location,Size,Price
1,New York,1000,300000
2,Los Angeles,1500,450000
3,Chicago,800,250000
4,Miami,1200,360000
5,Dallas,1400,420000
```

Now load it into a Pandas DataFrame:

```python
df = pd.read_csv('house_prices.csv')
```

---

## 🔍 Step 3: Explore the Dataset

### ➤ View the first few rows

```python
print(df.head())
```

### ➤ Check the structure and types

```python
print(df.info())
```

This shows column names, data types (int64, object, etc.), and null value counts.

### ➤ View basic statistics

```python
print(df.describe())
```

Includes mean, std dev, min, max, and percentiles for numeric columns.

### ➤ List all column names

```python
print(df.columns.tolist())
```

Useful for quickly checking spelling or naming issues.

---

## 🧠 Step 4: Data Selection & Filtering

### ➤ Select a specific column

```python
prices = df['Price']
print(prices.head())
```

### ➤ Select multiple columns

```python
subset = df[['Location', 'Price']]
print(subset.head())
```

### ➤ Filter rows (e.g., price > \$400,000)

```python
expensive_houses = df[df['Price'] > 400000]
print(expensive_houses)
```

### ➤ Filter by Location

```python
ny_houses = df[df['Location'] == 'New York']
print(ny_houses)
```

This is especially useful when dealing with customer segments or regional data.

---

## 🧮 Step 5: Data Transformation

### ➤ Add a computed column: price per square foot

```python
df['PricePerSqFt'] = df['Price'] / df['Size']
```

View it:

```python
print(df[['Location', 'Size', 'Price', 'PricePerSqFt']])
```

This is a **derived metric**—something often created during feature engineering in ML.

---

### ➤ Group by location to find average price

```python
avg_price = df.groupby('Location')['Price'].mean()
print(avg_price)
```

You can reset the index for a cleaner DataFrame:

```python
print(avg_price.reset_index())
```

---

## ⚠️ Step 6: Handle Missing Data

Let’s simulate missing data:

```python
df.loc[2, 'Size'] = None  # Set Chicago’s size to NaN
```

### ➤ Check for missing values

```python
print(df.isnull().sum())
```

### ➤ Fill missing values with the column mean

```python
df['Size'] = df['Size'].fillna(df['Size'].mean())
```

### ➤ Drop rows with any missing values

```python
df.dropna(inplace=True)
```

Use this cautiously—you may lose valuable data!

---

## 🧮 Step 7: Sort and Aggregate

### ➤ Sort by price (descending)

```python
sorted_df = df.sort_values(by='Price', ascending=False)
print(sorted_df)
```

### ➤ Sum total house prices by location

```python
total_price = df.groupby('Location')['Price'].sum()
print(total_price)
```

---

## 💾 Step 8: Save the Modified Dataset

Always save your clean or enriched data for future use:

```python
df.to_csv('house_prices_modified.csv', index=False)
```

---

## 💪 Challenge Exercises

Test your skills with these challenges:

1. **Create a "PriceCategory" column**:

   * Label homes as `"Affordable"` if under \$350,000, else `"Expensive"`.

2. **Find the average size for each PriceCategory**.

3. **Identify the most expensive home** in the dataset and display all its details.

---

## ✅ Solutions

```python
# 1. Price Category
df['PriceCategory'] = df['Price'].apply(lambda x: 'Affordable' if x < 350000 else 'Expensive')

# 2. Average Size by Category
avg_size = df.groupby('PriceCategory')['Size'].mean()
print(avg_size)

# 3. Most Expensive House
most_expensive = df.loc[df['Price'].idxmax()]
print("Most Expensive House:")
print(most_expensive)
```

Example Output:

```text
Most Expensive House:
Id                         2
Location         Los Angeles
Size                    1500
Price                 450000
PricePerSqFt           300.0
PriceCategory     Expensive
```

---

## 🧠 Bonus Exploration Ideas

* Add a column for "Estimated Property Tax" assuming 1.2% of price.
* Visualize price distribution using `matplotlib` or `pandas.plot`.
* Create a bar chart of average house size by location.
* Save filtered data (e.g., only Expensive homes) into a separate CSV.

---

## 🎓 What You’ve Learned

By completing this walkthrough, you now understand how to:

* Load, explore, and clean tabular data
* Filter and derive insights
* Perform basic aggregation and transformation
* Create and save new features

These are **foundational data science skills** that you’ll use across nearly every project, whether you're working on housing prices, customer data, or medical records.


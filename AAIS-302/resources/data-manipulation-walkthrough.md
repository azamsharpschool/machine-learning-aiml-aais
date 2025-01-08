### Getting Started with Pandas: Data Manipulation Walkthrough - House Prices

Welcome to the Pandas Data Manipulation walkthrough! In this exercise, you’ll learn the basics of using Pandas for data manipulation with a focus on **House Prices**. You'll learn how to load data, explore it, and perform key operations such as selecting, transforming, and aggregating data. Let’s get started!

---

### Step 1: Importing Pandas
First, make sure you have Pandas installed. Open your Python environment and run:

```bash
pip install pandas
```

Then, import Pandas in your script:

```python
import pandas as pd
```

---

### Step 2: Loading Data
Download a sample dataset (e.g., house prices data) or use one provided below. Save the following CSV as `house_prices.csv`:

```csv
Id,Location,Size,Price
1,New York,1000,300000
2,Los Angeles,1500,450000
3,Chicago,800,250000
4,Miami,1200,360000
5,Dallas,1400,420000
```

Load it into a DataFrame:

```python
df = pd.read_csv('house_prices.csv')
```

---

### Step 3: Exploring the Data
Inspect the dataset to understand its structure and content.

**Display the first few rows:**

```python
print(df.head())
```

**Get a summary of the dataset:**

```python
print(df.info())
```

**View basic statistics for numeric columns:**

```python
print(df.describe())
```

---

### Step 4: Data Selection and Filtering
Learn how to select specific rows and columns.

**Select a single column (e.g., Price):**

```python
prices = df['Price']
print(prices.head())
```

**Filter rows where the house price is greater than 400,000:**

```python
high_price_houses = df[df['Price'] > 400000]
print(high_price_houses.head())
```

**Filter houses located in 'New York':**

```python
new_york_houses = df[df['Location'] == 'New York']
print(new_york_houses.head())
```

---

### Step 5: Data Transformation
Modify or add new columns.

**Create a new column "PricePerSqFt" to calculate price per square foot:**

```python
df['PricePerSqFt'] = df['Price'] / df['Size']
print(df[['Location', 'Size', 'Price', 'PricePerSqFt']].head())
```

**Calculate the average house price for each location:**

```python
avg_price_by_location = df.groupby('Location')['Price'].mean()
print(avg_price_by_location)
```

---

### Step 6: Handling Missing Data
Learn how to deal with missing values.

**Check for missing values:**

```python
print(df.isnull().sum())
```

**Fill missing values in the "Size" column with the mean size:**

```python
df['Size'] = df['Size'].fillna(df['Size'].mean())
```

---

### Step 7: Sorting and Aggregating Data
Sort and summarize your data.

**Sort houses by price:**

```python
sorted_df = df.sort_values('Price', ascending=False)
print(sorted_df.head())
```

**Find the total price of houses by location:**

```python
total_price_by_location = df.groupby('Location')['Price'].sum()
print(total_price_by_location)
```

---

### Step 8: Saving the Modified Data
Save your manipulated dataset to a new CSV file:

```python
df.to_csv('house_prices_modified.csv', index=False)
```

---

### Challenge Exercises
Here are some exercises to deepen your understanding:

1. **Add a new column called "PriceCategory"** to categorize houses as "Affordable" (below $350,000) or "Expensive" (above $350,000).
2. **Find the average house size for each price category** ("Affordable" vs. "Expensive").
3. **Identify the most expensive house** in the dataset.

---

### Solution

Here are the solutions for the challenge exercises:

1. **Add a new column called "PriceCategory"** to categorize houses as "Affordable" or "Expensive":

```python
df['PriceCategory'] = df['Price'].apply(lambda x: 'Affordable' if x < 350000 else 'Expensive')
print(df[['Location', 'Price', 'PriceCategory']].head())
```

2. **Find the average house size for each price category**:

```python
avg_size_by_price_category = df.groupby('PriceCategory')['Size'].mean()
print(avg_size_by_price_category)
```

3. **Identify the most expensive house**:

```python
most_expensive_house = df.loc[df['Price'].idxmax()]
print("Most Expensive House:")
print(most_expensive_house)
```

**Output example:**

```python
Most Expensive House:
Id                          2
Location               Los Angeles
Size                     1500
Price                   450000
PricePerSqFt           300
PriceCategory     Expensive
Name: 1, dtype: object
```

---

### Conclusion:
By following this walkthrough, you have learned how to manipulate house price data using Pandas. You can now load datasets, explore and analyze them, apply transformations, handle missing data, and save your results. Feel free to experiment with additional exercises to deepen your understanding and apply these techniques to your datasets!
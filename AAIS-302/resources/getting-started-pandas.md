### **Getting Started Walkthrough: Pandas Basics**

This walkthrough introduces you to **Pandas**, a powerful library for data manipulation and analysis in Python. Follow the steps to get hands-on experience with its core functionalities.

---

#### **1. Installation**

If you haven't installed Pandas, use the following command:

```bash
pip install pandas
```

---

#### **2. Importing Pandas**

Open your Python environment (e.g., Jupyter Notebook, VS Code, or terminal), and start by importing the library:

```python
import pandas as pd
```

---

#### **3. Creating a DataFrame**

A **DataFrame** is a two-dimensional, tabular data structure similar to an Excel spreadsheet or SQL table.

```python
# Create a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
```

---

#### **4. Reading Data from a File**

Download a sample CSV file or use the provided link.

```python
# Reading a CSV file into a DataFrame
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
csv_df = pd.read_csv(url)

# Display the first few rows
print(csv_df.head())
```

---

#### **5. Basic Data Exploration**

Explore the structure and summary of the dataset:

```python
# Display the first 5 rows
print(csv_df.head())

# Show basic statistics for numerical columns
print(csv_df.describe())

# Display the column names
print(csv_df.columns)

# Check the shape (rows, columns)
print(csv_df.shape)

# Check for missing values
print(csv_df.isnull().sum())
```

---

#### **6. Filtering and Selecting Data**

Learn how to access rows and columns.

```python
# Selecting a single column
ages = df["Age"]
print(ages)

# Selecting multiple columns
subset = df[["Name", "City"]]
print(subset)

# Filtering rows based on a condition
filtered_df = df[df["Age"] > 30]
print(filtered_df)
```

---

#### **7. Adding and Removing Columns**

Modify your DataFrame by adding or removing columns.

```python
# Adding a new column
df["Salary"] = [70000, 80000, 90000]
print(df)

# Removing a column
df = df.drop("Salary", axis=1)
print(df)
```

---

#### **8. Sorting and Grouping Data**

Sort and group your data for better insights.

```python
# Sorting by Age
sorted_df = df.sort_values(by="Age", ascending=False)
print(sorted_df)

# Grouping by City and finding the mean Age
grouped = df.groupby("City")["Age"].mean()
print(grouped)
```

---

#### **9. Exporting Data**

Save your modified DataFrame to a file.

```python
# Exporting to CSV
df.to_csv("output.csv", index=False)

# Exporting to Excel
df.to_excel("output.xlsx", index=False)
```

---

#### **10. Practice Exercise**

Use the following dataset for practice:

```python
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "Price": [1200, 800, 300, 200],
    "Quantity": [5, 10, 15, 20]
}
practice_df = pd.DataFrame(data)
```

**Tasks:**
1. Find the total revenue for each product (Price × Quantity) and add it as a new column.
2. Filter products with a Price greater than $500.
3. Sort the DataFrame by Quantity in descending order.
4. Save the resulting DataFrame to a file called `practice_output.csv`.

---

#### Solution 

### **Solution: Practice Exercise**

Below is the solution to the tasks for the provided dataset:

```python
import pandas as pd

# Provided dataset
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "Price": [1200, 800, 300, 200],
    "Quantity": [5, 10, 15, 20]
}
practice_df = pd.DataFrame(data)

# 1. Find the total revenue for each product (Price × Quantity) and add it as a new column
practice_df["Total Revenue"] = practice_df["Price"] * practice_df["Quantity"]
print("Step 1: Total Revenue added")
print(practice_df)

# 2. Filter products with a Price greater than $500
filtered_df = practice_df[practice_df["Price"] > 500]
print("\nStep 2: Products with Price > $500")
print(filtered_df)

# 3. Sort the DataFrame by Quantity in descending order
sorted_df = practice_df.sort_values(by="Quantity", ascending=False)
print("\nStep 3: Sorted by Quantity in descending order")
print(sorted_df)

# 4. Save the resulting DataFrame to a file called `practice_output.csv`
sorted_df.to_csv("practice_output.csv", index=False)
print("\nStep 4: DataFrame saved to 'practice_output.csv'")
```

### **Output Examples**

#### **Step 1: Total Revenue added**

| Product | Price | Quantity | Total Revenue |
|---------|-------|----------|---------------|
| Laptop  | 1200  | 5        | 6000          |
| Phone   | 800   | 10       | 8000          |
| Tablet  | 300   | 15       | 4500          |
| Monitor | 200   | 20       | 4000          |

---

#### **Step 2: Products with Price > $500**

| Product | Price | Quantity | Total Revenue |
|---------|-------|----------|---------------|
| Laptop  | 1200  | 5        | 6000          |
| Phone   | 800   | 10       | 8000          |

---

#### **Step 3: Sorted by Quantity in descending order**

| Product | Price | Quantity | Total Revenue |
|---------|-------|----------|---------------|
| Monitor | 200   | 20       | 4000          |
| Tablet  | 300   | 15       | 4500          |
| Phone   | 800   | 10       | 8000          |
| Laptop  | 1200  | 5        | 6000          |

---

#### **Step 4: File `practice_output.csv`**
The final sorted DataFrame is saved to a CSV file in your working directory.
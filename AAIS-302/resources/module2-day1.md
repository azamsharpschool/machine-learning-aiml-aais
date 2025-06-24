
# 📅 Day 1: Beginner Walkthrough – **Introduction to Data Cleaning and Loading Data**

---

## 🧠 Why Data Cleaning and Loading Matter

Before we can visualize, analyze, or model data, we need to **load it** and **clean it**. This step is foundational — like sharpening your tools before starting a project.

### 💡 Real-World Analogy:

Imagine a restaurant receiving ingredients. If some vegetables are spoiled or mislabeled, cooking a delicious meal becomes impossible. Similarly, messy data leads to inaccurate insights — also known as **"garbage in, garbage out."**

---

## 🧹 Common Data Quality Issues You’ll Encounter

| 🔧 Problem              | 💥 Example                                       |
| ----------------------- | ------------------------------------------------ |
| Missing Values          | A customer record with no email or age           |
| Duplicates              | A product listed multiple times in a catalog     |
| Wrong Data Types        | A price column stored as text instead of numbers |
| Inconsistent Formatting | "USA" vs "U.S.A." vs "United States"             |
| Outliers or Typos       | Age of 999 or salary of -\$1000                  |

---

## 📦 Step 1: Load Data into Pandas

First, import the **Pandas** library — your go-to tool for working with structured data in Python.

```python
import pandas as pd
```

---

### 📁 1. Loading a CSV File

CSV (Comma Separated Values) is the most common format for tabular data.

```python
# Load CSV data
df = pd.read_csv('employee_data.csv')

# View the first few rows
print(df.head())

# View basic information
print(df.info())
```

👀 `df.head()` gives you a sneak peek.
🧾 `df.info()` shows row count, column types, and null values.

---

### 📊 2. Loading an Excel File

Excel files may contain multiple sheets. You'll need `openpyxl`:

```bash
pip install openpyxl
```

```python
# Load the first sheet
df_excel = pd.read_excel('employee_data.xlsx')
print(df_excel.head())

# Load a specific sheet by name
df_sheet = pd.read_excel('employee_data.xlsx', sheet_name='Sheet2')
```

---

### 🧾 3. Loading a JSON File

Useful for hierarchical or nested data (e.g., API responses):

```python
df_json = pd.read_json('employee_data.json')
print(df_json.head())
print(df_json.info())
```

---

## 🧪 Hands-On Activity – Load and Explore Employee Data

### 📥 Download Sample Data

* CSV: [Employee Heights and Weights](https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv)
* Save as `employee_data.csv`.

---

### 🔍 Step-by-Step: Load and Clean the CSV File

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('employee_data.csv')

# Display first 5 rows
print(df.head())

# Show data types and nulls
print(df.info())

# Check for missing values
print(df.isnull().sum())
```

---

### 📌 Check for Duplicates

Sometimes data is repeated unintentionally. Let’s find out:

```python
duplicate_count = df.duplicated().sum()
print(f"Duplicate Rows: {duplicate_count}")
```

To remove them:

```python
df = df.drop_duplicates()
```

---

## 📂 Optional: Load JSON Data

Create a file named `employee_data.json` and paste:

```json
[
  {"Name": "Alice", "Age": 25, "Department": "HR"},
  {"Name": "Bob", "Age": 30, "Department": "IT"},
  {"Name": "Charlie", "Age": 35, "Department": "Finance"}
]
```

Then load it with Pandas:

```python
df_json = pd.read_json('employee_data.json')
print(df_json.info())
print(df_json.head())
```

---

## 🧩 Pro Tips and Notes

* Always use `df.info()` right after loading any dataset.
* For large datasets, use `nrows=100` to load a sample.
* Clean column names:

```python
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
```

---

## 🧠 Learning Outcomes

By the end of Day 1, you will be able to:
✅ Load datasets from CSV, Excel, and JSON
✅ Inspect data using `.head()`, `.info()`, and `.describe()`
✅ Detect missing values and duplicates
✅ Understand common formatting pitfalls

---

## 🔍 Reflection & Real-World Scenario

> Imagine you’re working for a human resources team analyzing employee salary trends. If ages are recorded as text and departments have inconsistent labels (e.g., “IT” vs “it”), your summaries and dashboards may be completely wrong.

Cleaning ensures you're working with **trustworthy, structured, and consistent data**.

---

## 💪 Challenge Tasks

1. ✅ Download and load a different dataset (e.g., from [Kaggle](https://www.kaggle.com/datasets) or [data.gov](https://catalog.data.gov/))
2. ✅ Use `.isnull().sum()` and `.duplicated().sum()` on the dataset
3. ✅ Clean column names using string functions
4. ✅ Save the cleaned dataset to a new CSV file:

```python
df.to_csv('cleaned_data.csv', index=False)
```


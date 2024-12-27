### Beginner Walkthrough for Day 1: **Introduction to Data Cleaning and Loading Data**

---

#### **Introduction to Data Cleaning**

**Why It Matters**  
- Clean data is crucial for reliable analysis. Without cleaning, you risk the principle of "garbage in, garbage out."  
- Common issues:
  - Missing values
  - Duplicates
  - Incorrect formats (e.g., text instead of numbers)

> **Example**: Think of analyzing sales data where some entries are missing prices or dates. Cleaning ensures your analysis is meaningful.

---

#### **Loading Data into Pandas**

Pandas simplifies loading data from various formats. Let’s start with some basics:

1. **Loading a CSV File**  
   CSV files are widely used for tabular data.  
   **Code Example:**
   ```python
   import pandas as pd
   
   # Load a CSV file
   df = pd.read_csv('employee_data.csv')  # Replace with your actual file path
   
   # Preview the first few rows
   print(df.head())
   ```

---

2. **Loading an Excel File**  
   Excel files can have multiple sheets. Pandas supports reading them with `pd.read_excel()`.  
   **Code Example:**
   ```python
   df_excel = pd.read_excel('employee_data.xlsx')  # Replace with your file path
   print(df_excel.head())
   ```

   > **Note**: You may need the `openpyxl` library to read Excel files:
   ```bash
   pip install openpyxl
   ```

---

3. **Loading a JSON File**  
   JSON is often used for nested data like API responses.  
   **Code Example:**
   ```python
   df_json = pd.read_json('employee_data.json')  # Replace with your file path
   
   # Display structure and preview
   print(df_json.info())
   print(df_json.head())
   ```

---

#### **Hands-On Activity**

Let’s practice with sample data. Use the following steps:

1. **Download the Dataset**  
   Use this [Employee Data CSV](https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv) for this activity. Save it as `employee_data.csv`.  
   (This dataset includes employee heights and weights.)

2. **Load and Explore the CSV File**  
   **Code Example:**
   ```python
   import pandas as pd
   
   # Load the dataset
   df = pd.read_csv('employee_data.csv')
   
   # Display the first 5 rows
   print(df.head())
   
   # Check for missing values
   print(df.isnull().sum())  # Counts missing values in each column
   ```

3. **Check for Duplicates**  
   Identify and count duplicate rows:
   ```python
   print(df.duplicated().sum())  # Returns the number of duplicate rows
   ```

4. **Load a JSON File**  
   Save the following sample JSON data as `employee_data.json`:
   ```json
   [
       {"Name": "Alice", "Age": 25, "Department": "HR"},
       {"Name": "Bob", "Age": 30, "Department": "IT"},
       {"Name": "Charlie", "Age": 35, "Department": "Finance"}
   ]
   ```
   **Code Example:**
   ```python
   # Load JSON data
   df_json = pd.read_json('employee_data.json')
   
   # Display structure and first few rows
   print(df_json.info())
   print(df_json.head())
   ```

---

#### **Learning Outcomes**

By the end of this activity, you will:
1. Understand why data cleaning is crucial.
2. Load datasets from common file types (CSV, Excel, JSON) into Pandas.
3. Identify issues like missing values and duplicates in a dataset.

> **Challenge**: Try downloading another dataset (e.g., public data on housing prices) and practice loading it into Pandas!
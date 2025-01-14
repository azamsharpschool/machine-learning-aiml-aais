### **Scenario: Cleaning a Customer Database for a Marketing Campaign**

[Download the Dataset](realistic_customer_data_with_duplicates.csv) 

**Context**: You are a data analyst at a retail company preparing customer data for a targeted marketing campaign. The dataset contains 20,500 records, including duplicate customer names, inconsistent date formats, and non-standard text or numerical values. Cleaning this data is essential for accurate analysis and campaign targeting.

---

### **Objective**:
- Remove duplicate customer records to avoid redundant communications.
- Standardize data formats (e.g., consistent text casing, correct data types for numerical values, and standardized date formats).

---

### **Steps**:

#### **Step 1: Handling Duplicates**

1.1 **Identifying Duplicate Rows**  
The dataset contains duplicate records where the same customer may appear multiple times due to slight differences in formatting.

Using `.duplicated()`:

```python
# Check for duplicates
print("Number of duplicate rows:", df.duplicated().sum())

# Show duplicate rows
print("Duplicate rows:\n", df[df.duplicated()])
```

**Example Output** (for the new dataset):
```
Number of duplicate rows: 500
Duplicate rows:
              Name     Age    Signup_Date  Purchases
2050     John Doe     30    2023-01-15    five
5040     John Doe     30    2023-01-15    five
15001  Jane Smith     25    March 12, 2023   ten
```

---

1.2 **Removing Duplicates**

```python
# Remove duplicate rows
df = df.drop_duplicates()

# Confirm removal
print("Number of duplicate rows after removal:", df.duplicated().sum())
```

**Output**:
```
Number of duplicate rows after removal: 0
```

---

#### **Step 2: Cleaning and Standardizing Data Formats**

2.1 **Standardizing Text Data**  
Customer names have inconsistencies such as different capitalization, leading/trailing spaces, and variations in formatting.

```python
# Standardize the 'Name' column
df['Name'] = df['Name'].str.strip().str.lower()

# Check cleaned names
print(df[['Name']].head())
```

**Example Cleaned Data**:
```
          Name
0     john doe
1   jane smith
2  emily davis
```

---

2.2 **Converting Data Types**  
Columns such as `Age` and `Purchases` may have non-standard or inconsistent data types (e.g., "Thirty", "ten").

```python
# Convert 'Age' to integers, handling non-numeric values
def clean_age(value):
    try:
        return int(value)
    except ValueError:
        if value.lower() == "thirty":
            return 30
        if value.lower() == "forty":
            return 40
    return None

df['Age'] = df['Age'].apply(clean_age)

# Convert 'Purchases' to integers
def clean_purchases(value):
    if isinstance(value, str):
        if value.lower() == "five":
            return 5
        if value.lower() == "ten":
            return 10
    return int(value)

df['Purchases'] = df['Purchases'].apply(clean_purchases)

# Check data types
print(df.dtypes)
```

**Output**:
```
Name               object
Age                 int64
Signup_Date        object
Purchases           int64
dtype: object
```

---

2.3 **Handling Inconsistent Date Formats**  
Dates are stored in varying formats such as "2023-01-15", "15-01-2023", or "March 12, 2023."

```python
# Standardize 'Signup_Date'
df['Signup_Date'] = pd.to_datetime(df['Signup_Date'], errors='coerce')

# Check cleaned dates
print(df[['Signup_Date']].head())
```

**Cleaned Dates**:
```
  Signup_Date
0  2023-01-15
1  2023-03-12
2  2023-02-22
```

---

### **Step 3: Hands-On Activity**  
**Apply these steps to your dataset**:
1. Identify and remove duplicates using `.duplicated()` and `.drop_duplicates()`.
2. Standardize the `Name` column by removing spaces and normalizing case.
3. Convert `Age` and `Purchases` to integers using custom cleaning functions.
4. Standardize `Signup_Date` using `pd.to_datetime()`.

---

### **Real-World Outcome**:
The cleaned dataset ensures:
- Accurate customer counts and no redundant emails.
- Consistent naming conventions for easier analysis.
- Correct numerical data for accurate purchase trend analysis.
- Standardized date formats for seamless time-series analysis.

By following these steps, you’ve prepared a high-quality dataset ready for effective marketing and customer behavior insights!
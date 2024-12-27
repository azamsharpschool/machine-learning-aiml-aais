# Walkthrough for Day 3: Removing Duplicates and Cleaning Data Formats

This walkthrough will guide you step-by-step through the beginner-friendly activities outlined in the lecture. Follow along with the instructions and code snippets to practice detecting and removing duplicates and cleaning data formats.

---

## **Objective**  
By the end of this session, you’ll be able to:
1. Detect and remove duplicate rows in a dataset.
2. Standardize and clean data formats in preparation for analysis.

---

## **Step 1: Handling Duplicates**

### **1.1 Identifying Duplicate Rows**
Duplicate rows can inflate data and skew analysis. Start by identifying them using the `.duplicated()` method.

#### **Code Example**:
```python
# Check for duplicates
print("Number of duplicate rows:", df.duplicated().sum())

# Show duplicate rows
duplicates = df[df.duplicated()]
print("Duplicate rows:")
print(duplicates)
```

#### **Explanation**:
- `df.duplicated()` returns a boolean series indicating whether each row is a duplicate.
- `df[df.duplicated()]` filters and displays only the duplicate rows.

---

### **1.2 Removing Duplicates**
Once duplicates are identified, remove them using `.drop_duplicates()`.

#### **Code Example**:
```python
# Remove duplicate rows
df = df.drop_duplicates()

# Confirm removal
print("Number of duplicate rows after removal:", df.duplicated().sum())
```

#### **Explanation**:
- `df.drop_duplicates()` removes duplicate rows.
- The updated `df` no longer contains duplicates.

---

## **Step 2: Cleaning and Standardizing Data Formats**

### **2.1 Standardizing Text Data**
Text data often needs cleaning to ensure consistency. Use `.str.lower()` to convert text to lowercase and `.str.strip()` to remove leading and trailing whitespace.

#### **Code Example**:
```python
# Standardize the 'name' column
df['name'] = df['name'].str.strip().str.lower()

# Display the cleaned column
print(df[['name']].head())
```

#### **Explanation**:
- `.str.strip()` removes extra spaces.
- `.str.lower()` ensures all text is lowercase for consistency.

---

### **2.2 Converting Data Types**
Sometimes data is stored in the wrong format (e.g., numbers as strings). Use `.astype()` to convert columns to the appropriate data type.

#### **Code Example**:
```python
# Convert 'age' column to integer
df['age'] = df['age'].astype(int)

# Check the data type
print(df.dtypes)
```

#### **Explanation**:
- `.astype()` changes the data type of a column to the specified type.

---

### **2.3 Handling Inconsistent Date Formats**
Dates may have inconsistent formats. Use `pd.to_datetime()` to standardize them.

#### **Code Example**:
```python
# Standardize the 'date' column
df['date'] = pd.to_datetime(df['date'])

# Display the cleaned column
print(df[['date']].head())
```

#### **Explanation**:
- `pd.to_datetime()` parses various date formats into a consistent datetime format.

---

## **Step 3: Hands-On Activity**

Follow these steps to practice the concepts:

1. **Detect and Remove Duplicates**:
   ```python
   print("Duplicate rows:", df.duplicated().sum())
   df = df.drop_duplicates()
   print("Duplicates removed.")
   ```

2. **Clean Text Data**:
   ```python
   df['name'] = df['name'].str.strip().str.lower()
   print("Standardized text data:\n", df['name'].head())
   ```

3. **Standardize Data Types**:
   ```python
   df['age'] = df['age'].astype(int)
   print("Data types:\n", df.dtypes)
   ```

4. **Handle Dates**:
   ```python
   df['date'] = pd.to_datetime(df['date'])
   print("Standardized dates:\n", df['date'].head())
   ```

---

## **Learning Outcomes**
- **Detect duplicates**: You now know how to identify duplicate rows using `.duplicated()`.
- **Remove duplicates**: You can clean your dataset by removing unnecessary duplicates with `.drop_duplicates()`.
- **Clean text data**: You can standardize text formats for consistency using `.str` methods.
- **Standardize data types**: You can ensure columns have the correct data types with `.astype()`.
- **Handle dates**: You can parse and standardize inconsistent date formats using `pd.to_datetime()`.

---

Feel free to experiment with the dataset and apply these techniques to clean and prepare your data for analysis!
Here’s a walkthrough using the **Home Prices dataset**, which contains common features like square footage, number of bedrooms, and missing values. The dataset will simulate a real-world scenario of handling missing data.

---

## **Day 2: Handling Missing Data**

---

### **Step 1: Setting Up the Environment**

#### Install Required Libraries
```bash
pip install pandas numpy
```

#### Import Libraries and Create a Sample Home Prices Dataset
If you don’t already have a dataset, create one with missing values:

```python
import pandas as pd
import numpy as np

# Create a sample home prices dataset
data = {
    'Price': [300000, 400000, np.nan, 500000, 600000],
    'Square_Feet': [1500, 2000, 2500, np.nan, 3000],
    'Bedrooms': [3, 4, np.nan, 3, 5],
    'Location': ['Suburban', 'Urban', 'Urban', np.nan, 'Rural']
}

df = pd.DataFrame(data)
```

---

### **Step 2: Inspect the Dataset**

#### Display the Dataset
```python
print(df)
```

**Example Output:**
```
      Price  Square_Feet  Bedrooms  Location
0  300000.0       1500.0       3.0  Suburban
1  400000.0       2000.0       4.0     Urban
2       NaN       2500.0       NaN     Urban
3  500000.0          NaN       3.0       NaN
4  600000.0       3000.0       5.0     Rural
```

---

### **Step 3: Identifying Missing Data**

#### 1. Check for Missing Values
```python
print(df.isnull())
```

#### 2. Summarize Missing Data
```python
print("Missing values summary:")
print(df.isnull().sum())
```

**Output:**
```
Price          1
Square_Feet    1
Bedrooms       1
Location       1
dtype: int64
```

---

### **Step 4: Strategies for Handling Missing Data**

#### 1. Drop Rows/Columns with Missing Data
- **Drop Rows:** Remove rows where any value is missing.

```python
df_dropped_rows = df.dropna()
print("Data after dropping rows with missing values:")
print(df_dropped_rows)
```

**Output:**
```
      Price  Square_Feet  Bedrooms  Location
0  300000.0       1500.0       3.0  Suburban
1  400000.0       2000.0       4.0     Urban
4  600000.0       3000.0       5.0     Rural
```

- **Drop Columns:** Remove columns where values are missing.

```python
df_dropped_columns = df.dropna(axis=1)
print("Data after dropping columns with missing values:")
print(df_dropped_columns)
```

---

#### 2. Fill Missing Values
##### Replace Missing Values with the Mean (for Numerical Data)
```python
df['Price'] = df['Price'].fillna(df['Price'].mean())
df['Square_Feet'] = df['Square_Feet'].fillna(df['Square_Feet'].mean())
print("Data after filling missing values with mean:")
print(df)
```

**Updated Output:**
```
      Price  Square_Feet  Bedrooms  Location
0  300000.0       1500.0       3.0  Suburban
1  400000.0       2000.0       4.0     Urban
2  450000.0       2500.0       NaN     Urban
3  500000.0       2250.0       3.0       NaN
4  600000.0       3000.0       5.0     Rural
```

##### Replace Missing Values with the Median
```python
df['Bedrooms'] = df['Bedrooms'].fillna(df['Bedrooms'].median())
print("Data after filling missing Bedrooms with median:")
print(df)
```

**Output:**
```
      Price  Square_Feet  Bedrooms  Location
0  300000.0       1500.0       3.0  Suburban
1  400000.0       2000.0       4.0     Urban
2  450000.0       2500.0       3.0     Urban
3  500000.0       2250.0       3.0       NaN
4  600000.0       3000.0       5.0     Rural
```

##### Replace Missing Values in Categorical Columns
For `Location`, fill missing values with the most frequent value (mode):
```python
df['Location'] = df['Location'].fillna(df['Location'].mode()[0])
print("Data after filling missing Location with mode:")
print(df)
```

---

### **Step 5: Hands-On Activity**

1. **Identify Missing Values:**
   ```python
   print(df.isnull().sum())
   ```

2. **Drop Rows with Missing Values:**
   ```python
   df_cleaned = df.dropna()
   ```

3. **Fill Missing Numerical Data with Mean:**
   ```python
   df['Price'] = df['Price'].fillna(df['Price'].mean())
   ```

4. **Fill Missing Categorical Data with Mode:**
   ```python
   df['Location'] = df['Location'].fillna(df['Location'].mode()[0])
   ```

---

### **Step 6: Wrap-Up**
#### Learning Outcomes:
1. Identified missing data using `.isnull()` and `.isnull().sum()`.
2. Removed rows/columns with `.dropna()`.
3. Applied `.fillna()` to fill missing values with the mean, median, or mode.

---

### **Next Steps:**
- **Experiment Further:** Use different datasets with varying levels of missing data.
- **Advanced Techniques:** Explore machine learning-based imputations using libraries like `sklearn`.
### Getting Started with Pandas: Data Manipulation Walkthrough

Welcome to the Pandas Data Manipulation walkthrough! In this exercise, you'll learn the basics of using Pandas for data manipulation, including loading data, exploring it, and performing key operations. Let's get started!

---

### **Step 1: Importing Pandas**
First, make sure you have Pandas installed. Open your Python environment and run:

```python
pip install pandas
```

Then, import Pandas in your script:

```python
import pandas as pd
```

---

### **Step 2: Loading Data**
Download a sample dataset (e.g., Titanic dataset) or use one provided below. Save the following CSV as `titanic.csv`:

```csv
PassengerId,Survived,Pclass,Name,Sex,Age,Fare
1,0,3,Braund, Mr. Owen Harris,male,22,7.25
2,1,1,Cumings, Mrs. John Bradley,female,38,71.2833
3,1,3,Heikkinen, Miss. Laina,female,26,7.925
4,1,1,Futrelle, Mrs. Jacques Heath,female,35,53.1
5,0,3,Allen, Mr. William Henry,male,35,8.05
```

Load it into a DataFrame:

```python
df = pd.read_csv('titanic.csv')
```

---

### **Step 3: Exploring the Data**
Inspect the dataset to understand its structure and content.

- Display the first few rows:
  ```python
  print(df.head())
  ```

- Get a summary of the dataset:
  ```python
  print(df.info())
  ```

- View basic statistics for numeric columns:
  ```python
  print(df.describe())
  ```

---

### **Step 4: Data Selection and Filtering**
Learn how to select specific rows and columns.

- Select a single column (e.g., `Age`):
  ```python
  ages = df['Age']
  print(ages.head())
  ```

- Filter rows where passengers survived:
  ```python
  survived = df[df['Survived'] == 1]
  print(survived.head())
  ```

- Filter rows where passengers paid a fare greater than 50:
  ```python
  high_fare = df[df['Fare'] > 50]
  print(high_fare.head())
  ```

---

### **Step 5: Data Transformation**
Modify or add new columns.

- Create a new column `AgeCategory` to categorize passengers as `Child` or `Adult`:
  ```python
  df['AgeCategory'] = df['Age'].apply(lambda x: 'Child' if x < 18 else 'Adult')
  print(df[['Name', 'Age', 'AgeCategory']].head())
  ```

- Calculate the mean fare for each passenger class (`Pclass`):
  ```python
  mean_fare = df.groupby('Pclass')['Fare'].mean()
  print(mean_fare)
  ```

---

### **Step 6: Handling Missing Data**
Learn how to deal with missing values.

- Check for missing values:
  ```python
  print(df.isnull().sum())
  ```

- Fill missing ages with the median age:
  ```python
  df['Age'] = df['Age'].fillna(df['Age'].median())
  ```

---

### **Step 7: Sorting and Aggregating Data**
Sort and summarize your data.

- Sort passengers by age:
  ```python
  sorted_df = df.sort_values('Age')
  print(sorted_df.head())
  ```

- Aggregate the data to find the total fare paid by gender:
  ```python
  total_fare_by_gender = df.groupby('Sex')['Fare'].sum()
  print(total_fare_by_gender)
  ```

---

### **Step 8: Saving the Modified Data**
Save your manipulated dataset to a new CSV file:

```python
df.to_csv('titanic_modified.csv', index=False)
```

---

### **Challenge Exercises**
1. Add a new column called `Family` to indicate whether the passenger has a title (`Mr.`, `Mrs.`, etc.) in their name.
2. Find the survival rate for each passenger class (`Pclass`).
3. Identify the youngest and oldest passengers in the dataset.


### Solution 

Here are the solutions for the **Challenge Exercises**:

---

### **1. Add a new column called `Family` to indicate whether the passenger has a title (`Mr.`, `Mrs.`, etc.) in their name.**

We can extract titles from the `Name` column by looking for patterns like `Mr.`, `Mrs.`, etc., and then create a new column.

```python
import re

# Function to check if a title exists in the name
def has_title(name):
    if re.search(r'\b(Mr|Mrs|Miss|Master)\b', name):
        return True
    return False

# Apply the function to create a new 'Family' column
df['Family'] = df['Name'].apply(has_title)
print(df[['Name', 'Family']].head())
```

---

### **2. Find the survival rate for each passenger class (`Pclass`).**

The survival rate is calculated as the ratio of survivors (`Survived == 1`) to the total number of passengers in each class.

```python
# Group by 'Pclass' and calculate survival rate
survival_rate = df.groupby('Pclass')['Survived'].mean()
print(survival_rate)
```

Output example:
```
Pclass
1    0.80
2    0.50
3    0.25
Name: Survived, dtype: float64
```

---

### **3. Identify the youngest and oldest passengers in the dataset.**

To find the youngest and oldest passengers, we can use the `idxmin` and `idxmax` functions on the `Age` column.

```python
# Find the youngest passenger
youngest_passenger = df.loc[df['Age'].idxmin()]
print("Youngest Passenger:")
print(youngest_passenger)

# Find the oldest passenger
oldest_passenger = df.loc[df['Age'].idxmax()]
print("\nOldest Passenger:")
print(oldest_passenger)
```

Output example:
```
Youngest Passenger:
PassengerId                        1
Survived                           0
Pclass                             3
Name         Braund, Mr. Owen Harris
Sex                             male
Age                               22
Fare                            7.25
Family                          True
Name: 0, dtype: object

Oldest Passenger:
PassengerId                        2
Survived                           1
Pclass                             1
Name      Cumings, Mrs. John Bradley
Sex                           female
Age                               38
Fare                        71.2833
Family                          True
Name: 1, dtype: object
```

---

Feel free to adapt the solutions to your specific dataset or add enhancements for deeper analysis!


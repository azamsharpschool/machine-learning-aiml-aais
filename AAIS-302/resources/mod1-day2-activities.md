### Walkthrough for Beginner Activities: Day 2 - Data Manipulation with Pandas

#### **Objective**: Learn how to clean and manipulate data using Pandas.

---

### **1. Handling Missing Data**
#### **Concept**
- Discuss missing data in datasets and its implications.
- Introduce `.dropna()` to remove rows or columns with missing data.
- Introduce `.fillna()` to replace missing values with a default value.

#### **Walkthrough**
1. **Load a Dataset**: Load a dataset with missing values (e.g., a CSV file).
   ```python
   import pandas as pd
   
   # Example dataset
   data = {
       'Name': ['Alice', 'Bob', 'Charlie', 'David'],
       'Age': [25, 30, None, 40],
       'Salary': [50000, None, 60000, 70000]
   }
   df = pd.DataFrame(data)
   print(df)
   ```
2. **Identify Missing Data**:
   ```python
   print(df.isnull())  # Check where values are missing
   print(df.isnull().sum())  # Count missing values per column
   ```

3. **Handle Missing Data**:
   - Replace missing values:
     ```python
     df_filled = df.fillna({'Age': 0, 'Salary': 0})
     print(df_filled)
     ```
   - Drop rows with missing values:
     ```python
     df_dropped = df.dropna()
     print(df_dropped)
     ```

#### **Activity**:
- Replace missing values in the dataset with default values.
- Drop rows with missing data and observe the differences.

---

### **2. Filtering and Selecting Data**
#### **Concept**
- Learn how to filter rows based on conditions.
- Understand selecting specific columns using column names.

#### **Walkthrough**
1. **Filter Rows**:
   ```python
   # Example: Filter rows where Salary is greater than 60000
   filtered_df = df[df['Salary'] > 60000]
   print(filtered_df)
   ```

2. **Select Columns**:
   ```python
   # Example: Select only the 'Name' and 'Age' columns
   selected_columns = df[['Name', 'Age']]
   print(selected_columns)
   ```

#### **Activity**:
- Filter the dataset to show rows where `Salary > 60000`.
- Select specific columns (e.g., `Name` and `Salary`).

---

### **3. Sorting and Ranking Data**
#### **Concept**
- Use `.sort_values()` to sort data by specific columns.
- Use `.rank()` to assign rankings to values in a column.

#### **Walkthrough**
1. **Sort Data**:
   ```python
   # Example: Sort by 'Salary' in descending order
   sorted_df = df.sort_values(by='Salary', ascending=False)
   print(sorted_df)
   ```

2. **Rank Data**:
   ```python
   # Example: Rank employees by 'Age'
   df['Age_Rank'] = df['Age'].rank()
   print(df)
   ```

#### **Activity**:
- Sort the dataset by `Salary` in ascending and descending order.
- Rank the dataset by `Age`.

---

### **4. Creating New Columns**
#### **Concept**
- Add calculated or derived columns to enhance analysis.

#### **Walkthrough**
1. **Add a Calculated Column**:
   ```python
   # Example: Add a column that calculates double the salary
   df['Double_Salary'] = df['Salary'] * 2
   print(df)
   ```

2. **Add a Derived Column**:
   ```python
   # Example: Add a column that shows if Age is above 30
   df['Is_Age_Above_30'] = df['Age'] > 30
   print(df)
   ```

#### **Activity**:
- Add a column that calculates the square of the `Age` column.
- Add a column indicating whether `Salary` is above 50,000.

---

### **5. Group and Aggregate Data**
#### **Concept**
- Use `.groupby()` to group data by a categorical column.
- Use aggregation functions (e.g., `.mean()`, `.sum()`, `.count()`).

#### **Walkthrough**
1. **Group Data**:
   ```python
   # Example: Group by 'Age' and calculate the mean 'Salary'
   grouped_df = df.groupby('Age')['Salary'].mean()
   print(grouped_df)
   ```

2. **Aggregate Data**:
   ```python
   # Example: Group by 'Name' and calculate the sum of 'Salary'
   aggregated_df = df.groupby('Name').agg({'Salary': 'sum'})
   print(aggregated_df)
   ```

#### **Activity**:
- Group the dataset by a categorical column (e.g., `Name`).
- Calculate the average `Salary` for each group.

---

### Tips for Beginners:
- **Check Results**: After every step, print the DataFrame to understand the changes.
- **Experiment**: Modify the conditions or column names to see how the output changes.
- **Documentation**: Refer to [Pandas documentation](https://pandas.pydata.org/docs/) for detailed explanations and examples.

By completing these activities, learners will gain hands-on experience with essential data manipulation techniques in Pandas.
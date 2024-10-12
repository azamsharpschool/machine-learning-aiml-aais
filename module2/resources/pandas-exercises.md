# Pandas Exercises

### Exercise 1: 
Create a Series named fruits containing the following fruits: apple, banana, orange, mango.

Assign the number of calories for each fruit: apple (95), banana (105), orange (62), mango (100).

Print the Series and display the calorie count for oranges.

### Exercise 2: 
Create a DataFrame named customer_data with the following columns:

    - Name (list: Alice, Bob, Charlie)
    - Age (list: 25, 30, 28)
    - City (list: New York, Los Angeles, Chicago)

Print the DataFrame and display the age of Bob.
Add a new column named State with values (NY, CA, IL) corresponding to each city.

### Exercise 3: 

Load the tips dataset in Pandas and assign it to a DataFrame named tips_data.

Print the first 5 rows of the DataFrame.

Calculate the average tip amount and display it.

Filter the DataFrame to show only records where the total bill amount is greater than $50.

[Tips DataSet](tips.csv)

### Exercise 4: 

Create a Series named temperatures containing temperature values in Celsius: [25, 18, None, 32, 20].

Print the Series and check for missing values (represented by None).

Replace the missing value with the average temperature of the other values (excluding None).

Print the Series again to confirm the missing value is replaced.

### Exercise 5: Data Selection and Filtering

Task:

```
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
```

```
Select the 'Name' column.
Select rows where the 'Age' is greater than 25.
Select rows where 'City' is 'Chicago' or 'Phoenix'.
```

### Exercise 6: DataFrame Modification

Task:

Add a new column 'Salary' with arbitrary values.

Modify the 'Age' column by adding 2 to each value.

Drop the 'City' column.

### Exercise 7: Grouping and Aggregation
Task:

Group the DataFrame by 'City' and calculate the mean 'Age' for each group.

Group by 'City' and calculate the sum of 'Salary' for each group.

### Exercise 8: Handling Missing Data

Task:

Introduce some missing values into the DataFrame.

Fill the missing values with a default value.

Drop rows with any missing values.


### Exercise 9: Merging and Joining DataFrames

Task:

Create another DataFrame with 'Name' and 'Department' columns.

Merge the two DataFrames on the 'Name' column.

Perform a left join on the two DataFrames.

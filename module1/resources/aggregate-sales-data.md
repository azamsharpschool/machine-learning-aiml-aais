Question:
Create a Python program that aggregates sales data from multiple JSON files, each containing sales data for different regions. Each JSON file follows the structure:

```json
{
  "region": "Region_Name",
  "sales": [
    {"date": "YYYY-MM-DD", "revenue": revenue_value},
    {"date": "YYYY-MM-DD", "revenue": revenue_value},
    ...
  ]
}
```

The program should read these JSON files and combine the sales data into a single JSON file named `aggregated_sales.json`. The aggregated data should include the total revenue across all regions, the average sales per day, and sales data for each region, including the total revenue for each region and sales data for each day.

Write a Python function `aggregate_sales(json_files)` that takes a list of JSON file names as input and returns a dictionary representing the aggregated sales data. The function should calculate the total revenue across all regions, the average sales per day, and compile sales data for each region.

Ensure that your program provides error handling for file reading operations and follows best practices for file handling and data manipulation in Python.

Provide the complete Python program along with necessary instructions or explanations to execute the program successfully.
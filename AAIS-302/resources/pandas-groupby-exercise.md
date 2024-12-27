Here's a beginner exercise to help you practice using the `groupby` function in pandas. This exercise will involve basic grouping and aggregation operations.

### Exercise: Analyzing Sales Data

#### Dataset Description:
You have a dataset of sales records for an online store. The dataset contains the following columns:
- `OrderID`: Unique identifier for each order.
- `CustomerID`: Unique identifier for each customer.
- `Product`: Name of the product.
- `Category`: Category of the product.
- `Quantity`: Quantity of the product ordered.
- `Price`: Price of a single unit of the product.
- `OrderDate`: Date when the order was placed.

Here is a sample dataset:

| OrderID | CustomerID | Product     | Category    | Quantity | Price | OrderDate  |
|---------|------------|-------------|-------------|----------|-------|------------|
| 1       | 101        | Laptop      | Electronics | 1        | 1200  | 2023-01-15 |
| 2       | 102        | Smartphone  | Electronics | 2        | 800   | 2023-02-18 |
| 3       | 103        | Chair       | Furniture   | 4        | 150   | 2023-01-21 |
| 4       | 101        | Desk        | Furniture   | 1        | 300   | 2023-03-05 |
| 5       | 102        | Headphones  | Electronics | 3        | 200   | 2023-04-10 |
| 6       | 104        | Coffee Table| Furniture   | 1        | 250   | 2023-05-12 |

#### Tasks:

1. **Load the dataset:**
   Load the data into a pandas DataFrame. You can create a dictionary and then convert it to a DataFrame for this exercise.

2. **Total Sales by Category:**
   Calculate the total sales (Quantity * Price) for each product category.

3. **Average Price by Product:**
   Calculate the average price for each product.

4. **Total Quantity Sold by Month:**
   Calculate the total quantity of products sold each month.

5. **Top Customer:**
   Identify the customer who spent the most money in total.

#### Steps:

1. **Load the dataset:**

   ```python
   import pandas as pd

   data = {
       'OrderID': [1, 2, 3, 4, 5, 6],
       'CustomerID': [101, 102, 103, 101, 102, 104],
       'Product': ['Laptop', 'Smartphone', 'Chair', 'Desk', 'Headphones', 'Coffee Table'],
       'Category': ['Electronics', 'Electronics', 'Furniture', 'Furniture', 'Electronics', 'Furniture'],
       'Quantity': [1, 2, 4, 1, 3, 1],
       'Price': [1200, 800, 150, 300, 200, 250],
       'OrderDate': pd.to_datetime(['2023-01-15', '2023-02-18', '2023-01-21', '2023-03-05', '2023-04-10', '2023-05-12'])
   }

   df = pd.DataFrame(data)
   ```

2. **Total Sales by Category:**

   ```python
   df['TotalSales'] = df['Quantity'] * df['Price']
   total_sales_by_category = df.groupby('Category')['TotalSales'].sum()
   print(total_sales_by_category)
   ```

3. **Average Price by Product:**

   ```python
   avg_price_by_product = df.groupby('Product')['Price'].mean()
   print(avg_price_by_product)
   ```

4. **Total Quantity Sold by Month:**

   ```python
   df['Month'] = df['OrderDate'].dt.to_period('M')
   total_quantity_by_month = df.groupby('Month')['Quantity'].sum()
   print(total_quantity_by_month)
   ```

5. **Top Customer:**

   ```python
   total_sales_by_customer = df.groupby('CustomerID')['TotalSales'].sum()
   top_customer = total_sales_by_customer.idxmax()
   print(f'Top Customer ID: {top_customer} with Total Sales: {total_sales_by_customer[top_customer]}')
   ```

### Expected Output:

1. **Total Sales by Category:**

   ```
   Category
   Electronics    5200
   Furniture       850
   Name: TotalSales, dtype: int64
   ```

2. **Average Price by Product:**

   ```
   Product
   Chair          150.0
   Coffee Table   250.0
   Desk           300.0
   Headphones     200.0
   Laptop        1200.0
   Smartphone     800.0
   Name: Price, dtype: float64
   ```

3. **Total Quantity Sold by Month:**

   ```
   Month
   2023-01    5
   2023-02    2
   2023-03    1
   2023-04    3
   2023-05    1
   Freq: M, Name: Quantity, dtype: int64
   ```

4. **Top Customer:**

   ```
   Top Customer ID: 102 with Total Sales: 2800
   ```

This exercise should give you a solid foundation in using the `groupby` function in pandas to perform various aggregation operations.
### Day 4: Advanced Manipulation and Real-World Applications Walkthrough

## Datasets 
- [Sales Data](sales.csv)
- [Customers Data](customers.csv)
- [Sales Data](sales_data.csv)
- [Time Series Data](time_series_data.csv)
- [Covid Data](covid_data.csv)

---

#### **Objective**
Introduce students to advanced Pandas techniques, combining multiple DataFrames, reshaping data, and performing time series analysis. Conclude the session with a real-world case study and a final project to consolidate their knowledge.

---

### **1. Merging and Joining DataFrames**
**Goal:** Learn how to combine datasets effectively.

- **Teaching Points:**
  - Use `.merge()` for combining DataFrames on a specific column.
  - Use `.concat()` for stacking DataFrames vertically or horizontally.

- **Activity: Merging Sales and Customer Data**
  1. **Step 1:** Load the sales and customer datasets into separate DataFrames.
     ```python
     import pandas as pd
     sales = pd.read_csv('sales.csv')
     customers = pd.read_csv('customers.csv')
     ```
  2. **Step 2:** Merge the datasets on a common column (e.g., `customer_id`).
     ```python
     merged_data = pd.merge(sales, customers, on='customer_id', how='inner')
     ```
  3. **Step 3:** Analyze the combined data.
     - Calculate total sales by customer.
     ```python
     total_sales = merged_data.groupby('customer_name')['sales_amount'].sum()
     print(total_sales)
     ```

---

### **2. Reshaping DataFrames**
**Goal:** Learn to transform data for better analysis.

- **Teaching Points:**
  - Use `.pivot()` to reshape data into a pivot table.
  - Use `.melt()` to unpivot data for analysis.

- **Activity: Reshaping Sales Data**
  1. **Step 1:** Load sales data.
     ```python
     data = pd.read_csv('sales_data.csv')
     ```
  2. **Step 2:** Use `.pivot()` to show sales by region and product category.
     ```python
     pivot_data = data.pivot(index='region', columns='product_category', values='sales_amount')
     print(pivot_data)
     ```
  3. **Step 3:** Use `.melt()` to revert the pivoted data.
     ```python
     melted_data = pivot_data.reset_index().melt(id_vars=['region'], var_name='product_category', value_name='sales_amount')
     print(melted_data)
     ```

---

### **3. Time Series Analysis**
**Goal:** Handle and analyze datetime data.

- **Teaching Points:**
  - Convert columns to datetime using `pd.to_datetime()`.
  - Resample data to calculate monthly/weekly aggregates.

- **Activity: Monthly Averages for Sales Data**
  1. **Step 1:** Load and convert the date column.
     ```python
     data = pd.read_csv('time_series_data.csv')
     data['date'] = pd.to_datetime(data['date'])
     ```
  2. **Step 2:** Set the date as the index and calculate monthly averages.
     ```python
     data.set_index('date', inplace=True)
     monthly_avg = data['sales_amount'].resample('M').mean()
     print(monthly_avg)
     ```

---

### **4. Real-World Case Study**
**Goal:** Apply Pandas techniques to clean, manipulate, and visualize real-world data.

- **Dataset:** Provide a dataset such as COVID-19 statistics or e-commerce transactions.

- **Activity: Analyze Real-World Dataset**
  1. **Step 1:** Load and clean the dataset.
     ```python
     data = pd.read_csv('covid_data.csv')
     data.dropna(subset=['cases', 'deaths'], inplace=True)
     ```
  2. **Step 2:** Perform analysis (e.g., calculate daily case growth).
     ```python
     data['daily_growth'] = data['cases'].diff()
     print(data.head())
     ```
  3. **Step 3:** Visualize trends (e.g., cases over time).
     ```python
     import matplotlib.pyplot as plt
     data['cases'].plot()
     plt.title('Cases Over Time')
     plt.show()
     ```

---

### **5. Final Project: Data Analysis Report**
**Goal:** Encourage students to independently apply their skills.

- **Instructions:**
  1. Choose a dataset from Kaggle or a provided list.
  2. Perform the following steps:
     - Clean and preprocess the data.
     - Merge and reshape as needed.
     - Perform time series analysis if applicable.
     - Create meaningful visualizations.
  3. Present findings in a Jupyter Notebook.

- **Example Workflow:**
  1. Load and inspect the dataset:
     ```python
     data = pd.read_csv('dataset.csv')
     print(data.info())
     ```
  2. Perform analysis:
     ```python
     summary = data.groupby('category')['value'].mean()
     print(summary)
     ```
  3. Visualize insights:
     ```python
     summary.plot(kind='bar')
     plt.title('Average Value by Category')
     plt.show()
     ```

---

### **Expected Outcomes**
1. Students will master advanced Pandas techniques.
2. They will confidently tackle real-world data manipulation tasks.
3. The final project will demonstrate their ability to analyze and present data professionally.

**Note:** Provide feedback and suggestions for improvement during project presentations.
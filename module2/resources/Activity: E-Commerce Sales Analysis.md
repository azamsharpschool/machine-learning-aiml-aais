### **Activity: E-Commerce Sales Analysis**

#### **Objectives:**
- Analyze sales trends over a period of time.
- Identify the top-selling products.
- Provide actionable insights based on the analysis.

---

### **Activity Setup:**
You are provided with a dataset containing the following columns:
- `OrderID`: Unique identifier for each order.
- `Date`: Date of the transaction.
- `Product`: Name of the product sold.
- `Quantity`: Number of units sold.
- `Price`: Price per unit.
- `TotalSales`: Total revenue from the transaction (`Quantity * Price`).

Your task is to:
1. Analyze sales trends (e.g., monthly sales).
2. Identify the top 3 best-selling products based on total sales.
3. Provide actionable insights based on your findings.

---

### **Dataset Example (CSV):**
```csv
OrderID,Date,Product,Quantity,Price,TotalSales
1,2024-01-01,Widget A,10,25,250
2,2024-01-02,Widget B,5,50,250
3,2024-01-03,Widget A,8,25,200
4,2024-01-05,Widget C,15,10,150
5,2024-02-01,Widget B,7,50,350
6,2024-02-10,Widget A,12,25,300
7,2024-03-01,Widget C,20,10,200
8,2024-03-15,Widget B,10,50,500
```

---

### **Solution Code:**

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.DataFrame({
    "OrderID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Date": pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-05", 
                            "2024-02-01", "2024-02-10", "2024-03-01", "2024-03-15"]),
    "Product": ["Widget A", "Widget B", "Widget A", "Widget C", 
                "Widget B", "Widget A", "Widget C", "Widget B"],
    "Quantity": [10, 5, 8, 15, 7, 12, 20, 10],
    "Price": [25, 50, 25, 10, 50, 25, 10, 50],
    "TotalSales": [250, 250, 200, 150, 350, 300, 200, 500]
})

# Analyze monthly sales trends
data['Month'] = data['Date'].dt.to_period('M')
monthly_sales = data.groupby('Month')['TotalSales'].sum()

# Identify top-selling products
product_sales = data.groupby('Product')['TotalSales'].sum()
top_products = product_sales.sort_values(ascending=False).head(3)

# Plot sales trends
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o', label="Total Sales")
plt.title("Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid()
plt.legend()
plt.show()

# Print results
print("Monthly Sales Trends:")
print(monthly_sales)
print("\nTop 3 Best-Selling Products:")
print(top_products)
```

---

### **Expected Output:**

#### **Monthly Sales Trends Table:**
```
Month
2024-01    850
2024-02    650
2024-03    700
Name: TotalSales, dtype: int64
```

#### **Top 3 Best-Selling Products:**
```
Product
Widget B    1350
Widget A     750
Widget C     350
Name: TotalSales, dtype: int64
```

#### **Visualization:**
A line plot showing the monthly sales trend, highlighting sales peaks and dips.

---

### **Actionable Insights:**
1. **Sales Trends:**
   - Sales peaked in January 2024, suggesting high demand at the start of the year.
   - February saw a decline, possibly indicating seasonality or a lack of promotions.
   - March sales picked up slightly, signaling potential market recovery or new product demand.

2. **Top Products:**
   - Widget B is the best-selling product, accounting for the highest revenue. Focus on maintaining its inventory and promoting it further.
   - Widget A is the second-best-selling product. Bundle it with Widget B to increase sales.
   - Widget C contributes the least. Consider promotions or discontinuation based on profit margins.

3. **Recommendations:**
   - Plan promotions for February to boost sales during the dip.
   - Analyze customer feedback for Widget C to identify areas of improvement or marketing opportunities.
   - Increase production or inventory for Widget B during peak months to avoid stockouts.

---

### **Speaker Script for Group Discussion:**
1. **Introduction:**  
   "For this activity, we’ve analyzed e-commerce sales data to identify trends, best-selling products, and actionable insights."

2. **Questions for Group:**
   - "What factors could explain the sales dip in February?"
   - "How would you market Widget B to maintain its top-selling status?"
   - "Should Widget C be discontinued or rebranded? Why?"

3. **Application in Real World:**  
   - **Retail:** "Sales trend analysis helps retailers plan inventory and promotions effectively."
   - **Marketing:** "Identifying top products allows businesses to create targeted campaigns to boost sales."

4. **Wrap-Up:**  
   "Data-driven decisions, like the ones we discussed, are vital for optimizing business performance and staying competitive in the e-commerce industry." 

This activity allows participants to practice data analysis while exploring real-world applications of insights.
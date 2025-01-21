### Real-Life Walkthrough: Day 4 - Bringing It All Together  
**Objective:** Combine previous concepts to create meaningful visualizations and add interactivity for real-world use cases. Imagine you're a data analyst preparing a report on customer sales trends and marketing performance for a meeting.

---

### **Activity 1: Data Cleaning and Preparation**  
**Scenario:** You receive a sales dataset from the marketing team and need to clean and prepare it for analysis.

#### **Steps**:
1. **Load the Dataset**:
   ```python
   import pandas as pd
   
   # Load sales data
   sales_data = pd.read_csv('sales_data.csv')
   
   # Preview the first few rows
   print(sales_data.head())
   ```

2. **Clean the Data**:
   - Remove rows with missing values:
     ```python
     sales_data = sales_data.dropna()
     ```
   - Filter to only include sales above $1000:
     ```python
     sales_data = sales_data[sales_data['total_sales'] > 1000]
     ```

3. **Prepare for Visualization**:
   - Add a new column for sales in thousands:
     ```python
     sales_data['sales_in_thousands'] = sales_data['total_sales'] / 1000
     ```
   - Convert `date` column to a proper datetime format:
     ```python
     sales_data['date'] = pd.to_datetime(sales_data['date'])
     ```

---

### **Activity 2: Combining Multiple Plots**  
**Scenario:** You need to create a dashboard showcasing sales trends, customer demographics, and product performance.

#### **Steps**:
1. **Set Up Subplots**:
   ```python
   import matplotlib.pyplot as plt
   
   fig, axs = plt.subplots(1, 3, figsize=(18, 6))  # 1 row, 3 columns
   ```

2. **Add Plots**:
   - **Line Chart**: Visualize monthly sales trends.
     ```python
     monthly_sales = sales_data.groupby(sales_data['date'].dt.to_period('M')).sum()
     axs[0].plot(monthly_sales.index.astype(str), monthly_sales['total_sales'], label='Monthly Sales', color='blue')
     axs[0].set_title('Monthly Sales Trends')
     axs[0].set_xlabel('Month')
     axs[0].set_ylabel('Total Sales ($)')
     axs[0].legend()
     ```

   - **Scatterplot**: Compare age and spending habits.
     ```python
     axs[1].scatter(sales_data['age'], sales_data['total_sales'], color='red', alpha=0.6)
     axs[1].set_title('Age vs Spending')
     axs[1].set_xlabel('Age')
     axs[1].set_ylabel('Total Sales ($)')
     ```

   - **Bar Chart**: Show top-performing product categories.
     ```python
     category_sales = sales_data.groupby('product_category')['total_sales'].sum()
     axs[2].bar(category_sales.index, category_sales.values, color='green')
     axs[2].set_title('Top Product Categories')
     axs[2].set_xlabel('Category')
     axs[2].set_ylabel('Total Sales ($)')
     ```

3. **Adjust Layout and Display**:
   ```python
   plt.tight_layout()
   plt.show()
   ```

---

### **Activity 3: Interactive Legends**  
**Scenario:** Your manager wants the ability to toggle between datasets in the monthly sales chart.

#### **Steps**:
1. **Create the Plot**:
   ```python
   fig, ax = plt.subplots()
   online_sales, = ax.plot(monthly_sales.index.astype(str), monthly_sales['online_sales'], label='Online Sales')
   offline_sales, = ax.plot(monthly_sales.index.astype(str), monthly_sales['offline_sales'], label='Offline Sales')
   ax.set_title('Monthly Sales (Online vs Offline)')
   ax.legend()
   ```

2. **Add Interactivity**:
   ```python
   def toggle_visibility(event):
       online_sales.set_visible(not online_sales.get_visible())
       offline_sales.set_visible(not offline_sales.get_visible())
       fig.canvas.draw()
   
   fig.canvas.mpl_connect('key_press_event', toggle_visibility)
   plt.show()
   ```

   **Tip**: Press any key to toggle visibility.

---

### **Activity 4: Adding Interactivity with Widgets**  
**Scenario:** Enable dynamic exploration of sales trends by adjusting the date range.

#### **Steps**:
1. **Set Up the Plot**:
   ```python
   from matplotlib.widgets import Slider
   
   fig, ax = plt.subplots()
   sales_line, = ax.plot(monthly_sales.index.astype(str), monthly_sales['total_sales'])
   ax.set_title('Sales Trends')
   ax.set_xlabel('Month')
   ax.set_ylabel('Total Sales ($)')
   ```

2. **Add a Slider**:
   ```python
   ax_slider = plt.axes([0.2, 0.01, 0.65, 0.03])  # Slider position
   slider = Slider(ax_slider, 'Months', 1, len(monthly_sales), valinit=len(monthly_sales), valstep=1)

   def update(val):
       limit = int(slider.val)
       sales_line.set_data(monthly_sales.index.astype(str)[:limit], monthly_sales['total_sales'][:limit])
       ax.relim()
       ax.autoscale_view()
       fig.canvas.draw()
   
   slider.on_changed(update)
   plt.show()
   ```

---

### **Activity 5: Final Project**  
**Scenario:** Summarize customer behavior and product sales insights for a presentation.

#### **Steps**:
1. **Choose a Dataset**: Use your cleaned sales dataset.

2. **Create Visualizations**:
   - Combine a line chart for sales trends with a scatterplot for age vs spending.
   - Add annotations for key milestones:
     ```python
     ax.annotate('Sales Spike', xy=('2024-07', 50000), xytext=('2024-05', 60000),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))
     ```

3. **Save the Visualization**:
   ```python
   plt.savefig('sales_insights_report.png', dpi=300)
   ```

4. **Present the Work**:
   - Highlight insights such as the most profitable product categories and customer age groups with the highest spending.

---

### **Key Takeaways**:
- Real-world data often needs cleaning and preparation before visualization.
- Combining multiple plots provides a comprehensive view of data.
- Interactivity enhances the usability of visualizations for exploration.
- Saving visualizations ensures they are ready for presentations and reports.

This approach bridges the gap between theoretical learning and practical applications of data visualization!

### Sales by Product Category

``` py
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
sales_data = pd.read_csv('sales_data.csv')

# Group data by product category and sum the total sales
category_sales = sales_data.groupby("product_category")["total_sales"].sum()

# Plot the sales by product category
plt.figure(figsize=(10, 6))
category_sales.sort_values().plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Total Sales by Product Category", fontsize=16)
plt.xlabel("Product Category", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()
```

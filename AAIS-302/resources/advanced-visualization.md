Here’s a real-world scenario-based walkthrough for your activities using **Matplotlib**, which makes the examples relatable and practical:

---

### **Day 3: Advanced Visualizations with Matplotlib**  
**Scenario:** You are a data analyst at a marketing agency tasked with analyzing client data to present actionable insights. Let's visualize some aspects of the data.

---

### **Activity 1: Scatterplots**  
**Scenario:** You want to analyze the relationship between the age of customers and their monthly spending.

```python
import matplotlib.pyplot as plt

# Customer data
age = [22, 25, 30, 35, 40]
monthly_spending = [2000, 2500, 3000, 3500, 4000]

# Create scatterplot
plt.scatter(age, monthly_spending, color='blue', marker='o')
plt.title('Age vs Monthly Spending')
plt.xlabel('Age (Years)')
plt.ylabel('Monthly Spending ($)')
plt.show()
```

**Experiment:**  
- Use `plt.text()` to label high spenders.
- Change the marker to `'*'` to make points stand out.

---

### **Activity 2: Bar Charts**  
**Scenario:** Visualize product sales across different regions.

#### **Horizontal Bar Chart:**
```python
# Data
regions = ['North', 'South', 'East', 'West']
sales = [500, 700, 800, 600]

# Horizontal bar chart
plt.barh(regions, sales, color='green')
plt.title('Sales by Region')
plt.xlabel('Sales ($)')
plt.ylabel('Region')
plt.show()
```

#### **Stacked Bar Chart:**
You also want to compare online vs offline sales.

```python
import numpy as np

# Data
regions = ['North', 'South', 'East', 'West']
online_sales = [300, 400, 450, 300]
offline_sales = [200, 300, 350, 300]
indices = np.arange(len(regions))

# Stacked bar chart
plt.bar(indices, online_sales, color='blue', label='Online Sales')
plt.bar(indices, offline_sales, bottom=online_sales, color='orange', label='Offline Sales')
plt.xticks(indices, regions)
plt.title('Sales Breakdown by Region')
plt.xlabel('Region')
plt.ylabel('Sales ($)')
plt.legend()
plt.show()
```

---

### **Activity 3: Histograms**  
**Scenario:** Analyze the distribution of daily transactions in a store.

```python
# Data: Number of daily transactions
daily_transactions = [10, 20, 20, 30, 30, 30, 40, 40, 50]

# Create histogram
plt.hist(daily_transactions, bins=5, color='purple', edgecolor='black')
plt.title('Distribution of Daily Transactions')
plt.xlabel('Number of Transactions')
plt.ylabel('Frequency')
plt.show()
```

**Experiment:** Adjust the `bins` to group transactions differently.

---

### **Activity 4: Subplots**  
**Scenario:** Create a comprehensive dashboard showing multiple aspects of your data.

```python
fig, axs = plt.subplots(2, 2)  # 2x2 grid

# Line Graph: Growth over months
months = [1, 2, 3, 4, 5]
revenue = [1000, 1200, 1500, 1800, 2000]
axs[0, 0].plot(months, revenue, marker='o')
axs[0, 0].set_title('Monthly Revenue Growth')

# Bar Chart: Regional Sales
regions = ['North', 'South', 'East', 'West']
sales = [500, 700, 800, 600]
axs[0, 1].bar(regions, sales, color='blue')
axs[0, 1].set_title('Sales by Region')

# Histogram: Daily Transactions
transactions = [10, 20, 20, 30, 30, 30, 40, 40, 50]
axs[1, 0].hist(transactions, bins=5, color='green')
axs[1, 0].set_title('Daily Transactions')

# Empty Placeholder
axs[1, 1].axis('off')

# Adjust layout
plt.tight_layout()
plt.show()
```

---

### **Activity 5: Adding Annotations**  
**Scenario:** Highlight a key milestone in revenue growth.

```python
# Data
months = [1, 2, 3, 4, 5]
revenue = [1000, 1200, 1500, 1800, 2000]

# Plot with annotation
plt.plot(months, revenue, marker='o')
plt.title('Revenue Growth with Milestone')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')

# Annotate the highest point
plt.annotate('Milestone Reached', xy=(5, 2000), xytext=(3.5, 1800),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='red')
plt.show()
```

**Experiment:** Annotate multiple milestones.

---

### **Tips for Real-World Use:**  
1. **Save Visualizations**: Use `plt.savefig('chart.png')` for reports.
2. **Customize Themes**: Explore Matplotlib styles for professional visuals (`plt.style.use('ggplot')`).
3. **Real Data**: Replace sample data with actual CSV/Excel data using `pandas`.

By following these examples, you’ll learn how to apply visualization techniques in practical settings!
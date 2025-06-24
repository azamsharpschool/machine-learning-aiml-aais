
# 🎯 **Day 3 Walkthrough: Advanced Visualizations with Matplotlib**

**Real-World Focus:** Marketing & Sales Analytics

---

## 📌 Learning Objectives

By the end of this session, you'll be able to:

* Use **scatterplots** to analyze relationships
* Create **bar charts** and **stacked bars** for comparative analysis
* Plot **histograms** to reveal distributions
* Organize multiple visualizations using **subplots**
* Add **annotations** for insights storytelling

---

## 🔍 **Activity 1: Scatterplots**

### 📊 Goal:

Visualize how customer age relates to monthly spending.

```python
import matplotlib.pyplot as plt

age = [22, 25, 30, 35, 40]
monthly_spending = [2000, 2500, 3000, 3500, 4000]

plt.scatter(age, monthly_spending, color='blue', marker='o')
plt.title('Age vs Monthly Spending')
plt.xlabel('Age (Years)')
plt.ylabel('Monthly Spending ($)')
plt.grid(True)
plt.show()
```

### 🧠 Real Insight:

Scatterplots help us detect **trends** or **correlations** between two numeric variables.

---

## 📊 **Activity 2: Bar Charts**

### 🎯 Goal:

Compare sales across regions and channels.

#### 📌 Horizontal Bar Chart:

```python
regions = ['North', 'South', 'East', 'West']
sales = [500, 700, 800, 600]

plt.barh(regions, sales, color='green')
plt.title('Sales by Region')
plt.xlabel('Sales ($)')
plt.ylabel('Region')
plt.show()
```

#### 📌 Stacked Bar Chart:

```python
import numpy as np

online_sales = [300, 400, 450, 300]
offline_sales = [200, 300, 350, 300]
x = np.arange(len(regions))

plt.bar(x, online_sales, label='Online Sales', color='blue')
plt.bar(x, offline_sales, bottom=online_sales, label='Offline Sales', color='orange')
plt.xticks(x, regions)
plt.title('Sales Breakdown by Region')
plt.xlabel('Region')
plt.ylabel('Sales ($)')
plt.legend()
plt.show()
```

### 📌 Real Insight:

Stacked bars show **how much each component contributes** to the total per category.

---

## 📊 **Activity 3: Histograms**

### 🎯 Goal:

Understand the **distribution** of daily transaction volume.

```python
transactions = [10, 20, 20, 30, 30, 30, 40, 40, 50]

plt.hist(transactions, bins=5, color='purple', edgecolor='black')
plt.title('Distribution of Daily Transactions')
plt.xlabel('Number of Transactions')
plt.ylabel('Frequency')
plt.show()
```

### 📌 Real Insight:

Histograms help detect **skewness**, **clustering**, or **outliers** in data.

---

## 🧱 **Activity 4: Subplots – Dashboard View**

### 🎯 Goal:

Build a dashboard showing multiple KPIs.

```python
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Line chart
months = [1, 2, 3, 4, 5]
revenue = [1000, 1200, 1500, 1800, 2000]
axs[0, 0].plot(months, revenue, marker='o')
axs[0, 0].set_title('Monthly Revenue Growth')

# Bar chart
axs[0, 1].bar(regions, sales, color='skyblue')
axs[0, 1].set_title('Sales by Region')

# Histogram
axs[1, 0].hist(transactions, bins=5, color='lime')
axs[1, 0].set_title('Daily Transactions')

# Empty cell
axs[1, 1].axis('off')

plt.tight_layout()
plt.show()
```

### 📌 Real Insight:

Subplots allow visual **storytelling** by presenting related metrics together.

---

## 📝 **Activity 5: Adding Annotations**

### 🎯 Goal:

Highlight milestones or anomalies on a chart.

```python
plt.plot(months, revenue, marker='o')
plt.title('Revenue Growth with Milestone')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')

# Highlight a key month
plt.annotate('Milestone Reached', 
             xy=(5, 2000), 
             xytext=(3.5, 1800),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='red')

plt.grid(True)
plt.show()
```

### 📌 Real Insight:

Annotations draw attention to **important points**, great for dashboards and presentations.

---

## 🔁 Bonus Challenges

* Create a **pie chart** showing % of sales by channel.
* Annotate **outliers** on a scatterplot.
* Turn subplots into a **report PDF** using `matplotlib.backends.backend_pdf`.

---

## 📦 Exporting Plots

```python
plt.savefig('sales_summary.png', dpi=300)
```

Use this for:

* Reports
* Dashboards
* Presentations


### Walkthrough for Beginner Activities: Day 3 - Data Visualization and Analysis

#### Objective:
To introduce students to data visualization and exploratory data analysis (EDA), enabling them to extract insights from data.

---

### **1. Introduction to Data Visualization with Matplotlib**

#### **Step-by-Step Guide:**
1. **Install Matplotlib**  
   ```bash
   pip install matplotlib
   ```
2. **Basics of Plotting:**
   - Explain the concept of figure and axes in Matplotlib.
   - Demonstrate how to plot a simple line chart and bar chart.

#### **Activity: Create a Simple Line Chart and Bar Chart**
- **Dataset Example:** Monthly sales data.
   ```python
   import matplotlib.pyplot as plt

   # Example data
   months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
   sales = [200, 300, 400, 500, 600]

   # Line chart
   plt.plot(months, sales, marker='o')
   plt.title('Monthly Sales')
   plt.xlabel('Month')
   plt.ylabel('Sales')
   plt.show()

   # Bar chart
   plt.bar(months, sales, color='skyblue')
   plt.title('Monthly Sales')
   plt.xlabel('Month')
   plt.ylabel('Sales')
   plt.show()
   ```

---

### **2. Visualize Data with Pandas**

#### **Step-by-Step Guide:**
1. **Install Pandas**  
   ```bash
   pip install pandas
   ```
2. **Load a Dataset:**  
   Use a simple dataset, e.g., a CSV file with columns like "Age" and "Income."
3. **Explain Built-In Plotting:**  
   Pandas supports quick visualizations.

#### **Activity: Create a Histogram and Scatter Plot**
- **Histogram:** Visualize the distribution of a numeric column.
- **Scatter Plot:** Show relationships between two numeric columns.

   ```python
   import pandas as pd

   # Sample data
   data = {
       'Age': [25, 30, 35, 40, 45],
       'Income': [3000, 4000, 5000, 6000, 7000]
   }
   df = pd.DataFrame(data)

   # Histogram
   df['Age'].plot(kind='hist', title='Age Distribution', color='orange')
   plt.xlabel('Age')
   plt.show()

   # Scatter plot
   df.plot(kind='scatter', x='Age', y='Income', title='Age vs Income', color='red')
   plt.show()
   ```

---

### **3. Analyzing Correlations**

#### **Step-by-Step Guide:**
1. **Explain Correlation:**  
   Highlight how correlation indicates the relationship between variables.
2. **Use `.corr()` Method:**  
   Calculate correlations between numeric columns in Pandas.

#### **Activity: Calculate and Visualize Correlations with a Heatmap**
- Optional: Install Seaborn for better visualizations.
   ```bash
   pip install seaborn
   ```
   ```python
   import seaborn as sns

   # Calculate correlations
   corr = df.corr()

   # Heatmap visualization
   sns.heatmap(corr, annot=True, cmap='coolwarm')
   plt.title('Correlation Heatmap')
   plt.show()
   ```

---

### **4. EDA with Pandas**

#### **Step-by-Step Guide:**
1. **Summary Statistics:**  
   Use `.describe()` to view trends and identify outliers.
2. **Visualize Patterns:**  
   Create visualizations to support EDA.

#### **Activity: Identify Trends, Outliers, and Patterns**
- Example: Using summary statistics to find outliers.
   ```python
   print(df.describe())  # Provides a summary of numeric columns
   ```

- Visualize:
   ```python
   df.boxplot(column='Income')
   plt.title('Income Distribution')
   plt.show()
   ```

---

### **5. Hands-On Mini Project: Basic EDA**

#### **Scenario:**
Provide a simple dataset (e.g., sales data or movie ratings) and guide students through a structured EDA process.

#### **Activity: Answer Key Questions**
1. **Load the Dataset:**
   ```python
   # Example sales dataset
   data = {
       'Category': ['Electronics', 'Clothing', 'Food', 'Electronics', 'Food'],
       'Sales': [1000, 500, 800, 1200, 700],
       'Year': [2020, 2020, 2021, 2021, 2020]
   }
   df = pd.DataFrame(data)
   ```

2. **Questions to Answer:**
   - Which category has the highest sales?
     ```python
     print(df.groupby('Category')['Sales'].sum().idxmax())
     ```
   - What is the average sales for each year?
     ```python
     print(df.groupby('Year')['Sales'].mean())
     ```

3. **Visualize Insights:**
   ```python
   df.groupby('Category')['Sales'].sum().plot(kind='bar', title='Sales by Category')
   plt.show()
   ```

---

### **Expected Outcome:**
By the end of this session, students will:
- Understand basic plotting with Matplotlib.
- Use Pandas' visualization and EDA techniques effectively.
- Perform correlation analysis.
- Gain hands-on experience analyzing real-world data to extract insights.
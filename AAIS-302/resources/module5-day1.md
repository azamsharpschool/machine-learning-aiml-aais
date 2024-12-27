### Walkthrough: Real-World Scenario for Day 1: Introduction to Unsupervised Learning

---

**Title:** Exploring Unsupervised Learning Through Data Preparation and Visualization  

---

### **Activity Focus:**  
Understand the foundational concepts of unsupervised learning by exploring a dataset, visualizing patterns, and preparing it for clustering.

---

### **Scenario: Retail Customer Behavior Analysis**

**Objective:**  
Help a retail store group customers based on spending habits to optimize marketing strategies. 

**Dataset Description:**  
A dataset containing customer details, such as:  
- Age  
- Annual Income (in thousands)  
- Spending Score (1–100, a metric assigned by the store based on purchasing behavior).  

---

### **Step-by-Step Walkthrough**

---

#### **Step 1: Understand Supervised vs. Unsupervised Learning**

1. **Task:** Compare labeled vs. unlabeled datasets.  
   - **Labeled Data Example:** A dataset where customers are already grouped into categories (e.g., "High Spender," "Moderate Spender," "Low Spender").  
   - **Unlabeled Data Example:** A dataset with raw features like age, income, and spending score, but no predefined labels.  

2. **Discussion:**  
   - Supervised learning uses labeled data to predict outcomes.  
   - Unsupervised learning identifies patterns or groups in unlabeled data.

**Code Example:**  
```python
import pandas as pd

# Sample labeled and unlabeled data
labeled_data = pd.DataFrame({
    'Age': [25, 40, 22],
    'Annual Income': [30, 70, 25],
    'Spending Score': [60, 40, 75],
    'Category': ['Moderate Spender', 'Low Spender', 'High Spender']  # Labels
})

unlabeled_data = labeled_data.drop(columns=['Category'])  # No labels

print("Labeled Data:\n", labeled_data)
print("\nUnlabeled Data:\n", unlabeled_data)
```

---

#### **Step 2: Data Exploration with Visualizations**

1. **Task:** Create visualizations to identify patterns.  
   - Plot a scatter plot of **Annual Income** vs. **Spending Score**.  

2. **Code Example:**
   ```python
   import matplotlib.pyplot as plt
   import seaborn as sns

   # Load retail dataset (or sample data)
   data = pd.DataFrame({
       'Age': [25, 40, 22, 35, 50],
       'Annual Income': [30, 70, 25, 60, 90],
       'Spending Score': [60, 40, 75, 50, 30]
   })

   # Scatter plot
   plt.scatter(data['Annual Income'], data['Spending Score'], c='blue', s=50)
   plt.title('Customer Spending Behavior')
   plt.xlabel('Annual Income (in thousands)')
   plt.ylabel('Spending Score (1-100)')
   plt.show()
   ```

3. **Discussion:**  
   - Ask students to observe if there are natural groupings (e.g., customers with high income but low spending scores).  
   - Highlight how unsupervised learning algorithms like K-Means will group these points.

---

#### **Step 3: Feature Selection**

1. **Task:** Choose features for clustering.  
   - Features to use: **Annual Income** and **Spending Score**.  
   - Exclude unrelated features like **Age** to simplify analysis.  

2. **Discussion:**  
   - Explain the importance of feature selection in clustering.  
   - Unnecessary features can confuse the model or increase computational complexity.

**Code Example:**  
```python
# Selecting relevant features
selected_features = data[['Annual Income', 'Spending Score']]
print("Selected Features:\n", selected_features.head())
```

---

#### **Step 4: Preprocess the Data**

1. **Task:** Normalize or scale the data to ensure all features are on a similar scale.  
   - **Why?** Clustering algorithms like K-Means are sensitive to scale, as they rely on distance calculations.  

2. **Code Example:**
   ```python
   from sklearn.preprocessing import StandardScaler

   # Scale the features
   scaler = StandardScaler()
   scaled_data = scaler.fit_transform(selected_features)

   print("Scaled Data:\n", scaled_data[:5])
   ```

3. **Discussion:**  
   - Show how preprocessing ensures features like **Annual Income** (thousands) don’t dominate **Spending Score** (1–100).  

---

### **Summary Discussion**

- **Reflection Questions:**  
   - What patterns did you notice in the scatter plot?  
   - Why is feature selection and preprocessing important for clustering?  
   - How would you extend this dataset for deeper analysis (e.g., adding online shopping behavior)?

- **Key Takeaways:**  
   - Unsupervised learning doesn’t rely on labels but finds patterns in raw data.  
   - Data visualization is a powerful tool to identify potential clusters.  
   - Preprocessing is a crucial step for accurate clustering.

---

### **Outcome:**  
By the end of this exercise, students will:  
- Understand the difference between supervised and unsupervised learning.  
- Create visualizations to explore data patterns.  
- Prepare data through feature selection and preprocessing, ready for clustering.  
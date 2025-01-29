### **Walkthrough of K-Means Clustering with a Solution: Customer Segmentation in a Coffee Shop**

[Download Dataset](KMeans_Realistic_CustomerData_20K.csv)

We will perform **K-Means Clustering** step by step using Python to analyze customer data for a coffee shop.

---

## **Step 1: Problem Definition**
A coffee shop wants to segment its customers based on:
- **Spending per visit ($)**
- **Visit frequency per month**

📌 **Objective:** Identify customer groups and optimize marketing strategies for each segment.

---

## **Step 2: Importing Required Libraries**
We will use **Pandas, NumPy, Matplotlib, and Scikit-learn** for data handling, visualization, and clustering.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
```

---

## **Step 3: Creating the Dataset**
We simulate customer spending and visit frequency data.

```python
# Creating a sample dataset
data = {
    'Customer': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Spending ($)': [5, 20, 7, 30, 25, 6, 50, 35, 10, 15],
    'Frequency (visits/month)': [20, 5, 15, 3, 8, 18, 2, 6, 12, 10]
}

# Converting to DataFrame
df = pd.DataFrame(data)

# Extracting features for clustering
X = df[['Spending ($)', 'Frequency (visits/month)']]

# Display data
import ace_tools as tools
tools.display_dataframe_to_user(name="Customer Data", dataframe=df)
```

---

## **Step 4: Visualizing the Data**
Before applying K-Means, let's visualize customer spending vs. visit frequency.

```python
# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Frequency (visits/month)'], df['Spending ($)'], color='blue', s=100, edgecolors='black')
plt.xlabel('Visit Frequency per Month')
plt.ylabel('Spending per Visit ($)')
plt.title('Customer Clusters (Before Clustering)')
plt.grid()
plt.show()
```

---

## **Step 5: Applying the Elbow Method to Find Optimal K**
We use the **Elbow Method** to determine the optimal number of clusters.

```python
# Finding the optimal K using the Elbow Method
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)  # Within-cluster sum of squares

# Plotting the Elbow Method graph
plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--', color='red')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.title('Elbow Method for Optimal K')
plt.show()
```

🔎 **Observation:** The "elbow" appears around **K=3**, meaning **three clusters** is a good choice.

---

## **Step 6: Applying K-Means Clustering**
Now we cluster customers into **3 groups** based on spending and visit frequency.

```python
# Applying K-Means
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Extracting cluster centroids
centroids = kmeans.cluster_centers_

# Display updated DataFrame with clusters
tools.display_dataframe_to_user(name="Segmented Customer Data", dataframe=df)
```

---

## **Step 7: Visualizing the Clusters**
We now plot the clusters along with their centroids.

```python
# Plot clustered data
plt.figure(figsize=(8, 6))
for cluster in range(3):
    plt.scatter(X[df['Cluster'] == cluster]['Frequency (visits/month)'], 
                X[df['Cluster'] == cluster]['Spending ($)'], s=100, edgecolors='black', label=f'Cluster {cluster}')

# Plot centroids
plt.scatter(centroids[:, 1], centroids[:, 0], s=300, c='black', marker='X', label='Centroids')

plt.xlabel('Visit Frequency per Month')
plt.ylabel('Spending per Visit ($)')
plt.title('Customer Clusters (After K-Means Clustering)')
plt.legend()
plt.grid()
plt.show()
```

---

## **Step 8: Understanding the Clusters**
Now, let's interpret the **three customer segments**:

| Cluster | Description | Customers |
|---------|------------|-----------|
| **Cluster 0** | Frequent Visitors, Low Spending | Customers who visit often but spend little. |
| **Cluster 1** | Premium Customers | Customers who visit regularly and spend a lot. |
| **Cluster 2** | Occasional Big Spenders | Customers who visit rarely but make high-value purchases. |

---

## **Step 9: Business Strategy Based on Clusters**
Based on customer segments, we **implement marketing strategies**:

- **Frequent Visitors, Low Spending (Cluster 0)**  
  ✅ **Loyalty Programs**: Free coffee after 10 visits.  
  ✅ **Discount Coupons** to encourage higher spending.

- **Premium Customers (Cluster 1)**  
  ✅ **VIP Benefits**: Exclusive offers on new drinks.  
  ✅ **Personalized Recommendations** to enhance experience.

- **Occasional Big Spenders (Cluster 2)**  
  ✅ **Event Promotions**: Invite them to limited-time offers.  
  ✅ **Bundle Offers**: Discount on buying multiple items.

---

## **Final Thoughts**
K-Means Clustering helped us:
✅ **Segment customers effectively.**  
✅ **Optimize marketing strategies.**  
✅ **Boost customer satisfaction and revenue.**

---

This real-world walkthrough provides an **end-to-end solution** using **Python and K-Means Clustering** for **customer segmentation**. Let me know if you have any questions! 🚀
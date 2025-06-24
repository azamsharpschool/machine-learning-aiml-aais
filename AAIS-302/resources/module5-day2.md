
# 🧠 Beginner’s Guide to K-Means Clustering in Healthcare

## 📊 Grouping Patients for Early Disease Detection

---

### ✅ What You’ll Learn

In this hands-on guide, you’ll use **K-Means clustering**, a popular machine learning algorithm, to **group patients based on medical data**. The goal? Help healthcare professionals **spot high-risk individuals early** so they can receive faster and more personalized care.

---

### 🩺 Real-World Problem

A hospital wants to make sense of its growing patient records. Instead of manually reviewing thousands of files, we’ll use **K-Means** to automatically cluster patients by health risk based on:

* **Age**
* **BMI**
* **Blood Pressure**
* **Glucose Level**
* **Cholesterol Level**

🎯 Our goal: Create **3 clusters** (Low Risk, Moderate Risk, High Risk)

---

### 🏁 Step 1: Sample Patient Data

Here’s a simplified dataset with 10 patients:

| Patient | Age | BMI  | Blood Pressure | Glucose | Cholesterol |
| ------- | --- | ---- | -------------- | ------- | ----------- |
| 1       | 35  | 22.5 | 120            | 85      | 190         |
| 2       | 50  | 27.3 | 140            | 120     | 250         |
| 3       | 40  | 25.8 | 130            | 110     | 230         |
| 4       | 28  | 21.4 | 110            | 75      | 180         |
| 5       | 60  | 29.0 | 145            | 140     | 270         |
| ...     | ... | ...  | ...            | ...     | ...         |

🔍 We want to group these patients by **health similarity** using unsupervised learning.

---

### ⚙️ Step 2: What Is K-Means Clustering?

K-Means is an **unsupervised learning algorithm** that:

1. **Picks `k` clusters** (we’ll use `k = 3`)
2. Randomly assigns each data point (patient) to a cluster
3. Calculates a **centroid** (center) for each cluster
4. Moves patients to the **nearest centroid**
5. Repeats until clusters no longer change

💡 **Why K-Means?**
It helps you find patterns in data *without* labeled answers—perfect when you don’t know who is "high-risk" in advance.

---

### 🔧 Step 3: Prepare the Data

Use only **Age** and **Glucose Level** to keep it simple and easy to visualize.

#### Python Code:

```python
import pandas as pd

data = {
    'Age': [35, 50, 40, 28, 60, 45, 33, 55, 70, 25],
    'Glucose Level': [85, 120, 110, 75, 140, 130, 90, 135, 160, 80]
}
df = pd.DataFrame(data)
```

---

### 📐 Step 4: Normalize the Data

Why normalize? Because **Age** and **Glucose** are on different scales. Without normalization, one might dominate the clustering process.

#### Code:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
```

---

### 🤖 Step 5: Apply K-Means Clustering

```python
from sklearn.cluster import KMeans

# Use 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df_scaled)
```

Now every patient is assigned a **cluster label** (0, 1, or 2).

---

### 📊 Step 6: Visualize the Clusters

```python
import matplotlib.pyplot as plt

# Scatter plot of clusters
plt.scatter(df['Age'], df['Glucose Level'], c=df['Cluster'], cmap='viridis', s=100)

# Optional: Plot centroids
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')

plt.title("Patient Clusters by Age and Glucose Level")
plt.xlabel("Age")
plt.ylabel("Glucose Level")
plt.legend()
plt.show()
```

🟢 Each color = one cluster
❌ Red “X” = cluster center

---

### 🧠 Step 7: Interpret the Clusters

| Cluster | Typical Traits            | Health Status         |
| ------- | ------------------------- | --------------------- |
| 0       | Young, low glucose        | Healthy (Low risk)    |
| 1       | Mid-age, moderate glucose | Monitor (Medium risk) |
| 2       | Older, high glucose       | High-risk             |

📌 Note: Your actual labels may vary depending on initialization—K-Means is unsupervised.

---

### 🩺 Step 8: Use It in Healthcare

✅ **Prioritize high-risk groups** for screenings
✅ **Customize advice** for moderate-risk patients
✅ **Track progress** over time using cluster shifts

🔬 You can expand this to include:

* **BMI**, **Blood Pressure**
* **Historical trends**
* **More sophisticated clustering (e.g., DBSCAN, GMM)**

---

### 📚 Recap: What You Learned

* ✅ What K-Means clustering is
* ✅ How to apply it using `scikit-learn`
* ✅ How to normalize health data
* ✅ How clustering helps identify patient risk levels

---

### 💡 Final Thought

K-Means clustering isn’t just about math—it’s about saving lives with data. Use it wisely, test your assumptions, and always validate your models with medical professionals.


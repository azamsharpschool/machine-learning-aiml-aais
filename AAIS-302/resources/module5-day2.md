
# **Beginner’s Guide to K-Means Clustering in Healthcare**
## **Grouping Patients for Early Disease Detection**

## **What You Will Learn**
In this guide, you will learn how to apply **K-Means clustering**, a machine learning algorithm, to group patients based on their medical data. This technique helps doctors **identify high-risk patients**, leading to **early diagnosis** and **personalized treatment plans**.

---

## **Understanding the Problem**
Imagine a hospital wants to analyze patient data to detect health risks. Instead of manually sorting through large amounts of patient records, **K-Means clustering** can automatically group patients based on **similar symptoms**.

### **Example Scenario: Diagnosing Common Diseases**
Doctors collect data from patients, such as:
- **Age**
- **BMI (Body Mass Index)**
- **Blood Pressure**
- **Glucose Level**
- **Cholesterol Level**

Using **K-Means clustering**, we can **group** patients into different risk categories:
1. **Low risk** (healthy)
2. **Moderate risk** (needs monitoring)
3. **High risk** (urgent medical attention)

Let’s walk through the entire process step by step.

---

## **Step 1: Collect Patient Data**
The first step is collecting medical information from patients. Below is an example dataset of **10 patients** with their medical measurements:

| **Patient ID** | **Age** | **BMI** | **Blood Pressure** | **Glucose Level** | **Cholesterol Level** |
|---------------|--------|--------|-----------------|----------------|------------------|
| 1            | 35     | 22.5   | 120             | 85             | 190              |
| 2            | 50     | 27.3   | 140             | 120            | 250              |
| 3            | 40     | 25.8   | 130             | 110            | 230              |
| 4            | 28     | 21.4   | 110             | 75             | 180              |
| 5            | 60     | 29.0   | 145             | 140            | 270              |
| 6            | 45     | 26.1   | 135             | 130            | 240              |
| 7            | 33     | 23.5   | 118             | 90             | 200              |
| 8            | 55     | 28.2   | 142             | 135            | 260              |
| 9            | 70     | 30.0   | 150             | 160            | 290              |
| 10           | 25     | 20.5   | 105             | 80             | 170              |

🔹 **What do we want to do?**  
We want to **group these patients** based on their **similarity** using **K-Means clustering**.

---

## **Step 2: Understanding K-Means Clustering**
K-Means is a machine learning algorithm that **automatically finds groups (clusters) in data**.

### **How It Works**
1. **Choose a number of clusters (`k`)**  
   - Here, we select **k = 3** to create **three groups** (low, moderate, high risk).

2. **Assign patients to random clusters**  
   - Each patient is randomly assigned to one of the three groups.

3. **Find the "center" of each cluster (centroid)**  
   - The centroid is the **average** of all points in a cluster.

4. **Reassign patients**  
   - Patients are reassigned to the nearest centroid.

5. **Repeat steps 3 and 4 until clusters stabilize**  
   - The clusters stop changing, and we get final groups.

---

## **Step 3: Preparing the Data**
Before applying K-Means, we need to **normalize** the data.  
Why?  
- **Different scales** can bias clustering (e.g., Glucose Level is much larger than BMI).  
- **Normalization** ensures all features contribute equally.

📌 **Steps to normalize the data:**
1. Subtract the **mean** from each value.
2. Divide by the **range** (max - min) of that feature.

---

## **Step 4: Apply K-Means Clustering**
Now, let’s write a **Python program** to apply K-Means clustering to our patient dataset.

### **Step 4.1: Import Required Libraries**
```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
```
🔹 **Why these libraries?**
- `pandas`: Handles data tables.
- `matplotlib.pyplot`: Creates graphs.
- `sklearn.cluster.KMeans`: Runs K-Means clustering.
- `sklearn.preprocessing.StandardScaler`: Normalizes data.

---

### **Step 4.2: Load the Data**
```python
# Create a DataFrame with patient data
data = {
    'Age': [35, 50, 40, 28, 60, 45, 33, 55, 70, 25],
    'Glucose Level': [85, 120, 110, 75, 140, 130, 90, 135, 160, 80]
}
df = pd.DataFrame(data)
```
🔹 **We are using only two features (`Age` and `Glucose Level`) to visualize the clusters.**

---

### **Step 4.3: Normalize the Data**
```python
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
```
🔹 **StandardScaler** ensures that all values are on the same scale.

---

### **Step 4.4: Run K-Means Clustering**
```python
# Apply K-Means with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df_scaled)
```
🔹 **What does this do?**
- **Groups patients** into **three** clusters.
- **Assigns a cluster number** to each patient.

---

## **Step 5: Visualize the Results**
We can plot the clusters using a **scatter plot**.

```python
# Plot the clusters
plt.scatter(df['Age'], df['Glucose Level'], c=df['Cluster'], cmap='viridis', s=100)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            c='red', marker='X', s=200, label='Centroids')
plt.title('Patient Clustering by Age and Glucose Level')
plt.xlabel('Age')
plt.ylabel('Glucose Level')
plt.legend()
plt.show()
```
🔹 **What does this plot show?**
- **Each dot represents a patient**.
- **Colors represent clusters**.
- **Red "X" marks are centroids (cluster centers)**.

---

## **Step 6: Interpret the Results**
After clustering, we can analyze the **three groups**:

| **Cluster** | **Description** | **Possible Health Status** |
|------------|----------------|----------------------------|
| Cluster 1  | Younger, lower glucose levels | Likely **healthy** |
| Cluster 2  | Middle-aged, moderate glucose | **Monitor** for pre-diabetes |
| Cluster 3  | Older, high glucose levels | **High-risk** of diabetes |

---

## **Step 7: Taking Action**
Based on clustering, doctors can:
✅ **Prioritize high-risk patients** for additional tests.  
✅ **Advise moderate-risk patients** on lifestyle changes.  
✅ **Reassure low-risk patients** with general health maintenance.

🔹 **Real-World Extensions:**
- Use more features (**Blood Pressure, BMI, Cholesterol**) for accurate grouping.
- Apply K-Means to **genetic mutations** for disease predictions.
- Cluster **MRI images** to detect brain abnormalities.

---

## **Final Thoughts**
🔹 **What We Learned:**
✅ How to apply **K-Means clustering** to real healthcare data.  
✅ How to use Python’s `sklearn` to **analyze patient groups**.  
✅ How clustering helps **early disease detection** and **personalized healthcare**.

Now, you can **apply K-Means** to any dataset and uncover hidden patterns in data! 🚀
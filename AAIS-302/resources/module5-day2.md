### Real-Life Example: **K-Means in Healthcare**

---

**Objective:**  
Use K-Means clustering to group patients based on symptoms and medical data for early disease detection and personalized treatment plans.

---

### **Scenario: Classifying Patients Based on Symptoms**

#### **Context:**  
A hospital wants to identify groups of patients showing similar symptoms to help diagnose and manage common diseases like diabetes, hypertension, or heart conditions. By clustering patient data, doctors can group individuals for targeted diagnostics and treatment.

---

#### **Dataset Description:**  
- **Features:** Age, BMI, Blood Pressure, Glucose Level, and Cholesterol Level.  
- **Goal:** Use K-Means clustering to group patients into clusters that represent potential risk groups for specific diseases.

---

### **Step-by-Step Example:**

#### **Step 1: Data Collection**
- Patient data is collected during routine health check-ups.  
- Example data for 10 patients:  

| **Patient ID** | **Age** | **BMI** | **Blood Pressure** | **Glucose Level** | **Cholesterol Level** |
|----------------|---------|---------|--------------------|-------------------|-----------------------|
| 1              | 35      | 22.5    | 120                | 85                | 190                   |
| 2              | 50      | 27.3    | 140                | 120               | 250                   |
| 3              | 40      | 25.8    | 130                | 110               | 230                   |
| ...            | ...     | ...     | ...                | ...               | ...                   |

---

#### **Step 2: Apply K-Means Clustering**
- Normalize the dataset to avoid bias due to differences in scales (e.g., glucose level and age).  
- Use K-Means with `k=3` to group patients into three clusters:  
  - **Cluster 1:** Low risk.  
  - **Cluster 2:** Moderate risk.  
  - **Cluster 3:** High risk.  

---

#### **Step 3: Visualize Results**
- After applying K-Means, each patient is assigned a cluster based on their features.  
- Visualize the clusters using a 2D scatter plot for two features (e.g., Age vs. Glucose Level):  

```python
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

# Example data
data = {
    'Age': [35, 50, 40, 28, 60, 45, 33, 55, 70, 25],
    'Glucose Level': [85, 120, 110, 75, 140, 130, 90, 135, 160, 80]
}
df = pd.DataFrame(data)

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df)

# Plot results
plt.scatter(df['Age'], df['Glucose Level'], c=df['Cluster'], cmap='viridis', s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title('Patient Clustering by Age and Glucose Level')
plt.xlabel('Age')
plt.ylabel('Glucose Level')
plt.legend()
plt.show()
```

---

#### **Step 4: Interpret the Clusters**
- **Cluster 1:** Young patients with low glucose levels (likely healthy).  
- **Cluster 2:** Middle-aged patients with moderate glucose levels (monitor for pre-diabetes).  
- **Cluster 3:** Older patients with high glucose levels (high-risk group for diabetes).  

---

#### **Step 5: Healthcare Actions**
- Doctors can prioritize patients in Cluster 3 for additional testing or early intervention programs.  
- Patients in Cluster 2 are advised on lifestyle changes to prevent disease progression.  
- Cluster 1 patients are given general health maintenance recommendations.

---

### **Extension:**
This approach can be expanded for:  
- Grouping patients by DNA mutations to identify genetic predispositions for conditions.  
- Clustering MRI images to distinguish between healthy and abnormal brain scans.

**Impact:**  
K-Means clustering helps personalize healthcare, enabling faster diagnosis and more efficient allocation of medical resources.
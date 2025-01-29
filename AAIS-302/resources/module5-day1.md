
# Step-by-Step Guide to K-Means Clustering with Python: Customer Segmentation & Elbow Method

[Download DataSet](income_data.csv)

## 🚀 **Step 1: Open in Google Colab**
- If you're using **Google Colab**, open a new notebook.
- Copy and paste the provided code into a cell.
- If you're using **Jupyter Notebook**, you can also run the same code there.

---

## **🔹 Step 2: Import Required Libraries**
First, we need to import the necessary libraries:

```python
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
%matplotlib inline
```

### **What Do These Libraries Do?**
- `sklearn.cluster.KMeans`: Used for K-Means clustering.
- `pandas`: Helps us work with structured data (CSV files).
- `sklearn.preprocessing.MinMaxScaler`: Used to scale data for better clustering results.
- `matplotlib.pyplot`: Helps us visualize data.
- `%matplotlib inline`: Ensures that graphs appear in the notebook.

---

## **🔹 Step 3: Load and View Data**
We will load a dataset containing people's **age** and **income**.

```python
df = pd.read_csv("income.csv")
df.head()
```

### **Sample Data (income.csv)**
| Name  | Age | Income($) |
|-------|----:|---------:|
| Rob   |  27 |   70000  |
| Michael | 29 |   90000  |
| Mohan |  29 |   61000  |
| Ismail | 28 |   60000  |
| Kory  |  42 |  150000  |

---

## **🔹 Step 4: Visualizing the Data**
We can plot **Age vs Income** to see if any patterns exist.

```python
plt.scatter(df.Age, df['Income($)'])
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.show()
```
This scatter plot will show how people’s income varies with their age.

---

## **🔹 Step 5: Applying K-Means Clustering**
Now, we apply **K-Means** to group the data into **3 clusters**.

```python
km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Age', 'Income($)']])
df['cluster'] = y_predicted
df.head()
```

### **How K-Means Works Here?**
- It **chooses 3 centroids** randomly.
- Each data point is **assigned to the nearest centroid**.
- Centroids are **recalculated** based on the mean of assigned points.
- This **repeats until no changes occur** in the clusters.

---

## **🔹 Step 6: Visualizing Clusters**
Now, we separate the data by clusters and plot them.

```python
df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]

plt.scatter(df1.Age, df1['Income($)'], color='green')
plt.scatter(df2.Age, df2['Income($)'], color='red')
plt.scatter(df3.Age, df3['Income($)'], color='black')

plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], color='purple', marker='*', label='centroid')

plt.xlabel('Age')
plt.ylabel('Income ($)')
plt.legend()
plt.show()
```

### **What Does This Show?**
- Points are **grouped into 3 clusters** (colors).
- The **purple stars** represent the **centroids** of the clusters.

---

## **🔹 Step 7: Preprocessing with Min-Max Scaling**
Since **income and age have different ranges**, we **scale them** for better clustering.

```python
scaler = MinMaxScaler()

scaler.fit(df[['Income($)']])
df['Income($)'] = scaler.transform(df[['Income($)']])

scaler.fit(df[['Age']])
df['Age'] = scaler.transform(df[['Age']])

df.head()
```

### **Why Scale the Data?**
- **Before scaling:**  
  - Age: `27 - 50`  
  - Income: `$60,000 - $150,000`  
- **After scaling:**  
  - Age: `0 - 1`
  - Income: `0 - 1`
  
👉 This ensures that **both features contribute equally** in clustering.

---

## **🔹 Step 8: Reapply K-Means on Scaled Data**
```python
km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Age', 'Income($)']])
df['cluster'] = y_predicted
df.head()
```

Now, clustering will be **more accurate** since values are scaled.

---

## **🔹 Step 9: Visualizing Scaled Clusters**
```python
df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]

plt.scatter(df1.Age, df1['Income($)'], color='green')
plt.scatter(df2.Age, df2['Income($)'], color='red')
plt.scatter(df3.Age, df3['Income($)'], color='black')

plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], color='purple', marker='*', label='centroid')

plt.legend()
plt.show()
```

🎯 Now, the clustering is **more accurate** because **scaled data removes bias**.

---

## **🔹 Step 10: Finding the Optimal K Using the Elbow Method**
The **Elbow Method** helps determine the best number of clusters.

```python
sse = []
k_rng = range(1,10)

for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['Age', 'Income($)']])
    sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng, sse)
plt.show()
```

### **What’s Happening?**
- **SSE (Sum of Squared Errors)** measures how well data fits into clusters.
- The **elbow point** (where the curve bends) suggests the **optimal K value**.

---

## **🎯 Exercise: Clustering Iris Flowers**
### **Your Task**
1️⃣ Load the **Iris dataset** from `sklearn`.  
2️⃣ Use **only Petal Width & Petal Length** for clustering.  
3️⃣ Apply **K-Means** and visualize clusters.  
4️⃣ Check if **scaling improves clustering**.  
5️⃣ **Use the Elbow Method** to find the best `K`.

### **Starter Code**
```python
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# Load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Keep only Petal Length and Petal Width
df = df[['petal length (cm)', 'petal width (cm)']]

# Scale data
scaler = MinMaxScaler()
df[['petal length (cm)', 'petal width (cm)']] = scaler.fit_transform(df[['petal length (cm)', 'petal width (cm)']])

# Apply K-Means
km = KMeans(n_clusters=3)
df['cluster'] = km.fit_predict(df[['petal length (cm)', 'petal width (cm)']])

# Plot clusters
plt.scatter(df['petal length (cm)'], df['petal width (cm)'], c=df['cluster'])
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()

# Elbow Method
sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['petal length (cm)', 'petal width (cm)']])
    sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Sum of Squared Error')
plt.plot(k_rng, sse)
plt.show()
```

👉 **Find the elbow point and choose the best K value!** 💡

---

## **✅ Summary**
✔ We **applied K-Means** to customer income data.  
✔ **Scaled the data** for better clustering.  
✔ **Plotted clusters and centroids**.  
✔ Used the **Elbow Method** to choose the best `K`.  
✔ Gave you an **Iris dataset exercise** for practice! 🚀

Would you like me to explain anything in more detail? 😊
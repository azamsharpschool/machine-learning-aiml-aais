
# 🧭 Walkthrough: Real-World Scenario for Outlier Detection

**🔍 Title:** Detecting Outliers in House Prices

---

### 🎯 Objective

Learn how to **identify, visualize, and handle outliers** in house price data using Python. This is essential for building better prediction models and making trustworthy real estate decisions.

---

### 🏡 Real-World Scenario

You're working with a real estate company analyzing house prices. Some houses are **extremely expensive or unusually cheap** compared to others. These “outliers” can distort your analysis, so you need to detect and deal with them properly.

---

## 🧪 Step-by-Step Walkthrough

---

### 🧰 Step 1: Load the Dataset

Let’s simulate a small dataset of houses, showing area and price.

```python
import pandas as pd

# Create dataset
data = {
    'Area': [1200, 1500, 1700, 2000, 5000, 1400, 1600, 1800, 3000, 10000],
    'Price': [300000, 350000, 400000, 450000, 900000, 320000, 370000, 420000, 600000, 2000000]
}
df = pd.DataFrame(data)
print(df)
```

✅ Each row shows a house's area (in sq ft) and its price in dollars.

---

### 📊 Step 2: Visualize the Data

Plot a scatter graph to visually inspect the data.

```python
import matplotlib.pyplot as plt

# Basic scatter plot
plt.scatter(df['Area'], df['Price'], color='blue', s=50)
plt.title('House Prices vs Area')
plt.xlabel('Area (sq ft)')
plt.ylabel('Price ($)')
plt.grid(True)
plt.show()
```

🔎 **What to look for:**
Notice how some points are far away from the cluster — they’re **potential outliers**.

---

### 🧠 Step 3: Detect Outliers with Isolation Forest

We’ll use the **Isolation Forest** algorithm to automatically detect unusual data points.

```python
from sklearn.ensemble import IsolationForest

# Create model
iso_forest = IsolationForest(contamination=0.1, random_state=42)
df['Anomaly'] = iso_forest.fit_predict(df[['Area', 'Price']])
```

* `Anomaly = 1` → Normal
* `Anomaly = -1` → Outlier

Now separate them:

```python
# Split data
normal = df[df['Anomaly'] == 1]
outliers = df[df['Anomaly'] == -1]
```

✅ About 10% (based on `contamination=0.1`) will be marked as outliers.

---

### 🎨 Step 4: Visualize Outliers

Plot the results — highlight outliers in red:

```python
# Visualize
plt.scatter(normal['Area'], normal['Price'], color='blue', label='Normal', s=50)
plt.scatter(outliers['Area'], outliers['Price'], color='red', label='Outlier', s=50)
plt.title('Outlier Detection (Isolation Forest)')
plt.xlabel('Area (sq ft)')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.show()
```

🔴 Outliers stand out clearly in red. This helps non-technical stakeholders understand the problem too.

---

### 🧹 Step 5: Clean the Data (Optional)

Once identified, you can choose to remove the outliers:

```python
# Remove outliers
cleaned_df = df[df['Anomaly'] == 1].drop(columns='Anomaly')
print(cleaned_df)
```

You’re now ready to perform **clean regression analysis**, **build models**, or **create dashboards** with more accurate data.

---

## 💬 Discussion Questions

1. **Why is detecting outliers important in pricing models?**
2. **When would you keep an outlier instead of removing it?**
3. **How does changing the `contamination` value affect the model?**

---

## 🚀 Learning Outcomes

By completing this walkthrough, you’ve learned how to:

✅ Detect outliers both visually and using machine learning
✅ Interpret real-world consequences of anomalies
✅ Prepare a clean dataset for better analysis

---

## 🌍 Real-World Applications

| Industry      | Outlier Example                       |
| ------------- | ------------------------------------- |
| Real Estate   | Unusual home pricing                  |
| Finance       | Suspicious transactions (fraud)       |
| Healthcare    | Abnormal lab results or diagnoses     |
| Manufacturing | Defective products in production line |


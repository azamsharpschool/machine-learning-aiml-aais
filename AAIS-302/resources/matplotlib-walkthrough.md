
# 🖼 Beginner’s Guide to **Matplotlib** in Python

## 🎯 Goal

By the end, you’ll be able to create **simple and colorful charts** (line plots, bar charts, scatter plots) using Matplotlib.

---

## 1️⃣ What is Matplotlib?

Matplotlib is **Python’s most popular plotting library**.
Think of it as your “paintbrush” for turning numbers into **pictures** — graphs, charts, and plots.

📦 Installation:

```bash
pip install matplotlib
```

---

## 2️⃣ The Basics — Import & Setup

Matplotlib’s most used module is `pyplot` (similar to MATLAB’s plotting style).

```python
import matplotlib.pyplot as plt
```

---

## 3️⃣ First Plot — A Simple Line Graph

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y)

# Add labels and title
plt.xlabel("X Axis - Numbers")
plt.ylabel("Y Axis - Doubled")
plt.title("Simple Line Plot")

# Show the plot
plt.show()
```

✅ **What’s Happening:**

* `plt.plot()` → draws the line graph
* `plt.xlabel()` / `plt.ylabel()` → label your axes
* `plt.title()` → add a title
* `plt.show()` → makes the plot window appear

---

## 4️⃣ Adding Style — Colors, Markers & Lines

You can customize the look:

```python
plt.plot(x, y, color="red", marker="o", linestyle="--", linewidth=2)
plt.show()
```

* `color` → `'red'`, `'blue'`, or hex codes like `'#1f77b4'`
* `marker` → `'o'` (circle), `'^'` (triangle), `'s'` (square)
* `linestyle` → `'-'`, `'--'`, `':'`
* `linewidth` → thickness of the line

---

## 5️⃣ Bar Charts

```python
categories = ["Apples", "Bananas", "Cherries"]
values = [10, 15, 7]

plt.bar(categories, values, color="orange")
plt.title("Fruit Count")
plt.show()
```

---

## 6️⃣ Scatter Plots

```python
x = [5, 7, 8, 7, 6, 9, 5, 7, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94]

plt.scatter(x, y, color="purple")
plt.title("Height vs Weight")
plt.show()
```

---

## 7️⃣ Multiple Plots in One Figure

```python
# Data for two lines
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [2, 4, 6, 8]

plt.plot(x, y1, label="Squares", color="blue")
plt.plot(x, y2, label="Doubles", color="green")

plt.title("Two Lines on One Plot")
plt.legend()  # Show labels
plt.show()
```

---

## 8️⃣ Saving Plots

```python
plt.savefig("my_plot.png")  # Save before plt.show()
```

---

## 9️⃣ Quick Tips for Beginners

* Always label your axes so people understand your data
* Use `plt.grid(True)` to make reading easier
* Use contrasting colors for clarity
* Start small — learn line, bar, and scatter before advanced plots

---

## 🔍 Summary Table

| Task         | Function/Method                 |
| ------------ | ------------------------------- |
| Line plot    | `plt.plot()`                    |
| Bar chart    | `plt.bar()`                     |
| Scatter plot | `plt.scatter()`                 |
| Add title    | `plt.title()`                   |
| Add labels   | `plt.xlabel()` / `plt.ylabel()` |
| Show plot    | `plt.show()`                    |
| Save plot    | `plt.savefig()`                 |

---


**Download the dataset:** [home\_prices.csv](sandbox:/mnt/data/home_prices.csv)

Here’s the step‑by‑step you can run locally:

```python
# 1) Setup
pip install matplotlib pandas
```

```python
# 2) Imports
import pandas as pd
import matplotlib.pyplot as plt

# 3) Load the dataset
df = pd.read_csv("home_prices.csv")  # use the downloaded file path

df.head()
```

### A. Price vs. Living Area (scatter)

Good for spotting how price changes with square footage.

```python
plt.figure()
plt.scatter(df["sqft_living"], df["price"])
plt.xlabel("Living Area (sqft)")
plt.ylabel("Price (USD)")
plt.title("Home Price vs Living Area")
plt.grid(True)
plt.show()
```

### B. Average Price by Bedrooms (bar)

Great to compare categories.

```python
avg_by_bed = df.groupby("bedrooms")["price"].mean()

plt.figure()
plt.bar(avg_by_bed.index.astype(str), avg_by_bed.values)
plt.xlabel("Bedrooms")
plt.ylabel("Average Price (USD)")
plt.title("Average Home Price by # of Bedrooms")
plt.grid(axis="y")
plt.show()
```

### C. Distribution of Prices (histogram)

See typical price ranges and skew.

```python
plt.figure()
plt.hist(df["price"], bins=25)
plt.xlabel("Price (USD)")
plt.ylabel("Count")
plt.title("Distribution of Home Prices")
plt.grid(True)
plt.show()
```

### D. Median Price by Build Decade (line)

A simple “trend over time” view.

```python
decade = (df["year_built"] // 10) * 10
median_by_decade = df.groupby(decade)["price"].median()

plt.figure()
plt.plot(median_by_decade.index.astype(int), median_by_decade.values, marker="o")
plt.xlabel("Build Decade")
plt.ylabel("Median Price (USD)")
plt.title("Median Price by Build Decade")
plt.grid(True)
plt.show()
```


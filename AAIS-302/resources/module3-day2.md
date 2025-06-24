
# 🎨 Day 2 Walkthrough: **Introduction to Matplotlib**

---

## 🧠 Learning Goals

By the end of today, you’ll be able to:

* Create and display basic plots using `matplotlib.pyplot`
* Add titles, labels, and legends to explain your charts
* Apply different styles to customize the look of your visualizations
* Plot multiple lines in one chart
* Save your plots as image files for presentations or reports

---

## 📦 Prerequisites

Make sure Matplotlib is installed:

```bash
pip install matplotlib
```

And import it before starting:

```python
import matplotlib.pyplot as plt
```

---

## ✏️ **Activity 1: Creating Basic Plots**

### ✅ Objective:

Create your **first line plot** using a simple dataset.

### 🪜 Steps:

```python
import matplotlib.pyplot as plt

# Create a simple dataset
data = [1, 2, 3, 4]

# Plot the data
plt.plot(data)

# Display the plot
plt.show()
```

### 📈 Expected Output:

A line plot connecting the points: 1 → 2 → 3 → 4.

📌 By default, Python assumes your x-values are `[0, 1, 2, 3]` and plots them against the y-values `[1, 2, 3, 4]`.

---

## 🏷️ **Activity 2: Adding Labels and Titles**

### ✅ Objective:

Make your plot **readable and informative** by labeling the axes and adding a title.

### 🪜 Steps:

```python
data = [1, 2, 3, 4]
plt.plot(data)

# Add a title and axis labels
plt.title('My First Line Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

plt.show()
```

### 🧠 Why It Matters:

Good charts tell a story. Titles and labels help others interpret your results quickly.

---

## 🎨 **Activity 3: Customizing Plot Styles**

### ✅ Objective:

Explore built-in Matplotlib styles to give your charts a **professional or creative look**.

### 🪜 Steps:

```python
# View available styles
print(plt.style.available)
```

Choose one and apply it:

```python
plt.style.use('ggplot')  # Try 'seaborn', 'dark_background', etc.
```

Then recreate your labeled plot:

```python
data = [1, 2, 3, 4]
plt.plot(data)
plt.title('Styled Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```

### 🎨 Tip:

Try applying different styles and compare:

```python
for style in ['seaborn', 'ggplot', 'classic']:
    plt.style.use(style)
    plt.plot(data)
    plt.title(f'Plot Style: {style}')
    plt.show()
```

---

## 🔀 **Activity 4: Plotting Multiple Lines**

### ✅ Objective:

Visualize **two related datasets** in a single chart, each with different formatting.

### 🪜 Steps:

```python
data1 = [1, 2, 3, 4]
data2 = [4, 3, 2, 1]

# Plot both datasets with different styles
plt.plot(data1, label='Data 1', linestyle='-', color='blue')
plt.plot(data2, label='Data 2', linestyle='--', color='red')

# Add a legend
plt.legend()

plt.title('Multiple Line Plot')
plt.xlabel('Index')
plt.ylabel('Values')
plt.show()
```

### 🧠 Why It Matters:

This is useful when comparing trends, such as actual vs predicted values in machine learning.

---

## 💾 **Activity 5: Saving Your Plots**

### ✅ Objective:

Save your visualizations as images or PDFs for sharing or reporting.

### 🪜 Steps:

```python
data = [1, 2, 3, 4]
plt.plot(data)
plt.title('Plot to Save')

# Save as PNG
plt.savefig('my_plot.png')

# Save as PDF
plt.savefig('my_plot.pdf')

# Show the plot
plt.show()
```

📁 Check your project directory — the files should be saved there.

---

## 💡 Bonus Tips

* Use `plt.grid(True)` to add helpful gridlines.

* Save high-resolution plots using:

  ```python
  plt.savefig('plot_highres.png', dpi=300)
  ```

* Add markers for better readability:

  ```python
  plt.plot(data, marker='o')
  ```

---

## 🎓 Summary of Skills Learned

| Concept             | Method/Command                |
| ------------------- | ----------------------------- |
| Create basic plot   | `plt.plot()`                  |
| Show plot           | `plt.show()`                  |
| Add title/labels    | `plt.title()`, `plt.xlabel()` |
| Change style        | `plt.style.use()`             |
| Plot multiple lines | `plt.plot()` with `label`     |
| Add legend          | `plt.legend()`                |
| Save plots          | `plt.savefig()`               |

---

## 🧩 Challenge Activities

1. Plot three datasets with different styles and add a legend.
2. Try plotting real-world data (e.g., daily temperatures).
3. Use different plot types like `plt.bar()` or `plt.scatter()`.


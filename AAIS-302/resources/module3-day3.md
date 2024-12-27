### Day 3: Advanced Visualizations with Matplotlib - Beginner Walkthrough

#### Activity 1: Scatterplots
**Goal**: Learn how to visualize relationships between two variables using scatterplots.

1. **Setup**:
   - Import `matplotlib.pyplot` as `plt`.
   - Prepare two lists or arrays, e.g., `age = [22, 25, 30, 35, 40]` and `income = [2000, 2500, 3000, 3500, 4000]`.

2. **Create a Scatterplot**:
   ```python
   import matplotlib.pyplot as plt
   
   age = [22, 25, 30, 35, 40]
   income = [2000, 2500, 3000, 3500, 4000]
   
   plt.scatter(age, income, color='blue', marker='o')
   plt.title('Age vs Income')
   plt.xlabel('Age')
   plt.ylabel('Income')
   plt.show()
   ```

3. **Experiment**:
   - Change the `color` or `marker` parameters.
   - Add labels to each point using `plt.text()`.

---

#### Activity 2: Bar Charts
**Goal**: Create horizontal and stacked bar charts.

1. **Setup**:
   - Prepare categories and corresponding values, e.g., `categories = ['A', 'B', 'C']` and `values = [10, 15, 7]`.

2. **Horizontal Bar Chart**:
   ```python
   plt.barh(categories, values, color='green')
   plt.title('Horizontal Bar Chart')
   plt.xlabel('Values')
   plt.ylabel('Categories')
   plt.show()
   ```

3. **Stacked Bar Chart**:
   - Create two datasets, e.g., `values1 = [5, 10, 6]` and `values2 = [3, 5, 4]`.
   ```python
   import numpy as np
   
   categories = ['A', 'B', 'C']
   values1 = [5, 10, 6]
   values2 = [3, 5, 4]
   indices = np.arange(len(categories))
   
   plt.bar(indices, values1, color='blue', label='Group 1')
   plt.bar(indices, values2, bottom=values1, color='orange', label='Group 2')
   plt.xticks(indices, categories)
   plt.title('Stacked Bar Chart')
   plt.xlabel('Categories')
   plt.ylabel('Values')
   plt.legend()
   plt.show()
   ```

---

#### Activity 3: Histograms
**Goal**: Visualize the distribution of a numerical dataset.

1. **Setup**:
   - Prepare a dataset, e.g., `data = [1, 2, 2, 3, 3, 3, 4, 4, 5]`.

2. **Create a Histogram**:
   ```python
   plt.hist(data, bins=5, color='purple', edgecolor='black')
   plt.title('Histogram of Data')
   plt.xlabel('Value')
   plt.ylabel('Frequency')
   plt.show()
   ```

3. **Experiment**:
   - Adjust the `bins` parameter to control the number of bars.
   - Change the color scheme.

---

#### Activity 4: Subplots
**Goal**: Create multiple plots in one figure.

1. **Setup**:
   - Import required libraries and prepare datasets.

2. **Create Subplots**:
   ```python
   fig, axs = plt.subplots(2, 2)  # 2x2 grid of subplots
   
   # Line Graph
   x = [0, 1, 2, 3, 4]
   y = [0, 1, 4, 9, 16]
   axs[0, 0].plot(x, y)
   axs[0, 0].set_title('Line Graph')
   
   # Bar Chart
   categories = ['A', 'B', 'C']
   values = [5, 7, 3]
   axs[0, 1].bar(categories, values, color='blue')
   axs[0, 1].set_title('Bar Chart')
   
   # Histogram
   data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
   axs[1, 0].hist(data, bins=5, color='green')
   axs[1, 0].set_title('Histogram')
   
   # Empty Placeholder
   axs[1, 1].axis('off')
   
   # Adjust layout
   plt.tight_layout()
   plt.show()
   ```

---

#### Activity 5: Adding Annotations
**Goal**: Highlight specific data points on a plot.

1. **Setup**:
   - Create a dataset, e.g., `x = [0, 1, 2, 3, 4]` and `y = [0, 1, 4, 9, 16]`.

2. **Add Annotations**:
   ```python
   plt.plot(x, y, marker='o')
   plt.title('Annotated Plot')
   plt.xlabel('X-axis')
   plt.ylabel('Y-axis')
   
   # Annotate the maximum point
   plt.annotate('Max Value', xy=(4, 16), xytext=(3, 12),
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=10, color='red')
   plt.show()
   ```

3. **Experiment**:
   - Try different `arrowstyle` values.
   - Annotate multiple points for more emphasis.

---

### Tips for Beginners:
- Experiment with different parameters in each activity to see how they affect the plots.
- Use `plt.savefig('filename.png')` to save your visualizations.
- Explore the official [Matplotlib documentation](https://matplotlib.org/stable/contents.html) for more options and styles.
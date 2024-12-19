The **Iris dataset** is a classic dataset widely used in data analysis and machine learning. It contains 150 samples from three species of Iris flowers (`setosa`, `versicolor`, and `virginica`), with four features for each sample:

- Sepal length
- Sepal width
- Petal length
- Petal width

The task is to create scatter plots of these features using **matplotlib**, a Python library for data visualization.

---

### Solution

Here’s how to achieve the task:

1. **Import Required Libraries**:
   - Use `pandas` to load and manipulate the dataset.
   - Use `matplotlib.pyplot` to create scatter plots.

2. **Load the Dataset**:
   - Use `sklearn.datasets` to load the Iris dataset.

3. **Visualize the Data**:
   - Create scatter plots for combinations of features, grouping by species.

### Python Code

```python
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris = load_iris()

# Create a DataFrame for easier handling
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species_name'] = df['species'].apply(lambda x: iris.target_names[x])

# Plot scatter plots
feature_pairs = [
    ('sepal length (cm)', 'sepal width (cm)'),
    ('petal length (cm)', 'petal width (cm)'),
    ('sepal length (cm)', 'petal length (cm)'),
    ('sepal width (cm)', 'petal width (cm)')
]

for x_feature, y_feature in feature_pairs:
    plt.figure(figsize=(8, 6))
    for species in df['species_name'].unique():
        species_data = df[df['species_name'] == species]
        plt.scatter(
            species_data[x_feature],
            species_data[y_feature],
            label=species,
            alpha=0.7
        )
    plt.title(f'{x_feature} vs {y_feature}')
    plt.xlabel(x_feature)
    plt.ylabel(y_feature)
    plt.legend(title='Species')
    plt.grid(True)
    plt.show()
```

---

### Explanation of the Code

1. **Load and Prepare Data**:
   - The Iris dataset is loaded from `sklearn.datasets`.
   - A pandas DataFrame is created to make the dataset more intuitive to work with.
   - A new column `species_name` maps numeric species labels (`0`, `1`, `2`) to their names (`setosa`, `versicolor`, `virginica`).

2. **Feature Pairs**:
   - Commonly analyzed feature pairs include:
     - Sepal length vs. Sepal width
     - Petal length vs. Petal width
     - Sepal length vs. Petal length
     - Sepal width vs. Petal width

3. **Plotting**:
   - A loop generates scatter plots for each feature pair.
   - For each species, data points are plotted with unique labels and colors for differentiation.
   - Legends and gridlines improve readability.

4. **Visualization**:
   - Scatter plots reveal patterns and separations among species based on the feature pair.
   - This visualization aids in understanding the relationships between features.

---

### Output

- **Scatter Plot Example**:
  - X-axis: `Sepal Length`
  - Y-axis: `Sepal Width`
  - Points are colored by species (e.g., red for `setosa`, blue for `versicolor`, green for `virginica`).

By comparing the scatter plots, we can observe separations and overlaps between the species, which can be useful for classification and clustering tasks.
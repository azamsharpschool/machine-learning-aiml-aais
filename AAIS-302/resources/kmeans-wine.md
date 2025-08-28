
### 🍷 Wine Dataset K-Means Assignment

[Download Dataset](https://www.kaggle.com/datasets/harrywang/wine-dataset-for-clustering)

**Objective**
Cluster wines based on their chemical properties using the K-Means algorithm.

**Steps**

1. Download the Wine Dataset for Clustering from Kaggle.
2. Load the dataset into a Pandas DataFrame and explore it using `.head()`, `.info()`, and `.describe()`.
3. Visualize the data with histograms or boxplots to understand distributions.
4. Handle any missing values if present.
5. Scale the dataset features using StandardScaler or MinMaxScaler.
6. Use the elbow method:

   * Run K-Means for values of K between 2 and 10.
   * Plot inertia values against K.
   * Choose the best K where the curve “bends.”
7. Train a K-Means model using the chosen K.
8. Add the cluster labels as a new column in your DataFrame.
9. Calculate the average values of each feature per cluster to profile them.
10. Create scatter plots of two features at a time (e.g., alcohol vs. malic acid, colored by cluster).
11. Summarize how the clusters differ and suggest how these groupings could be useful for wine producers, retailers, or researchers.


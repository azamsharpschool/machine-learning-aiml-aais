**Assignment: Exploring K-Nearest Neighbors (KNN) Algorithm**

**Objective:**
In this assignment, you'll dive into the fundamentals of the K-Nearest Neighbors (KNN) algorithm. You'll implement KNN from scratch, apply it to a real-world dataset, and evaluate its performance.

**Dataset Description:**
For this assignment, you'll use the "Iris" dataset, a popular dataset in machine learning. It contains measurements of various iris flowers, including sepal length, sepal width, petal length, and petal width. Each sample also has a corresponding target label indicating the species of iris (setosa, versicolor, or virginica).

**Use sklearn.datasets to access Iris Dataset

Once you download the dataset, you can use it for the assignment tasks mentioned earlier. If you have any further questions or need assistance, feel free to ask!

**Assignment Tasks:**

1. **Data Loading and Exploration:**
    - Load the Iris dataset into a Pandas DataFrame.
    - Display the first few rows of the dataset to understand its structure.
    - Check for any missing values in the dataset and handle them appropriately.
    - Display summary statistics of the dataset to gain insights into the feature distributions.

2. **Data Visualization:**
    - Create visualizations to explore the relationships between different features.
    - Use scatter plots to visualize the relationship between sepal length and width, as well as petal length and width, colored by species.

3. **Data Preprocessing:**
    - Split the data into features (X) and target labels (y).
    - Encode categorical target labels (species) into numerical values (e.g., 0 for setosa, 1 for versicolor, 2 for virginica).
    - Split the data into training and testing sets using an appropriate ratio (e.g., 80% training, 20% testing).

4. **K-Nearest Neighbors Implementation:**
    - Implement the KNN algorithm from scratch.
    - Define a function that takes the training data, testing data, value of k, and distance metric as inputs and returns the predicted labels for the testing data.

5. **Model Evaluation:**
    - Use your implemented KNN algorithm to make predictions on the testing data.
    - Evaluate the performance of the KNN model using appropriate evaluation metrics (e.g., accuracy, precision, recall, F1-score).
    - Compare the performance of your implemented KNN model with a built-in KNN model from scikit-learn.

6. **Conclusion:**
    - Write a brief conclusion summarizing your findings from implementing and evaluating the KNN algorithm.
    - Discuss any insights gained and potential areas for further exploration.

**Submission:**
- Write Python code to accomplish each task, ensuring clarity and correctness.
- Include comments in your code to explain the steps and any assumptions made.
- Submit your code along with any visualizations generated and the conclusions drawn from the analysis.

**Note:**
- Take your time to understand the KNN algorithm and implement it correctly.
- Ensure that your implementation is efficient and can handle large datasets.
- Test your implementation with different values of k and distance metrics to understand their effects on performance.
- If you encounter any difficulties or have questions, don't hesitate to ask for assistance.
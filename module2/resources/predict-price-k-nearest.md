
### Exercise: Predicting Customer Purchases with K-Nearest Neighbors

#### Dataset Description

You have a dataset of customers with the following features:
- `CustomerID`: A unique identifier for each customer.
- `Age`: The age of the customer.
- `AnnualIncome`: The annual income of the customer in thousands of dollars.
- `SpendingScore`: A score assigned by the marketing team based on customer behavior and spending patterns (1-100).
- `Purchase`: Whether the customer made a purchase (1) or not (0).

The dataset is provided as follows:

```plaintext
CustomerID,Age,AnnualIncome,SpendingScore,Purchase
1,19,15,39,0
2,21,15,81,0
3,20,16,6,0
4,23,16,77,0
5,31,17,40,0
6,22,17,76,0
7,35,18,6,0
8,23,18,94,1
9,64,19,3,0
10,30,19,72,0
11,67,19,14,0
12,35,19,99,1
13,58,20,15,0
14,24,20,77,0
15,37,20,13,0
16,22,20,79,0
17,35,21,35,0
18,20,21,66,0
19,52,23,29,0
20,35,23,98,1
```

#### Tasks

1. **Load the Dataset**:
   - Load the dataset into a pandas DataFrame.

2. **Explore the Dataset**:
   - Display the first few rows of the dataset.
   - Check for any missing values.
   - Print the summary statistics of the numerical features.

3. **Preprocess the Data**:
   - Separate the features (`Age`, `AnnualIncome`, `SpendingScore`) and the target variable (`Purchase`).
   - Split the data into training and testing sets (80% train, 20% test).

4. **Implement K-Nearest Neighbors**:
   - Use the `KNeighborsClassifier` from `scikit-learn` to fit the model on the training data.
   - Use the model to make predictions on the test data.

5. **Evaluate the Model**:
   - Calculate the accuracy of the model on the test data.
   - Print the confusion matrix and classification report.

6. **Experiment with Different Values of K**:
   - Try different values of `K` (e.g., 1, 3, 5, 7, 9) and observe how the accuracy changes.
   - Plot the accuracy for different values of `K`.

7. **Predict for a New Customer**:
   - Use the trained model to predict whether a new customer with `Age=40`, `AnnualIncome=25`, and `SpendingScore=50` will make a purchase.

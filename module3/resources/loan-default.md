### Exercise 3: Predicting Loan Default

Save the following data into a file named `loan_default_data_with_missing_values.csv`.

```plaintext
loan_amount,interest_rate,income,credit_score,loan_default
15000,5.5,55000,700,0
20000,6.0,62000,,0
25000,,48000,680,1
30000,4.5,75000,740,0
10000,5.0,45000,650,1
22000,6.5,53000,710,
,7.2,47000,670,1
18000,5.8,60000,730,0
24000,6.8,51000,690,1
32000,4.0,,750,0
16000,5.3,58000,710,0
28000,7.5,46000,,1
14000,5.7,57000,720,0
26000,6.7,49000,680,1
19000,5.9,59000,700,0
31000,4.2,77000,740,0
12000,,44000,650,1
23000,6.3,52000,710,0
17000,5.4,,730,0
29000,7.1,48000,690,1
```

#### Exercise: Predicting Loan Default with Missing Values

**Scenario:** You are tasked with building a model to predict whether a loan applicant will default on their loan. However, your dataset has some missing values.

#### Steps:
1. **Load and Prepare the Data:**
    - Load the data from `loan_default_data_with_missing_values.csv` into a pandas DataFrame.
    - Handle the missing values appropriately (e.g., impute missing values, drop rows/columns with missing values, etc.).
    - Separate the features (`loan_amount`, `interest_rate`, `income`, `credit_score`) and the target variable (`loan_default`).
    - Split the data into training and testing sets.
    - Standardize the features.

2. **Build the Logistic Regression Model:**
    - Define a sequential model using Keras.
    - Add a dense layer with a single neuron and a sigmoid activation function.

3. **Compile the Model:**
    - Compile the model using the Adam optimizer.
    - Use binary crossentropy as the loss function.
    - Specify accuracy as a metric.

4. **Train the Model:**
    - Train the model using the training data.
    - Use a validation split to monitor the model's performance on validation data.

5. **Evaluate the Model:**
    - Evaluate the model's performance on the test data.
    - Print the test accuracy.

6. **Make Predictions:**
    - Use the model to make predictions on the test data.
    - Convert the predicted probabilities to binary classes (0 or 1).
    - Print the predicted classes along with the actual classes for comparison.

---
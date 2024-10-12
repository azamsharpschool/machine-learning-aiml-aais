
### Exercise 2: Predicting Employee Attrition

Save the following data into a file named `employee_attrition_data_with_missing_values.csv`.

```plaintext
age,satisfaction_level,number_of_projects,average_monthly_hours,attrition
34,0.45,5,220,0
29,0.80,3,,0
41,0.30,6,250,1
,0.70,2,170,0
50,0.25,7,280,1
35,0.60,4,210,
43,0.40,5,240,1
30,0.85,3,190,0
38,,4,230,0
49,0.20,6,260,1
32,0.75,,200,0
36,0.50,4,220,0
40,0.35,5,,1
28,0.90,2,180,0
45,0.30,6,270,1
33,,4,210,0
37,0.50,5,240,0
46,0.25,7,280,1
31,0.80,3,200,0
39,0.55,4,230,0
42,0.35,6,260,1
26,0.85,2,170,0
44,0.30,5,270,1
48,,7,290,1
```

#### Exercise: Predicting Employee Attrition with Missing Values

**Scenario:** You are working as a data scientist for a company and need to predict whether an employee will leave the company based on various features. However, your dataset has some missing values.

#### Steps:
1. **Load and Prepare the Data:**
    - Load the data from `employee_attrition_data_with_missing_values.csv` into a pandas DataFrame.
    - Handle the missing values appropriately (e.g., impute missing values, drop rows/columns with missing values, etc.).
    - Separate the features (`age`, `satisfaction_level`, `number_of_projects`, `average_monthly_hours`) and the target variable (`attrition`).
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

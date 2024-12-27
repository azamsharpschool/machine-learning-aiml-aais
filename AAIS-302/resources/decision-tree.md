

### Exercise: Predicting Disease Presence with Decision Tree

#### Dataset Description

You have a dataset of patients with the following features:
- `PatientID`: A unique identifier for each patient.
- `Age`: The age of the patient.
- `BMI`: The Body Mass Index of the patient.
- `BloodPressure`: The blood pressure level of the patient.
- `Cholesterol`: The cholesterol level of the patient.
- `Disease`: Whether the patient has the disease (1) or not (0).

The dataset is provided as follows:

```plaintext
PatientID,Age,BMI,BloodPressure,Cholesterol,Disease
1,25,22.4,120,200,0
2,30,28.1,130,220,1
3,35,23.0,115,210,0
4,40,30.5,140,240,1
5,45,26.7,135,215,0
6,50,29.3,150,230,1
7,55,24.8,125,205,0
8,60,31.6,160,250,1
9,65,27.5,145,225,1
10,70,32.0,155,235,1
```

#### Tasks

1. **Load the Dataset**:
   - Load the dataset into a pandas DataFrame.

2. **Explore the Dataset**:
   - Display the first few rows of the dataset.
   - Check for any missing values.
   - Print the summary statistics of the numerical features.

3. **Preprocess the Data**:
   - Separate the features (`Age`, `BMI`, `BloodPressure`, `Cholesterol`) and the target variable (`Disease`).
   - Split the data into training and testing sets (80% train, 20% test).

4. **Implement Decision Tree**:
   - Use the `DecisionTreeClassifier` from `scikit-learn` to fit the model on the training data.
   - Use the model to make predictions on the test data.

5. **Evaluate the Model**:
   - Calculate the accuracy of the model on the test data.
   - Print the confusion matrix and classification report.

6. **Visualize the Decision Tree**:
   - Visualize the trained decision tree using `plot_tree` from `scikit-learn`.

7. **Experiment with Different Depths**:
   - Try different values of `max_depth` (e.g., 2, 3, 4, 5) and observe how the accuracy changes.
   - Plot the accuracy for different values of `max_depth`.

8. **Predict for a New Patient**:
   - Use the trained model to predict whether a new patient with `Age=50`, `BMI=27.0`, `BloodPressure=140`, and `Cholesterol=220` has the disease.

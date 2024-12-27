
### Exercise: Predicting Diabetes

**Task:** Use logistic regression to predict whether a person has diabetes based on features such as glucose level, blood pressure, BMI, and age. Evaluate the model's performance using accuracy and a confusion matrix.

1. **Import Libraries**
    - Import the necessary libraries for data manipulation, visualization, and machine learning.

2. **Load the Dataset**
    - Load the Pima Indians Diabetes Dataset. This dataset is available in several places online, including Kaggle.

```python
# Load the Pima Indians Diabetes dataset
# If you have the dataset locally, you can use pd.read_csv('path_to_dataset.csv')
# Otherwise, you can load it directly from an online source like UCI Machine Learning Repository

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
diabetes_data = pd.read_csv(url, header=None, names=column_names)


```

3. **Prepare the Data**
    - Select features and the target variable. Split the data into training and testing sets.


4. **Train the Model**
    - Train a logistic regression model on the training data.

5. **Make Predictions**
    - Use the trained model to make predictions on the test data.

6. **Evaluate the Model**
    - Evaluate the model's performance by calculating the accuracy score and plotting the confusion matrix.

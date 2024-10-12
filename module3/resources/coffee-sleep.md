
## Exercise: Logistic Regression with Deep Learning

In this exercise, you'll build a logistic regression model using deep learning to predict whether a person will sleep well based on the number of cups of coffee they drink and their fitness level. We will use Python with TensorFlow and Keras libraries to achieve this.

### Step 1: Install Necessary Libraries

Ensure you have TensorFlow and pandas installed. 

```bash
conda install tensorflow 
```

### Step 2: Load and Prepare the Data

Save the following CSV data into a file named `coffee_sleep_data.csv`.

```plaintext
cups_of_coffee,fitness,will_sleep
5,87,1
2,76,1
1,96,1
4,73,1
1,50,1
0,62,1
3,63,1
2,29,0
7,51,0
3,38,0
8,20,0
6,80,1
2,15,0
3,75,1
4,30,0
5,45,0
1,91,1
7,54,0
3,48,0
6,88,1
0,66,1
1,52,1
8,14,0
4,43,0
2,34,0
5,72,0
1,99,1
6,77,1
2,44,0
7,61,0
3,55,0
8,20,0
6,83,1
2,41,0
1,95,1
0,59,1
4,33,0
7,50,0
3,40,0
8,27,0
5,67,0
6,82,1
1,60,1
2,35,0
7,48,0
3,56,0
```

### Step 3: Load and Prepare the Data

1. Load the data from `coffee_sleep_data.csv` into a pandas DataFrame.
2. Separate the features (`cups_of_coffee` and `fitness`) and the target variable (`will_sleep`).
3. Split the data into training and testing sets.
4. Standardize the features.

### Step 4: Build the Logistic Regression Model

1. Define a sequential model using Keras.
2. Add a dense layer with a single neuron and a sigmoid activation function.

### Step 5: Compile the Model

1. Compile the model using the Adam optimizer.
2. Use binary crossentropy as the loss function.
3. Specify accuracy as a metric.

### Step 6: Train the Model

1. Train the model using the training data.
2. Use a validation split to monitor the model's performance on validation data.

### Step 7: Evaluate the Model

1. Evaluate the model's performance on the test data.
2. Print the test accuracy.

### Step 8: Make Predictions

1. Use the model to make predictions on the test data.
2. Convert the predicted probabilities to binary classes (0 or 1).
3. Print the predicted classes along with the actual classes for comparison.

---

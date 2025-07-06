
## 🧠 Exercise: Predict California Housing Prices Using Linear Regression

### 🎯 **Objective**

Train a Linear Regression model to predict housing prices using the California Housing dataset. You’ll manually apply feature scaling and train the model without using a pipeline.

---

### 📦 **Dataset**

Use the following CSV files:

* `/content/sample_data/california_housing_train.csv`
* `/content/sample_data/california_housing_test.csv`

---

### 🛠️ **Instructions**

### ✅ Part 1: Import Libraries

Import the following:

* `pandas` and `numpy`
* `StandardScaler`, `LinearRegression`, `mean_squared_error`, and `r2_score` from `sklearn`

---

### ✅ Part 2: Load and Split the Data

* Load both CSV files into DataFrames
* Separate each into:

  * Features (`X`) — all columns except `median_house_value`
  * Target (`y`) — the `median_house_value` column

---

### ✅ Part 3: Feature Scaling

* Use `StandardScaler` to scale both the training and test features

> 💡 Don’t scale the target (`y`) — only the input features (`X_train` and `X_test`)

---

### ✅ Part 4: Train a Linear Regression Model

* Use `LinearRegression()` to fit the model on the scaled training data

---

### ✅ Part 5: Make Predictions and Evaluate

* Predict on the scaled test data

* Calculate:

  * **Mean Squared Error (MSE)**
  * **Root Mean Squared Error (RMSE)**
  * **R² Score**

* Print each metric with **two decimal places**

---


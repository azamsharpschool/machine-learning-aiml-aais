
## 🚗 Exercise: Predict Car Prices Using Linear Regression

[Download Dataset](car_prices_20k.csv)


**Objective:**
Train a linear regression model to predict car prices based on numerical features from the dataset `car_prices_20k.csv`.

---

### 📁 Dataset Columns:

* `brand` (string, ignore for this exercise)
* `year` (int): Year of manufacture
* `mileage` (int): Total miles driven
* `engine_size` (float): Engine size in liters
* `price` (int): Target variable — Car price in USD

---

### ✅ Step-by-Step Instructions

1. **Load the Dataset**

   * Load `car_prices_20k.csv` using Pandas.
   * Print the first 5 rows to understand the data.

2. **Select Features and Target**

   * Define feature matrix `X` using:

     * `year`
     * `mileage`
     * `engine_size`
   * Define target vector `y` as `price`.

3. **Split the Data**

   * Split the dataset into training and testing sets (80% train, 20% test) using `train_test_split`.

4. **Train the Model**

   * Use `LinearRegression` from `sklearn.linear_model`.
   * Fit the model on the training data.

5. **Predict Prices**

   * Use the trained model to predict prices on the test data.

6. **Evaluate the Model**

   * Print the following metrics:

     * Mean Squared Error (MSE)
     * Root Mean Squared Error (RMSE)
     * R² Score

---

### 🧠 Learning Goals

* Understand how to prepare numerical data for regression.
* Learn to apply linear regression in scikit-learn.
* Interpret regression performance using common metrics.


## 🚗 Exercise: Predicting Car Prices with Machine Learning

[Download the Dataset](car_price_predictor_numerical_20k.csv)

[Example - House Price Prediction](https://colab.research.google.com/gist/azamsharp/bdef1cd77fc9edcd5abbdc5407384f55/houseprices2025.ipynb)

### 📂 Dataset:

Use the file:
**[`car_price_predictor_numerical_20k.csv`](sandbox:/mnt/data/car_price_predictor_numerical_20k.csv)**

---

### 🎯 Objective:

Build and evaluate a regression model that predicts the **price of a car** based on its numerical features:

* `year`
* `mileage`
* `engine_size`

---

### ✅ Instructions:

1. **Load the Dataset**

   * Use `pandas` to load the CSV file.
   * Display the first few rows using `.head()`.

2. **Explore the Data**

   * Check for missing values.
   * Generate basic statistics using `.describe()`.
   * Visualize distributions of features using histograms.

3. **Split the Dataset**

   * Use `train_test_split()` from `sklearn.model_selection`.
   * 80% for training, 20% for testing.

4. **Preprocess the Data**

   * Standardize the features (`year`, `mileage`, `engine_size`) using `StandardScaler`.

5. **Train a Model**

   * Use `LinearRegression` from `sklearn.linear_model`.
   * Fit the model on the training data.

6. **Evaluate the Model**

   * Make predictions on the test set.
   * Compute:

     * Mean Squared Error (MSE)
     * Root Mean Squared Error (RMSE)
     * R² Score

7. **Bonus Challenge**

   * Try using `RandomForestRegressor` and compare results with Linear Regression.
   * Which model performs better? Why?

---

### 🧠 Questions for Reflection:

* Which feature appears most important in predicting price?
* How does mileage affect the car’s value?
* What are the limitations of using only numerical features?
* How could adding categorical data (e.g., brand, fuel type) improve the model?


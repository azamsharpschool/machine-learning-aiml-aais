To perform a hands-on exercise on **Linear Regression** using the **House Prices Dataset** from Kaggle, follow the steps below. I'll also provide a small sample dataset to work with.

---

### Step-by-Step Solution

#### 1. **Setup**
   - Install necessary libraries if not already installed:
     ```bash
     pip install pandas scikit-learn matplotlib seaborn
     ```

#### 2. **Load the Dataset**
   - Download the House Prices dataset from Kaggle ([House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)).
   - Alternatively, use the small sample dataset provided below for practice.

#### 3. **Explore the Dataset**
   - Load the dataset into a Pandas DataFrame and examine its structure.

#### 4. **Preprocess the Data**
   - Handle missing values.
   - Encode categorical variables.
   - Select features for the regression model.

#### 5. **Split the Data**
   - Divide the dataset into training and testing sets.

#### 6. **Build and Train the Model**
   - Use `LinearRegression` from `sklearn.linear_model`.

#### 7. **Evaluate the Model**
   - Check the performance using metrics like Mean Squared Error (MSE) and R².

---

### Sample Code

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Sample Dataset
data = {
    "LotArea": [8450, 9600, 11250, 9550, 14260],
    "OverallQual": [7, 6, 7, 7, 8],
    "YearBuilt": [2003, 1976, 2001, 1915, 2000],
    "TotalBsmtSF": [856, 1262, 920, 756, 1145],
    "GrLivArea": [1710, 1262, 1786, 1717, 2198],
    "SalePrice": [208500, 181500, 223500, 140000, 250000]
}

# Load the dataset into a DataFrame
df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[["LotArea", "OverallQual", "YearBuilt", "TotalBsmtSF", "GrLivArea"]]
y = df["SalePrice"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2)

# Plot actual vs predicted prices
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices")
plt.grid(True)
plt.show()
```

---

### Sample Dataset

| LotArea | OverallQual | YearBuilt | TotalBsmtSF | GrLivArea | SalePrice |
|---------|-------------|-----------|-------------|-----------|-----------|
| 8450    | 7           | 2003      | 856         | 1710      | 208500    |
| 9600    | 6           | 1976      | 1262        | 1262      | 181500    |
| 11250   | 7           | 2001      | 920         | 1786      | 223500    |
| 9550    | 7           | 1915      | 756         | 1717      | 140000    |
| 14260   | 8           | 2000      | 1145        | 2198      | 250000    |

---

### Explanation

1. **Feature Selection**:
   - Features like `LotArea`, `OverallQual`, `YearBuilt`, `TotalBsmtSF`, and `GrLivArea` were used to predict the house price (`SalePrice`).

2. **Model Training**:
   - The `LinearRegression` model learns the relationship between the features and the target price.

3. **Evaluation**:
   - **MSE**: Measures the average squared difference between actual and predicted values.
   - **R²**: Indicates how well the model explains the variability in the data.

4. **Visualization**:
   - The scatter plot shows the relationship between actual and predicted house prices.

This approach can be extended to larger datasets with more features and advanced preprocessing steps.
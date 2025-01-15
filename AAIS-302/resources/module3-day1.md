### **Problem: Predicting House Prices**

[Download Dataset](home_sales_data-module3-day1.csv)

#### **Objective**
Build a predictive model to estimate house prices based on features like bedrooms, bathrooms, square footage, and location, and use visualizations to explore and present insights.

---

### **Steps to Solve the Problem**

---

#### **Step 1: Load and Explore the Data**

1. Import necessary libraries and load the dataset:
   ```python
   import pandas as pd
   import matplotlib.pyplot as plt
   import seaborn as sns
   
   url = 'https://raw.githubusercontent.com/anderfernandes/python-cookbook/main/datasets/kc_house_data.csv'
   df = pd.read_csv(url)
   print(df.head())
   ```

2. Check the dataset for missing values and basic statistics:
   ```python
   print(df.info())
   print(df.describe())
   ```

3. Visualize the distribution of house prices:
   ```python
   sns.histplot(df['price'], kde=True)
   plt.title('Distribution of House Prices')
   plt.xlabel('Price')
   plt.ylabel('Frequency')
   plt.show()
   ```

---

#### **Step 2: Feature Selection and Preprocessing**

1. Select relevant columns:
   ```python
   df = df[['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode']]
   ```

2. Visualize the relationship between square footage and price:
   ```python
   sns.scatterplot(x=df['sqft_living'], y=df['price'])
   plt.title('Price vs. Square Footage')
   plt.xlabel('Square Footage')
   plt.ylabel('Price')
   plt.show()
   ```

3. Use one-hot encoding for categorical data like `zipcode`:
   ```python
   df = pd.get_dummies(df, columns=['zipcode'], drop_first=True)
   ```

4. Scale numerical features for uniformity:
   ```python
   from sklearn.preprocessing import MinMaxScaler
   
   scaler = MinMaxScaler()
   features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors']
   df[features] = scaler.fit_transform(df[features])
   ```

---

#### **Step 3: Train-Test Split**

1. Divide the dataset into features (`X`) and target (`y`):
   ```python
   X = df.drop('price', axis=1)
   y = df['price']
   ```

2. Split the data into training and testing sets:
   ```python
   from sklearn.model_selection import train_test_split
   
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
   ```

---

#### **Step 4: Build and Train a Predictive Model**

1. Train a **Linear Regression** model:
   ```python
   from sklearn.linear_model import LinearRegression
   
   model = LinearRegression()
   model.fit(X_train, y_train)
   ```

2. Visualize feature importance (coefficients for Linear Regression):
   ```python
   feature_importance = pd.Series(model.coef_, index=X.columns).sort_values()
   feature_importance.plot(kind='barh')
   plt.title('Feature Importance')
   plt.xlabel('Coefficient Value')
   plt.ylabel('Feature')
   plt.show()
   ```

---

#### **Step 5: Evaluate the Model**

1. Make predictions on the test data:
   ```python
   y_pred = model.predict(X_test)
   ```

2. Visualize predicted vs. actual prices:
   ```python
   sns.scatterplot(x=y_test, y=y_pred)
   plt.title('Predicted vs. Actual Prices')
   plt.xlabel('Actual Prices')
   plt.ylabel('Predicted Prices')
   plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
   plt.show()
   ```

3. Calculate evaluation metrics:
   ```python
   from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
   
   mae = mean_absolute_error(y_test, y_pred)
   mse = mean_squared_error(y_test, y_pred)
   r2 = r2_score(y_test, y_pred)
   
   print(f"Mean Absolute Error: {mae}")
   print(f"Mean Squared Error: {mse}")
   print(f"R^2 Score: {r2}")
   ```

---

#### **Step 6: Visualize Model Performance**

1. Visualize residuals (errors):
   ```python
   residuals = y_test - y_pred
   sns.histplot(residuals, kde=True)
   plt.title('Residual Distribution')
   plt.xlabel('Residuals')
   plt.ylabel('Frequency')
   plt.show()
   ```

2. Plot learning curve (if applicable):
   ```python
   from sklearn.model_selection import learning_curve
   
   train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=5)
   train_mean = train_scores.mean(axis=1)
   test_mean = test_scores.mean(axis=1)
   
   plt.plot(train_sizes, train_mean, label='Training Score')
   plt.plot(train_sizes, test_mean, label='Cross-Validation Score')
   plt.title('Learning Curve')
   plt.xlabel('Training Set Size')
   plt.ylabel('Score')
   plt.legend()
   plt.show()
   ```

---

### **Outcome**
1. A trained model capable of predicting house prices.
2. Insights into important features affecting house prices.
3. Visualizations for trends, model performance, and residuals.

This approach not only solves the problem but also ensures clarity and interpretability through rich visualizations at each step.
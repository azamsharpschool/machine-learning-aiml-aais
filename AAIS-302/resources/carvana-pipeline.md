
## Carvana Linear Regression Price Predictor 

[Download Dataset](https://www.kaggle.com/datasets/ravishah1/carvana-predict-car-prices)

[Complete Source Code](https://gist.github.com/azamsharpschool/cb924281c755243ddb0205f8af532214)


## Imports

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn.pipeline import Pipeline
```

* `pandas` loads and manipulates the CSV.
* `StandardScaler` standardizes numeric values so all features are on a similar scale.
* `train_test_split` separates data into training and testing sets.
* `LinearRegression` is the ML model (finds a best-fit line).
* `mean_squared_error` and `r2_score` evaluate the model.
* `numpy` is used mainly for `sqrt()` to compute RMSE.
* `Pipeline` chains preprocessing + modeling so it happens consistently.

**Note:** `LabelEncoder` is imported but not needed if you’re using one-hot encoding (`get_dummies`). It’s safe to remove.

---

## Load the data

```python
df = pd.read_csv("/content/sample_data/carvana.csv")
df.head()
```

* Reads the CSV into a DataFrame called `df`.
* `head()` shows the first few rows so you can see column names and sample values.

---

## Clean up the `Year` column

```python
df["Year"] = df["Year"].astype(str).str[:4].astype(int)
df.head()
```

This does three things:

1. `astype(str)` — converts year values to strings
2. `str[:4]` — takes only the first 4 characters
3. `astype(int)` — converts it back to an integer

Why this is useful:

* Sometimes `Year` values are messy (like `"2018.0"` or `"2018-01-01"`)
* A regression model needs clean numbers, so this ensures that.

---

## One-hot encode the `Name` column

```python
df = pd.get_dummies(df, columns=["Name"])
```

This converts a categorical column like:

* `"Honda Civic"`
* `"Toyota Camry"`

into many binary columns like:

* `Name_Honda Civic` (0 or 1)
* `Name_Toyota Camry` (0 or 1)

Why:

* ML models like Linear Regression can’t work directly with strings.
* One-hot encoding makes categories numeric.

**Important:** This can create **a LOT of columns** if there are many unique car names.

---

## Create features (X) and target (y)

Typically, the next step in your notebook is:

* `y` = `Price` (what you want to predict)
* `X` = everything else (the inputs)

Example pattern:

```python
X = df.drop("Price", axis=1)
y = df["Price"]
```

Why:

* The model learns a relationship: `X -> y`

---

## Split into training and test sets

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

* 80% of the data becomes training data
* 20% becomes test data

Why:

* You want to evaluate the model on data it never saw during training.
* Otherwise you risk fooling yourself with “perfect” results that don’t generalize.

`random_state=42` makes the split reproducible.

---

## Build a Pipeline (StandardScaler + LinearRegression)

```python
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])
```

This is the best practice way to do preprocessing.

The pipeline guarantees:

* the scaler is fit **only** on training data
* the same scaling is applied to test data and future predictions
* you avoid data leakage by accident

---

## Train the model

```python
pipeline.fit(X_train, y_train)
```

This triggers two things:

1. The scaler computes mean/std from `X_train` and transforms it
2. Linear regression fits a model to the scaled features

---

## Make predictions

```python
y_pred = pipeline.predict(X_test)
```

The pipeline automatically:

* scales `X_test` using the training set’s mean/std
* feeds that into the trained regression model
* produces predicted prices

---

## Evaluate performance

```python
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
```

### RMSE

* “How far off are we, on average, in dollars?”
* If RMSE is 5000, your predictions are off by about **$5,000** on average.

### R²

* “How much of price variation does the model explain?”
* 0.0 = no better than predicting the average price
* 1.0 = perfect predictions

---

## Print results

```python
print("RMSE:", rmse)
print("R²:", r2)
```

This gives you a quick summary of how your model performed.

---


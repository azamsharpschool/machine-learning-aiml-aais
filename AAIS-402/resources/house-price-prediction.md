# House Price Prediction Walkthrough 

[Download DataSet](realistic_house_prices.csv)

## 0. Imports – bringing in the tools

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
```

* `pandas as pd`
  Used to load and manipulate tabular data in a DataFrame (like an Excel sheet in Python).

* `train_test_split`
  Splits your data into training and test sets so you can train on one part and evaluate on unseen data.

* `ColumnTransformer`
  Lets you apply *different preprocessing steps to different columns* (e.g., scale numeric columns, one-hot encode categorical ones) in a single object.

* `StandardScaler`
  Standardizes numeric features:
  [
  z = \frac{x - \mu}{\sigma}
  ]
  (subtract mean, divide by standard deviation). This helps many models work better.

* `OneHotEncoder`
  Converts categorical columns (like `"Downtown"`, `"Suburban"`) into numeric indicator columns (0/1).

* `Pipeline`
  Chains preprocessing and model into one combined object so you can `.fit()` and `.predict()` without manually transforming data.

* `LinearRegression`
  A regression model that fits a straight line (or hyperplane) to predict a continuous target (house price).

* `r2_score`
  Computes the R² metric, which measures how well your model explains the variance in the target.

---

## 1. Load the dataset

```python
df = pd.read_csv("/content/sample_data/House Price Prediction Dataset.csv")
```

* Reads a CSV file into a Pandas DataFrame `df`.
* After this line, `df` has columns like:

  * `Id`, `Area`, `Bedrooms`, `Bathrooms`, `Floors`, `YearBuilt`, `Location`, `Condition`, `Garage`, `Price` (based on your previous context).

---

## 2. Drop the `Id` column if it exists

```python
df = df.drop(columns=["Id"], errors="ignore")
```

* `Id` is just a row identifier; it has no predictive value.
* We drop it so it doesn’t confuse the model.
* `errors="ignore"` means:

  * If the `Id` column doesn’t exist, don’t crash; just do nothing.

This keeps the code robust if the CSV changes.

---

## 3. Create an `Age` feature and remove `YearBuilt`

```python
CURRENT_YEAR = 2025
df["Age"] = CURRENT_YEAR - df["YearBuilt"]
df = df.drop(columns=["YearBuilt"])
```

### Why this is smart:

* `YearBuilt` is a point in time (e.g., 1970), which is not directly meaningful to the model.
* What you really care about is **how old the house is now**.

So:

* For a house built in 2000: `Age = 2025 - 2000 = 25`
* For one built in 1980: `Age = 45`

Now the model sees something like:

> Older house → maybe lower price (or different pattern).

Then you drop `YearBuilt` because `Age` fully replaces it and avoids redundancy.

---

## 4. Separate features and target

```python
X = df.drop(columns=["Price"])
y = df["Price"]
```

* `Price` is what you want to predict → this is your **target** (`y`).
* Everything else is input data → these are your **features** (`X`).

So:

* `X` contains:

  * `Area`, `Bedrooms`, `Bathrooms`, `Floors`, `Location`, `Condition`, `Garage`, `Age`
* `y` contains:

  * House prices (numbers like 150,000; 300,000; 600,000; etc.)

---

## 5. Train–test split

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

This does three important things:

1. **Splits the data** into:

   * `X_train`, `y_train` → 80% of rows (by default) for training.
   * `X_test`, `y_test` → 20% of rows for evaluation.

2. Ensures **no data leakage**:

   * The model will only learn from `X_train`, `y_train`.
   * `X_test`, `y_test` simulate “future” unseen data.

3. `random_state=42` makes the split reproducible:

   * Same random split every time you run your notebook.

Why do this *before* scaling/encoding?
Because any preprocessing that **learns from the data** (means, std, category mapping) must only see **training data**, not test data.

---

## 6. Define which columns get which preprocessing

```python
numeric_cols = ["Area", "Age"]
categorical_cols = ["Location", "Condition", "Garage"]
# Everything else (Bedrooms, Bathrooms, Floors) will pass through
```

Here you’re telling scikit-learn:

* These columns are **numeric** and should be **scaled**:

  * `Area`
  * `Age`

* These columns are **categorical** and should be **one-hot encoded**:

  * `Location`
  * `Condition`
  * `Garage`

* Other columns like:

  * `Bedrooms`, `Bathrooms`, `Floors`
    are present in `X`, but not listed here, so they will be handled by the `remainder="passthrough"` later. That means they’ll just flow through untouched.

---

## 7. Build the `ColumnTransformer` (the preprocessor)

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
    ],
    remainder="passthrough"  # keeps Bedrooms, Bathrooms, Floors as-is
)
```

This is your **preprocessing plan**:

* `"num"` step:

  * Applies `StandardScaler()` to `numeric_cols` (`Area`, `Age`).
  * That standardizes them: mean 0, std 1 (based on training data).

* `"cat"` step:

  * Applies `OneHotEncoder()` to `categorical_cols` (`Location`, `Condition`, `Garage`).
  * Each unique category becomes its own column, e.g.:

    * `Location_Downtown`, `Location_Suburban`, …
    * `Condition_Excellent`, `Condition_Good`, `Condition_Fair`, …
    * `Garage_Yes`, `Garage_No`
  * `handle_unknown="ignore"` means:

    * If a new unseen category appears in test data, it won’t crash; it will just ignore that new category.

* `remainder="passthrough"`:

  * Any columns not mentioned in `numeric_cols` or `categorical_cols` (i.e., `Bedrooms`, `Bathrooms`, `Floors`) are passed through untouched.
  * So your final feature matrix includes:

    * standardized `Area`, `Age`
    * one-hot encoded `Location`, `Condition`, `Garage`
    * raw `Bedrooms`, `Bathrooms`, `Floors`

This object **knows how to turn raw X into model-ready numeric arrays**.

---

## 8. Build the full pipeline (preprocessing + model)

```python
model = Pipeline(steps=[
    ("preprocess", preprocessor),
    ("regressor", LinearRegression())
])
```

The pipeline chains two stages:

1. `"preprocess"`
   Uses the `preprocessor` you just defined:

   * Fit:

     * Learn scaling parameters (mean/std).
     * Learn one-hot categories.
   * Transform:

     * Apply scaling and encoding.

2. `"regressor"`
   A `LinearRegression()` model trained on the preprocessed features.

When you call:

```python
model.fit(X_train, y_train)
```

the pipeline does:

1. `preprocessor.fit(X_train)`
2. `preprocessor.transform(X_train)`
3. `LinearRegression.fit(preprocessed_X_train, y_train)`

All in one call 🎉

When you later call:

```python
model.predict(X_test)
```

it auto-applies the same preprocessor to `X_test` and then feeds it to the trained regressor.

You don’t manually handle scaling or one-hot encoding anymore.

---

## 9. Fit the model

```python
model.fit(X_train, y_train)
```

* Fits the entire pipeline on the **training data only**.
* Internally:

  * `StandardScaler` learns mean & std of `Area` and `Age` from `X_train`.
  * `OneHotEncoder` learns all categories present in `Location`, `Condition`, `Garage` in `X_train`.
  * Transforms `X_train` into a numeric matrix.
  * `LinearRegression` learns weights for each feature to best fit `y_train`.

No test data is touched here.

---

## 10. Make predictions on the test set

```python
y_pred = model.predict(X_test)
```

Now the pipeline:

1. Applies the stored preprocessing to `X_test`:

   * Uses the *training* means/stds for scaling.
   * Uses the *training* category mapping for one-hot encoding.
2. Passes the transformed `X_test` to the trained linear regression model.
3. Returns a NumPy array `y_pred` with predicted house prices.

---

## 11. Evaluate with R²

```python
r2 = r2_score(y_test, y_pred)

print("R² on test:", r2)
print("First 5 actual:   ", y_test.iloc[:5].values)
print("First 5 predicted:", y_pred[:5])
```

* `r2_score(y_test, y_pred)` computes **R²**, defined as:

[
R^2 = 1 - \frac{SS_{\text{residual}}}{SS_{\text{total}}}
]

* **R² interpretation**:

  * `1.0` → perfect predictions
  * `0.0` → model is no better than predicting the mean of `y_train`
  * negative → model is worse than the mean baseline

* The prints help you:

  * See how good the numeric score is.
  * Visually compare the first 5 **actual vs predicted** prices.

---

## Big picture: what this script accomplishes

From top to bottom, your code:

1. Loads and cleans the dataset.
2. Engineers a better feature (`Age`) from `YearBuilt`.
3. Splits data into train and test to simulate real-world predictive performance.
4. Sets up **column-wise preprocessing**:

   * Scales continuous numeric features.
   * One-hot encodes categorical features.
   * Keeps some features as raw integers.
5. Builds a **single unified pipeline**:

   * Preprocessing + Linear Regression model.
6. Trains the model correctly (no data leakage).
7. Evaluates performance with a standard metric (R²).

This is *exactly* the kind of structure used in real-world ML projects and is something you could drop into a notebook for a class or a portfolio project.

---


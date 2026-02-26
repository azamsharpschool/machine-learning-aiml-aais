
# 📘 Carvana Price Prediction – Full Walkthrough (Without Pipeline)

In this notebook, we build a simple **car price prediction model** using Linear Regression. The goal is to understand the full machine learning workflow step by step without using Pipelines so that we can clearly see what is happening behind the scenes.

We are intentionally doing everything manually to understand:

* Data preprocessing
* One-hot encoding
* Train/test splitting
* Feature scaling
* Model training
* Model evaluation

This is foundational knowledge for any ML engineer.

---

# 1️⃣ Importing Libraries

We begin by importing required libraries:

* `pandas` → for data manipulation
* `numpy` → for numerical operations
* `sklearn` modules → for model building and evaluation

This sets up our environment for working with structured data and machine learning tools.

---

# 2️⃣ Loading the Dataset

We load the dataset into a Pandas DataFrame.

At this stage, students should:

* Inspect `.head()`
* Check `.info()`
* Check for missing values
* Understand column meanings

Typical columns:

* `Name` → car brand/model
* `Miles` → number of miles driven
* `Year` → manufacturing year
* `Price` → target variable (what we want to predict)

Important concept:

👉 Always understand your dataset before modeling.

---

# 3️⃣ Feature Selection

We separate features (X) from target (y):

```python
X = df.drop("Price", axis=1)
y = df["Price"]
```

Why?

Machine learning models need:

* Input features (X)
* Target variable (y)

We are building a **supervised learning model**, so we must clearly separate inputs from outputs.

---

# 4️⃣ Train/Test Split

We split the dataset:

```python
train_test_split(...)
```

This is critical.

Why?

We want to simulate real-world behavior:

* The model learns from training data
* The model is evaluated on unseen test data

If we trained and tested on the same data, we would get unrealistic results.

Think of this like studying for an exam:

Training set → practice problems
Test set → final exam

---

# 5️⃣ One-Hot Encoding (Categorical Variable Handling)

The `Name` column is categorical. Machine learning models cannot understand text labels directly.

So we convert it using:

```python
pd.get_dummies(...)
```

What this does:

If we have:

| Name   |
| ------ |
| Toyota |
| Honda  |
| Ford   |

It becomes:

| Name_Toyota | Name_Honda | Name_Ford |
| ----------- | ---------- | --------- |
| 1           | 0          | 0         |

This is called **One-Hot Encoding**.

Important idea:

Each category becomes its own binary feature.

---

# 6️⃣ Aligning Train and Test Columns

After encoding:

* Training and test datasets must have identical columns
* Same order
* Same number of features

We ensure consistency using column alignment.

This step prevents:

* Shape mismatch errors
* Incorrect model behavior

This is extremely important in real-world ML systems.

---

# 7️⃣ Feature Scaling with StandardScaler

We now scale numeric features:

* `Miles`
* `Year`

Why scaling?

Because features are on different scales:

* Miles might be 80,000
* Year might be 2018

Without scaling:

* Larger numbers dominate the model
* Optimization becomes unstable

StandardScaler applies:

[
z = \frac{x - mean}{std}
]

Where:

* mean and std are calculated from training data only

Very important:

We use:

```python
scaler.fit_transform(X_train)
scaler.transform(X_test)
```

We DO NOT fit on test data.

Why?

Because that would cause data leakage.

Test data must remain unseen.

---

# 8️⃣ Understanding Mean and Standard Deviation

You extract:

```python
scaler.mean_
scaler.scale_
```

This is excellent teaching.

Students should understand:

* Scaling is not magic
* It simply standardizes values
* The model is working on normalized data

This is how real ML engineers think.

---

# 9️⃣ Training Linear Regression

We train:

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

Linear Regression tries to find:

[
Price = b_0 + b_1(Miles) + b_2(Year) + ...
]

The model learns the coefficients that minimize error.

This is Ordinary Least Squares optimization.

---

# 🔟 Making Predictions

After training:

```python
predictions = model.predict(X_test)
```

The model now uses learned coefficients to predict prices on unseen cars.

This is the first time the model sees test data.

---

# 1️⃣1️⃣ Model Evaluation

You evaluate using:

* RMSE (Root Mean Squared Error)
* R² score

### RMSE

Measures average prediction error in original units (dollars).

Lower RMSE = better model.

---

### R² Score

Measures how much variance is explained.

* 0 → explains nothing
* 1 → perfect prediction

In real-world ML:

* 0.7+ is often strong
* Depends on domain

---
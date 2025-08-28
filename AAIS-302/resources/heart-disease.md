
### Heart Disease Prediction Assignment (Logistic Regression)

[Download Dataset](https://www.kaggle.com/datasets/dileep070/heart-disease-prediction-using-logistic-regression) 

**Objective:**
Build a logistic regression model to predict whether a patient is at risk of heart disease within 10 years, using the Kaggle dataset by “dileep070” ([Data Science Portfolio][1]).

---

#### **Steps**

1. **Data Loading & Exploration**

   * Download the dataset and load it into a DataFrame.
   * Explore it using `.head()`, `.info()`, and `.describe()` to understand features and data types.

2. **Feature Understanding**

   * Identify and list features (e.g., age, sex, current smoker, cigarettes per day, blood pressure meds, stroke history, hypertension, diabetes, total cholesterol, systolic/diastolic BP, BMI, heart rate, glucose, etc.) and the target (`10-year CHD risk`) ([Data Science Portfolio][1]).

3. **Data Cleaning & Preprocessing**

   * Handle missing values (e.g., drop or impute).
   * Encode categorical features if needed (e.g., sex, smoker).
   * Scale numeric features using StandardScaler or MinMaxScaler—important for consistent model learning.

4. **Train‑Test Split**

   * Divide data into train and test sets (e.g., 70% train, 30% test) with a fixed `random_state` to ensure reproducibility ([GeeksforGeeks][2], [Data Science Portfolio][1]).

5. **Model Training**

   * Train a logistic regression model on the training data.

6. **Evaluation**

   * Evaluate the model using accuracy, confusion matrix, classification report (precision, recall, F1‑score) in the test set ([GeeksforGeeks][2]).

7. **Interpret Results**

   * Analyze which features have the strongest coefficients (highest positive or negative impact on predicting disease).
   * Discuss model performance: how well does it identify at‑risk patients? Discuss potential limitations (e.g., imbalance of classes, overfitting).


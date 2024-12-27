### Beginner Walkthrough for Day 4: Combining Techniques and Debugging

---

### **Real-World Example Walkthrough**

**Title:** Predicting Survival on the Titanic: Classification, Debugging, and Model Evaluation  

---

#### **Objective:**  
Integrate knowledge of classification and debugging to build, troubleshoot, and compare models using the Titanic dataset.

---

### **Activity: Titanic Survival Prediction**

---

#### **Step 1: Dataset Overview**

1. **Load the Titanic Dataset:**
   The Titanic dataset contains information about passengers, such as:
   - **Features:** Age, gender, ticket class, fare, etc.  
   - **Target Variable:** `Survived` (0 = did not survive, 1 = survived).

2. **Load the dataset using Pandas:**
   ```python
   import pandas as pd
   df = pd.read_csv('titanic.csv')
   print(df.head())
   ```

3. **Understand the Target Variable:**
   - The target variable `Survived` is **categorical** because it represents discrete categories: survival or non-survival.
   - **Choose Classification** for this problem.

---

#### **Step 2: Debugging a Classification Model**

1. **Introduce Buggy Code:**
   ```python
   from sklearn.tree import DecisionTreeClassifier
   
   data = pd.read_csv('titanic.csv')  # Missing preprocessing step
   X = data[['age', 'fare']]  # Missing feature scaling and handling NaN values
   y = data['survived']
   
   model = DecisionTreeClassifier  # Missing parentheses
   model.fit(X, y)  # Incorrect syntax, parentheses needed
   print(model.predict([[22, 7.25]]))
   ```

2. **Debugging Steps:**
   - **Step 1: Handle Missing Values:** The `age` column often contains missing values.
     ```python
     data['age'].fillna(data['age'].mean(), inplace=True)
     ```
   - **Step 2: Correct Model Initialization Syntax:**
     ```python
     model = DecisionTreeClassifier()  # Add parentheses
     ```
   - **Step 3: Preprocess Features:** Ensure data is properly scaled or normalized for better model performance.
     ```python
     from sklearn.preprocessing import StandardScaler
     scaler = StandardScaler()
     X_scaled = scaler.fit_transform(data[['age', 'fare']])
     ```
   - **Step 4: Re-run the Model:** Train and predict.
     ```python
     model.fit(X_scaled, y)
     print(model.predict([[22, 7.25]]))
     ```

3. **Key Takeaways:**
   - Debugging requires interpreting error messages.  
   - Systematic corrections can resolve multiple issues.

---

#### **Step 3: Evaluate and Compare Models**

1. **Split Data into Training and Testing Sets:**
   ```python
   from sklearn.model_selection import train_test_split
   X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
   ```

2. **Train Two Models (Decision Tree and k-NN):**
   ```python
   from sklearn.tree import DecisionTreeClassifier
   from sklearn.neighbors import KNeighborsClassifier
   from sklearn.metrics import accuracy_score
   
   # Decision Tree
   dt_model = DecisionTreeClassifier()
   dt_model.fit(X_train, y_train)
   dt_preds = dt_model.predict(X_test)
   
   # k-NN
   knn_model = KNeighborsClassifier(n_neighbors=3)
   knn_model.fit(X_train, y_train)
   knn_preds = knn_model.predict(X_test)
   ```

3. **Compare Model Performance:**
   ```python
   print("Decision Tree Accuracy:", accuracy_score(y_test, dt_preds))
   print("k-NN Accuracy:", accuracy_score(y_test, knn_preds))
   ```

4. **Discuss Metrics:**
   - **Accuracy:** Proportion of correct predictions.
   - Compare the two models based on their accuracy.

---

#### **Step 4: Capstone Project**

1. **Problem Statement:** Predict survival on the Titanic using additional features (e.g., gender, class).  

2. **Dataset Overview:**
   - Include columns like `Pclass` (ticket class), `Sex` (gender), `Age`, and `Fare`.

3. **Define the Steps:**
   - Load the dataset.
   - Preprocess data (e.g., handle missing values, encode categorical variables).
   - Split into training and testing sets.
   - Train and evaluate models (Decision Tree, Random Forest, or k-NN).
   - Compare model performance.

4. **Example Code:**
   ```python
   from sklearn.ensemble import RandomForestClassifier
   
   # Encode categorical variables
   df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
   df['Pclass'] = df['Pclass'].astype('category')
   
   # Select features
   features = ['Pclass', 'Sex', 'Age', 'Fare']
   target = 'Survived'
   
   X = df[features]
   y = df[target]
   
   # Handle missing values
   X['Age'].fillna(X['Age'].mean(), inplace=True)
   
   # Train-test split
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
   
   # Train Random Forest
   rf_model = RandomForestClassifier()
   rf_model.fit(X_train, y_train)
   preds = rf_model.predict(X_test)
   
   # Evaluate
   from sklearn.metrics import classification_report
   print(classification_report(y_test, preds))
   ```

5. **Report and Presentation:**
   - Include the dataset overview, preprocessing steps, models used, and results.
   - Highlight debugging challenges and how they were resolved.
   - Provide visualizations, such as feature importance or confusion matrix.

---

### **Key Takeaways:**
- **Classification vs. Regression:** Understand when to use each approach.  
- **Debugging Skills:** Learn to identify and resolve errors systematically.  
- **Model Comparison:** Use metrics to evaluate and select the best-performing model.  
- **Capstone Project:** Apply all learned concepts in a hands-on exercise to solidify understanding.
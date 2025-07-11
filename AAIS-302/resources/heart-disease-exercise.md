
## 📝 Exercise: Predicting Heart Disease Using Logistic Regression

[Download Dataset](Heart_Disease_Dataset.csv)

### 🧠 Background

You are a data scientist working for a health tech startup. Your goal is to develop a model that can **predict whether a patient has heart disease** based on several medical features. You have access to a dataset containing 20,000 patient records.

---

### 📦 Dataset Columns

| Column   | Description                                                            |
| -------- | ---------------------------------------------------------------------- |
| age      | Age of the patient                                                     |
| sex      | 0 = female, 1 = male                                                   |
| cp       | Chest pain type (0–3)                                                  |
| trestbps | Resting blood pressure (mm Hg)                                         |
| chol     | Serum cholesterol (mg/dl)                                              |
| fbs      | Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)                  |
| restecg  | Resting electrocardiographic results (0–2)                             |
| thalach  | Maximum heart rate achieved                                            |
| exang    | Exercise induced angina (1 = yes; 0 = no)                              |
| oldpeak  | ST depression induced by exercise                                      |
| slope    | Slope of the peak exercise ST segment (0–2)                            |
| ca       | Number of major vessels colored by fluoroscopy (0–4)                   |
| thal     | Thalassemia type (0 = normal, 1 = fixed defect, 2 = reversible defect) |
| target   | 1 = heart disease present, 0 = not present                             |

---

### 🎯 Your Tasks

#### 🔍 1. **Explore the Data**

* Check for missing values or anomalies.
* Plot the distribution of key features (`age`, `chol`, `thalach`, `oldpeak`).
* Analyze class balance in the `target` column.

#### 🧪 2. **Preprocess the Data**

* Perform any necessary feature scaling or encoding (if applicable).
* Decide whether to balance the dataset or not.

#### 🤖 3. **Build a Logistic Regression Model**

* Split the data into training and testing sets (e.g., 80/20).
* Train a logistic regression classifier using the appropriate features.

#### 📈 4. **Evaluate the Model**

* Use metrics like accuracy, precision, recall, and F1-score.
* Plot the confusion matrix.
* (Bonus) Plot the ROC curve and calculate AUC.

#### 🧩 5. **Interpret the Results**

* Which features contribute most to the prediction?
* Are there any patterns in false positives or false negatives?

---

### 🚀 Bonus Challenges

1. Try training a **decision tree** or **random forest** on the same dataset and compare results.
2. Perform **cross-validation** to improve model robustness.
3. Create a **simple dashboard** or interactive visualization showing prediction probability based on input values.


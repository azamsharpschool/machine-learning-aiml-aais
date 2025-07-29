
# 👩‍💼 Getting Started with Pandas: Data Manipulation Walkthrough – Employee Salaries

### Download the Dataset

Welcome to your hands-on walkthrough with **Pandas**, where we’ll analyze a dataset of employee salaries. You’ll load, explore, clean, and transform structured data to answer real business questions related to workforce compensation.

This exercise reflects tasks you might encounter at companies focused on HR tech, financial planning, or workforce management.

[Download CSV File](employee_salaries_100.csv)

---

## 🧩 What You’ll Learn

* Importing and loading a dataset
* Inspecting and understanding employee data
* Selecting, filtering, and transforming records
* Handling missing or inconsistent entries
* Aggregating, sorting, and exporting data
* Building new business-relevant features

---

## ✅ Prerequisites

Open Google Colab and create a new notebook. 

---

## 📥 Step 1: Import Pandas

```python
import pandas as pd
```

---

## 📁 Step 2: Load the Dataset

```python
df = pd.read_csv("employee_salaries.csv")
```

---

## 🔍 Step 3: Explore the Dataset

### ➤ View first few rows

```python
print(df.head())
```

### ➤ View structure and data types

```python
print(df.info())
```

### ➤ Get summary statistics

```python
print(df.describe())
```

### ➤ List column names

```python
print(df.columns.tolist())
```

---

## 🧠 Step 4: Data Selection & Filtering

### ➤ Select one column

```python
salaries = df["Salary"]
print(salaries)
```

### ➤ Select multiple columns

```python
subset = df[["Department", "Salary"]]
print(subset)
```

### ➤ Filter high earners (>\$80K)

```python
high_earners = df[df["Salary"] > 80000]
print(high_earners)
```

### ➤ Filter by department

```python
eng_dept = df[df["Department"] == "Engineering"]
print(eng_dept)
```

---

## 🧮 Step 5: Data Transformation

### ➤ Add computed column: salary per year of experience

```python
df["SalaryPerYear"] = df["Salary"] / df["ExperienceYears"]
print(df[["Department", "Salary", "ExperienceYears", "SalaryPerYear"]])
```

### ➤ Average salary by department

```python
avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary.reset_index())
```

---

## ⚠️ Step 6: Handle Missing Data

Let’s say `ExperienceYears` is missing for an employee.

### ➤ Check for missing values

```python
print(df.isnull().sum())
```

### ➤ Fill missing experience with mean

```python
df["ExperienceYears"].fillna(df["ExperienceYears"].mean(), inplace=True)
```

---

## 📊 Step 7: Sort and Aggregate

### ➤ Sort by salary (descending)

```python
sorted_df = df.sort_values(by="Salary", ascending=False)
print(sorted_df)
```

### ➤ Total payroll by department

```python
total_salary = df.groupby("Department")["Salary"].sum()
print(total_salary)
```

---

## 💾 Step 8: Save the Modified Dataset

```python
df.to_csv("employee_salaries_cleaned.csv", index=False)
```

---

## 💪 Challenge Exercises

1. **Create a column "SeniorityLevel"**

   * Junior: ≤3 years
   * Mid: 4–7 years
   * Senior: >7 years

2. **Find the highest paid employee and show all details.**

3. **Calculate average SalaryPerYear by department.**

---

## ✅ Solutions

```python
# 1. Seniority Level
df["SeniorityLevel"] = df["ExperienceYears"].apply(
    lambda x: "Junior" if x <= 3 else "Mid" if x <= 7 else "Senior"
)

# 2. Highest paid employee
highest_paid = df.loc[df["Salary"].idxmax()]
print("Highest Paid Employee:")
print(highest_paid)

# 3. Average salary per year by department
avg_salary_per_year = df.groupby("Department")["SalaryPerYear"].mean()
print(avg_salary_per_year)
```

---

## 🧠 Bonus Exploration Ideas

* Visualize salary distribution using a histogram
* Create a pie chart of department distribution
* Add a column for “Estimated Bonus” as 10% of salary
* Filter and export only senior-level employees to a new CSV

---

## 🎓 What You’ve Learned

With this walkthrough, you can now:

* Work with real-world structured employee data
* Clean and transform features for analysis
* Derive new insights through grouping and filtering
* Save clean datasets for downstream use

This foundational skill set is critical for **HR analytics**, **business intelligence**, and **workforce planning** roles. Try swapping in your own dataset next!


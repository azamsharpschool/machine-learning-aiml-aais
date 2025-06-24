
# 📋 Day 3 Walkthrough: **Cleaning a Customer Database for a Marketing Campaign**

---

## 🧠 Scenario: Why Clean Customer Data?

You're a data analyst preparing a list of customers for a retail company’s **email marketing campaign**. The dataset has:

* Over **20,000 records**
* Duplicate customers
* Inconsistent formats (like “John Doe” vs “ john doe ”)
* Non-numeric entries like `"five"` or `"ten"` in numeric columns
* Messy dates like `"March 12, 2023"` or `"15-01-2023"`

If left uncleaned, you might:

* Email the same person multiple times 😬
* Miscalculate customer age or purchase history 📉
* Fail to identify recent signups due to inconsistent dates 🗓️

---

## 🎯 Objective

You will:

1. Remove duplicate customer records
2. Clean and standardize:

   * Names (text casing and whitespace)
   * Numerical columns like age and purchase count
   * Signup dates for consistency

---

## 🧰 Step-by-Step Data Cleaning Process

---

## 🔍 Step 1: **Identifying and Removing Duplicates**

### 1.1 Check for Duplicates

```python
# View number of duplicates
print("Number of duplicate rows:", df.duplicated().sum())

# Display some duplicate rows
print("Example duplicates:\n", df[df.duplicated()])
```

💡 `.duplicated()` checks for **entire row matches**. If the same row appears more than once (including formatting issues), it’ll flag it.

📌 **Tip:** Use `keep=False` in `duplicated()` if you want to highlight all duplicates.

---

### 1.2 Drop Duplicates

```python
df = df.drop_duplicates()

# Recheck to confirm
print("Duplicates after removal:", df.duplicated().sum())
```

✅ Now your customer list is clean, and **no customer will receive two emails**.

---

## ✍️ Step 2: **Standardizing and Cleaning Text**

### 2.1 Clean the "Name" Field

```python
df['Name'] = df['Name'].str.strip().str.lower()
```

🧼 This removes:

* Extra spaces (before or after names)
* Case inconsistencies (`"JOHN DOE"` becomes `"john doe"`)

**Preview the result:**

```python
print(df[['Name']].drop_duplicates().head())
```

📌 **Optional:** Use `.title()` if you want names to be capitalized (e.g., `"John Doe"`)

```python
df['Name'] = df['Name'].str.strip().str.lower().str.title()
```

---

## 🔢 Step 3: **Fixing Numerical Columns**

Some values like `"five"` or `"ten"` need to be cleaned so models or reports work.

### 3.1 Clean the `Age` Column

```python
def clean_age(value):
    try:
        return int(value)
    except:
        if isinstance(value, str):
            val = value.strip().lower()
            if val == "thirty": return 30
            if val == "forty": return 40
    return None  # or np.nan

df['Age'] = df['Age'].apply(clean_age)
```

---

### 3.2 Clean the `Purchases` Column

```python
def clean_purchases(value):
    try:
        return int(value)
    except:
        if isinstance(value, str):
            val = value.strip().lower()
            if val == "five": return 5
            if val == "ten": return 10
    return None  # or np.nan

df['Purchases'] = df['Purchases'].apply(clean_purchases)
```

✅ You now have consistent **numeric data types** — ready for analysis and plotting.

---

## 🗓️ Step 4: **Standardizing Date Formats**

Different date formats can cause problems in sorting, filtering, and aggregating.

```python
df['Signup_Date'] = pd.to_datetime(df['Signup_Date'], errors='coerce')
```

* Converts formats like `"2023-01-15"`, `"March 12, 2023"`, `"15-01-2023"` to one standard format
* Any invalid date will become `NaT` (Not a Time)

**Check results:**

```python
print(df['Signup_Date'].head())
```

📌 You can also format output:

```python
df['Signup_Date'] = df['Signup_Date'].dt.strftime('%Y-%m-%d')
```

---

## ✏️ Step 5: Hands-On Cleaning Activity

Apply all of the above steps:

```python
# Step 1: Remove duplicates
df = df.drop_duplicates()

# Step 2: Clean text columns
df['Name'] = df['Name'].str.strip().str.lower().str.title()

# Step 3: Clean numeric values
df['Age'] = df['Age'].apply(clean_age)
df['Purchases'] = df['Purchases'].apply(clean_purchases)

# Step 4: Standardize date format
df['Signup_Date'] = pd.to_datetime(df['Signup_Date'], errors='coerce')
```

Then, **save your cleaned dataset**:

```python
df.to_csv("cleaned_customer_data.csv", index=False)
```

---

## 📊 Final Check: Data Types and Cleaned Output

```python
print(df.dtypes)
print(df.head())
```

✅ All columns should now be in proper format:

* `Name`: `object` (cleaned, consistent casing)
* `Age`: `int64`
* `Purchases`: `int64`
* `Signup_Date`: `datetime64[ns]`

---

## ✅ Learning Outcomes

By completing this walkthrough, you:

* Removed duplicate customer entries
* Standardized messy names for consistency
* Converted non-numeric strings to integers
* Unified date formats for accurate time-based analysis

---

## 🚀 Real-World Benefits

✅ More accurate **customer segmentation**
✅ Cleaner reports and dashboards
✅ Better targeting for marketing outreach
✅ Ready-to-use dataset for **machine learning** or **predictive modeling**


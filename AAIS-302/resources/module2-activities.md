
## 📦 **Module 2: Data Cleaning and Preparation Activities**

---

[Products Dataset](products_dirty.csv)

### 📅 **Day 1: Introduction to Data Cleaning and Loading Data**

**Learning Goal:** Learn how to load datasets, explore their structure, and identify data quality issues.

#### 🔧 Activities:

1. **Load the dataset** from a CSV file and preview the first 5 rows.
2. **Check data types** of each column. Are any of them incorrect (e.g., dates as strings)?
3. **List column names** and rename at least one for better clarity.
4. **Check for duplicate rows.** How many are there?
5. **Check for missing values** in each column.

---

### 📅 **Day 2: Handling Missing Data**

[Rental Car Dataset](rental_cars.csv)

**Learning Goal:** Learn different strategies for dealing with missing data.

#### 🔧 Activities:

1. **Load the rental car dataset** and identify columns with missing values.
2. **Drop rows** where `price` or `car_type` is missing.
3. **Fill missing numerical values** (e.g., `mileage`) with the column’s mean.
4. **Fill missing categorical values** with the most frequent value.
5. **Create a summary table** showing the number of missing values before and after cleaning.

---

### 📅 **Day 3: Removing Duplicates and Cleaning Formats**

[Use the Customer Campaign Dataset](customer_contacts_dirty.csv)

**Learning Goal:** Learn to clean up inconsistent data formats and remove duplicates.

#### 🔧 Activities:

1. **Check for and remove duplicate rows** in the dataset.
2. **Standardize formatting** of columns like `email` (e.g., all lowercase).
3. **Clean phone numbers** to have a consistent format.
4. **Convert date columns** to `datetime` format.
5. **Strip extra spaces** or symbols from `name`, `city`, or `state` fields.

---

### 📅 **Day 4: Combining and Reshaping Data**

- [customers.csv](customers1.csv)
- [orders.csv](orders1.csv) 
- [sales_region1.csv](sales_region1.csv) 
- [sales_region2.csv](sales_region2.csv) 
- [monthly_sales.csv](monthly_sales.csv) 

**Learning Goal:** Learn how to combine multiple datasets and reshape them for analysis.

#### 🔧 Activities:

1. **Create two DataFrames** (e.g., customers and orders).
2. **Merge them** using a common key (`customer_id`).
3. **Concatenate two DataFrames** vertically (e.g., data from two regions).
4. **Use `pivot_table`** to summarize sales per region and product.
5. **Reshape a dataset using `melt()`** to turn columns into rows (e.g., monthly sales).




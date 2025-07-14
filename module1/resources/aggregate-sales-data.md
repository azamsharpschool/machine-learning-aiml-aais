
## 🧾 **Assignment: Aggregating Regional Sales Data from JSON Files**

### **Objective:**

Create a Python program that processes multiple JSON files, each representing sales data from a different region. Your program will read each file, extract relevant data, compute summaries, and generate a final aggregated report.

---

### 📁 **Input File Format**

Each input file is a JSON file representing a region's sales. Here's the structure:

```json
{
  "region": "Region_Name",
  "sales": [
    {"date": "YYYY-MM-DD", "revenue": revenue_value},
    {"date": "YYYY-MM-DD", "revenue": revenue_value}
  ]
}
```

You will work with multiple files (e.g., `north_region.json`, `south_region.json`, etc.) that follow this structure.

---

### 🎯 **Expected Output File: `aggregated_sales.json`**

The final file should contain:

* `total_revenue`: The total revenue across all regions
* `average_sales_per_day`: Average revenue per unique day across all data
* `regions`: A dictionary where each key is a region name and its value includes:

  * `total_revenue` for that region
  * `sales` data (same format as input)

---

### 🧠 **What You Need to Do**

1. **Create a function** `aggregate_sales(json_files)` that:

   * Takes a list of JSON file names as input
   * Returns a dictionary with the aggregated data as described

2. **In your main block**:

   * Call this function
   * Save the result into a file named `aggregated_sales.json` using `json.dump(...)`

3. **Your program must handle**:

   * Missing files
   * Corrupted or invalid JSON
   * Unexpected data formats

---

### 🗂️ **Sample Files to Create**

#### `north_region.json`

```json
{
  "region": "North",
  "sales": [
    {"date": "2025-07-01", "revenue": 1200},
    {"date": "2025-07-02", "revenue": 1500}
  ]
}
```

#### `south_region.json`

```json
{
  "region": "South",
  "sales": [
    {"date": "2025-07-01", "revenue": 1000},
    {"date": "2025-07-02", "revenue": 1000}
  ]
}
```

#### `east_region.json`

```json
{
  "region": "East",
  "sales": [
    {"date": "2025-07-01", "revenue": 800},
    {"date": "2025-07-03", "revenue": 1045}
  ]
}
```

---

### ✅ **Bonus Challenge (Optional)**

Enhance your program to:

* Identify the **busiest sales day** across all regions
* Include this as an extra field in the final report, e.g., `"busiest_day": "2025-07-01"`

---

### 🚀 **How to Run Your Program**

1. Create the three `.json` files above in your project folder.
2. Write and save your Python script (`sales_aggregator.py` or similar).
3. Run the script:

```bash
python sales_aggregator.py
```

4. Review the output in `aggregated_sales.json`.


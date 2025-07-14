
## 🧾 **Assignment: Calculate Average Age and Grade from Student CSV File**

### **Objective**

Create a Python script that reads a CSV file containing student data and calculates:

* The **average age** of the students
* The **average grade**

You’ll write a function named `calculate_averages(csv_file)` that takes the filename as input and returns a tuple `(average_age, average_grade)`.

---

### 📄 **CSV File Format**

Each row in the CSV represents a student with the following fields:

```
Name,Age,Grade
John Doe,18,85
Jane Smith,17,90
Michael Johnson,19,75
Emily Davis,18,92
Christopher Lee,17,80
```

* The file will have a **header row**.
* All data fields are expected to be **comma-separated**.
* `Age` and `Grade` must be parsed as integers.

---

### 🧠 **Your Tasks**

1. **Create the function** `calculate_averages(csv_file)` that:

   * Reads and parses the CSV file
   * Extracts the `Age` and `Grade` from each student
   * Calculates and returns the **average age** and **average grade** as a tuple

2. Ensure your code includes:

   * Proper error handling for:

     * Missing or unreadable files
     * Rows with missing or invalid data
   * Clean file I/O using `with open(...)`

---

### 🗂️ **Sample CSV File: `students.csv`**

Create a file named `students.csv` in the same folder as your script:

```csv
Name,Age,Grade
John Doe,18,85
Jane Smith,17,90
Michael Johnson,19,75
Emily Davis,18,92
Christopher Lee,17,80
```

---

### ✅ **Bonus Challenge (Optional)**

* Print the **names of students who scored above the average grade** after calculation.

---

### 🚀 **How to Run Your Program**

1. Save your Python script (e.g., `student_averages.py`) in the same directory as the `students.csv` file.
2. Run the script using your terminal or command prompt:

```bash
python student_averages.py
```

3. You should see the average age and grade printed or returned by the function.

---

### 📌 **Assumptions**

* The CSV file will contain a header row.
* All age and grade fields are numeric and within a reasonable range.
* Commas are used as delimiters.


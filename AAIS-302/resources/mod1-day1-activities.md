### Day 1 Walkthrough: Getting Started with Python for Data Analysis

This walkthrough provides step-by-step beginner-friendly activities to familiarize learners with Python, Jupyter Notebooks, and basic data analysis using Pandas.

---

#### **Step 1: Install and Set Up Jupyter Notebooks**

1. **Install Python and Jupyter:**
   - Guide learners to download and install [Anaconda](https://www.anaconda.com/) (recommended for beginners as it includes Python, Jupyter, and Pandas).
   - Alternatively, install Python and Jupyter via pip:
     ```
     pip install notebook pandas
     ```

2. **Launch Jupyter Notebook:**
   - Open the terminal or command prompt and type:
     ```
     jupyter notebook
     ```
   - This will open the Jupyter Notebook interface in the default web browser.

3. **Explore the Jupyter Interface:**
   - Demonstrate how to create a new notebook by clicking **New > Python 3**.
   - Explain the structure: cells (code and markdown), toolbar, and running/notebook states.

4. **Activity: Write and Execute a Python Print Statement**
   - In a new cell, write:
     ```python
     print("Hello, Data Analysis!")
     ```
   - Run the cell by pressing **Shift + Enter** or clicking the "Run" button.

---

#### **Step 2: Introduction to Python Basics**

1. **Python Syntax and Variables:**
   - Explain the basics of Python syntax (indenting, comments, etc.).
   - Introduce variables and data types (strings, integers, floats, lists, etc.).

2. **Activity: Create and Manipulate a List**
   - Ask learners to create a list of five favorite fruits:
     ```python
     favorite_fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
     ```
   - Print the first and last items using indexing:
     ```python
     print("First fruit:", favorite_fruits[0])
     print("Last fruit:", favorite_fruits[-1])
     ```

---

#### **Step 3: Exploring Pandas and DataFrames**

1. **Introduce Pandas:**
   - Explain what Pandas is and its role in data analysis.
   - Describe a DataFrame as a table-like data structure.

2. **Activity: Create a Simple DataFrame**
   - Import Pandas and create a DataFrame from a dictionary:
     ```python
     import pandas as pd
     
     data = {
         "Name": ["Alice", "Bob", "Charlie"],
         "Age": [25, 30, 35],
         "City": ["New York", "Los Angeles", "Chicago"]
     }
     
     df = pd.DataFrame(data)
     print(df)
     ```

---

#### **Step 4: Load a CSV File into Pandas**

1. **Reading CSV Files:**
   - Show how to read a CSV file into a Pandas DataFrame:
     ```python
     df = pd.read_csv('iris.csv')  # Replace with the path to the sample dataset
     ```

2. **Activity: Load and Display a Dataset**
   - Provide a sample dataset (e.g., [Iris dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/)).
   - Have learners load it and display the first five rows:
     ```python
     print(df.head())
     ```

---

#### **Step 5: Basic Data Exploration**

1. **Introduce DataFrame Methods:**
   - Teach learners to use:
     - `.head()` to view the first few rows.
     - `.info()` to understand the structure.
     - `.describe()` to view summary statistics.

2. **Activity: Explore the Dataset**
   - Guide learners to apply these methods:
     ```python
     print(df.head())      # First 5 rows
     print(df.info())      # Structure and column types
     print(df.describe())  # Summary statistics
     ```

---

### Outcomes:
By the end of Day 1, learners should:
- Be comfortable navigating Jupyter Notebooks.
- Understand Python basics, including variables and data types.
- Know how to create and explore Pandas DataFrames.
- Load and perform basic exploration of a dataset.

Encourage questions and provide real-time support as learners complete each activity!
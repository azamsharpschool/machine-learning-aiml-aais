**Assignment: One-sample Hypothesis Test for Population Proportion**

**Objective:**
In this assignment, you'll perform a one-sample hypothesis test for a population proportion using a fictional dataset. You'll use the statsmodels function `proportions_ztest` to test whether the actual proportion of a certain event is different from an expected proportion.

**Dataset Description:**
You are provided with a dataset containing information about 1000 online shoppers. Each row represents a shopper, and the dataset includes a binary variable indicating whether each shopper made a purchase (1 for purchased, 0 for not purchased).

[Download DataSet](purchase.csv)

**Assignment Tasks:**

1. **Load the Dataset:**
    - Load the provided dataset into a Pandas DataFrame.

2. **Calculate the Number of Shoppers Who Made a Purchase:**
    - Define a cutoff value for the event of interest (e.g., 1 for making a purchase).
    - Count the number of shoppers who made a purchase (i.e., the number of rows with the event value greater than the cutoff).

3. **Find the Total Number of Shoppers:**
    - Determine the total number of shoppers in the dataset.

4. **Perform a Z-test:**
    - Choose a user-defined expected proportion for the null hypothesis (e.g., 0.3).
    - Use the `proportions_ztest` function from the `statsmodels` library to perform a one-sample z-test for proportions.
    - Use the number of shoppers who made a purchase and the total number of shoppers as input to the z-test function.

5. **Determine Hypothesis Rejection:**
    - Determine whether the null hypothesis should be rejected at the alpha = 0.05 significance level.
    - If the p-value is less than 0.05, reject the null hypothesis and conclude that the actual proportion is different from the expected proportion. Otherwise, fail to reject the null hypothesis.

**Submission:**
- Write Python code to accomplish each task, ensuring clarity and correctness.
- Include comments in your code to explain the steps and any assumptions made.
- Submit your code along with the results.

**Note:**
- Ensure that the provided dataset is correctly loaded and that the event of interest is properly defined.
- Make sure to handle any potential data preprocessing steps (e.g., handling missing values) before performing the hypothesis test.
- Test your code with different cutoff values and expected proportions to ensure its correctness.
- If you encounter any difficulties or have questions, feel free to ask for clarification or assistance.
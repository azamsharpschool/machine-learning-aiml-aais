
# Activity: Heart Disease Prediction with Pandas

Objective:

Introduce learners to data exploration and analysis using pandas with a heart disease dataset.
Familiarize learners with common pandas functions for data manipulation and analysis.
Instructions:

Data Loading:

Load the heart disease dataset into a pandas DataFrame using pd.read_csv().
Data Exploration:

- Use df.head() to display the first few rows of the dataset.
- Use df.shape to check the dimensions of the dataset (number of rows and columns).
- Use df.info() to check the data types and presence of missing values.
- Use df.describe() to calculate summary statistics for numerical columns.

Data Visualization:

- Use df.hist() to plot histograms for important features such as Age, RestingBloodPressure, and Cholesterol.
- Use pd.crosstab() to create bar plots to visualize the distribution of categorical features like Sex, ChestPainType, and FastingBloodSugar.

Data Analysis:

- Calculate the percentage of patients with heart disease in the dataset using df['HeartDisease'].mean().
- Explore the relationship between different features and heart disease using df.groupby() or other aggregation techniques.
- Calculate the average age of patients with and without heart disease using df.groupby().
Conclusion:

[Download the Dataset](heart-disease.csv)


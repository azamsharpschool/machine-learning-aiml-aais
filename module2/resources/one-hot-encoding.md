
Exercise: One-Hot Encoding Practice and Linear Regression

You've been provided with a dataset containing information about various car models, including their make, model, year, price, and mileage. Your task is to perform one-hot encoding on the 'make' column to transform categorical data into numerical format. Additionally, you'll use scikit-learn's linear regression to predict the price of the car based on other features.

Here's the dataset:

```
make,model,year,price,mileage
Toyota,Corolla,2018,15000,30000
Toyota,Corolla,2018,15500,28000
Toyota,Corolla,2018,16000,32000
Honda,Civic,2017,14000,25000
Honda,Civic,2017,14500,23000
Honda,Civic,2017,15000,27000
Ford,Fusion,2019,18000,20000
Ford,Fusion,2019,18500,18000
Ford,Fusion,2019,19000,22000
Chevrolet,Cruze,2016,13000,35000
Chevrolet,Cruze,2016,13500,33000
Chevrolet,Cruze,2016,14000,37000
Nissan,Altima,2018,16000,28000
Nissan,Altima,2018,16500,26000
Nissan,Altima,2018,17000,30000
Hyundai,Elantra,2017,14000,27000
Hyundai,Elantra,2017,14500,25000
Hyundai,Elantra,2017,15000,29000
Volkswagen,Jetta,2019,19000,22000
Volkswagen,Jetta,2019,19500,20000
Volkswagen,Jetta,2019,20000,24000
Subaru,Impreza,2018,17000,24000
Subaru,Impreza,2018,17500,22000
Subaru,Impreza,2018,18000,26000
Mazda,Mazda3,2017,16000,26000
Mazda,Mazda3,2017,16500,24000
Mazda,Mazda3,2017,17000,28000
Kia,Forte,2019,17000,23000
Kia,Forte,2019,17500,21000
Kia,Forte,2019,18000,25000
```

Your task is to:

1. Load the dataset into a pandas DataFrame.
2. Perform one-hot encoding on the 'make' column.
3. Use scikit-learn's linear regression to predict the price of the car based on other features.

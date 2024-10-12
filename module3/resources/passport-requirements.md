# Passport Requirements 

You have been given the following array, which contains the list of countries along with the classifications if the countries require visa or not.  

```
passports = np.array(["us", "oman", "us", "us", "oman", "us", "oman", "us"]) 

visa_required = np.array([0, 1, 0, 0, 1, 0, 1, 0]) 
```

As you can see "us" does not require visa, indicated with 0 and "oman" require visa, indicated with 1. 

Train a TensorFlow model that handle the above use case. A user can provide the country and will get back 1 or 0 indicating whether the country requires the visa or not. 



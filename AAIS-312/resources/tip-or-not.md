
# 🍔 Beginner Deep Learning Exercise

## **Will the Customer Tip \$5 or More?**

---

### 🎯 Objective

Build a simple neural network that predicts whether a customer will tip **\$5 or more** based on:

* Delivery distance
* Order total
* Weather condition

---

## 🧠 What You’ll Practice

* Loading real-world data into Python
* Encoding categorical variables (e.g., weather)
* Building a binary classifier using a neural network
* Making predictions on new data
* Visualizing how predictions change based on distance

---

## 📁 Dataset

Use this simulated delivery dataset.

Create a file called `delivery_tips.csv` and paste the following:

```csv
distance,order_total,weather,tip_above_5
0.5,15,clear,1
1.2,8,rainy,0
2.0,25,snowy,1
0.7,12,clear,0
3.0,30,clear,1
0.4,9,rainy,0
1.0,20,clear,1
2.5,18,snowy,1
3.5,14,rainy,0
0.6,10,clear,0
4.0,35,clear,1
2.8,22,rainy,1
1.5,11,snowy,0
1.8,28,clear,1
3.0,12,rainy,0
```

---

## 📋 Instructions

### ✅ Step 1: Load the Data

* Load the dataset into a pandas DataFrame
* Inspect the shape and column types

### ✅ Step 2: Prepare the Data

* Encode the `weather` column (hint: use one-hot encoding)
* Separate the features (inputs) and the target column (`tip_above_5`)

### ✅ Step 3: Build the Model

* Use Keras `Sequential` API
* Input layer should match the number of features
* Final layer should output a probability (0 to 1)

### ✅ Step 4: Train the Model

* Choose an appropriate loss function and optimizer
* Train for at least 50 epochs

### ✅ Step 5: Make a Prediction

* Predict whether a customer will tip \$5 or more if:

  * Distance = 2.0 miles
  * Order total = \$22
  * Weather = rainy

### ✅ Step 6: Visualize Distance Effect

* Keep order total and weather constant
* Vary the `distance` from 0.5 to 5 miles
* Plot the probability of tipping \$5+ versus distance

---

## 🔍 Challenge Questions

1. What happens if you remove the weather feature?
2. How sensitive is the prediction to order total vs distance?
3. Try changing the model (e.g., number of neurons). Does it improve?
4. Is the model overfitting or underfitting?

---

## 🧩 Optional Extensions

* Add a new column: `delivery_time` (minutes)
* Create a web UI with [Gradio](https://gradio.app) or [Streamlit](https://streamlit.io)
* Build a confusion matrix to analyze prediction quality

---


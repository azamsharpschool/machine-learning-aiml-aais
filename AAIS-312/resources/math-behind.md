

## 🧮 The Math Behind a Single Neuron (Made Simple)

Let’s break down what happens inside a very simple neural network — one that has just **one input** and **one neuron**. For example, we want to predict if someone will **sleep well based on how many cups of coffee they drink**.

Here’s what the model looks like in Keras:

```python
Dense(1, activation='sigmoid', input_shape=(1,))
```

This means:

* The model takes in **1 input** (cups of coffee)
* It uses **1 neuron**
* It applies the **sigmoid** function to squash the output between 0 and 1

---

### 🧠 What’s the Math Inside?

Inside the neuron, here’s what happens:

```
z = (weight × input) + bias
output = sigmoid(z)
```

Where:

* `input` = number of cups of coffee
* `weight` and `bias` = values the model learns during training
* `z` = total value before activation
* `sigmoid(z)` = squashes the result to be between 0 and 1
* `output` = final prediction (like a probability of sleeping well)

---

### ☕ Example 1: Predicting Sleep After 2 Cups of Coffee

Let’s say the model learned:

* Weight = **-1.2**
* Bias = **5**
* Input = **2 cups**

#### Step 1: Calculate the total (z):

```
z = (-1.2 × 2) + 5 = -2.4 + 5 = 2.6
```

#### Step 2: Apply sigmoid to get the output:

```
sigmoid(2.6) = 1 / (1 + e^(-2.6)) ≈ 0.931
```

✅ **Prediction: 93.1% chance of sleeping well**

---

### ☕ Example 2: Predicting Sleep After 6 Cups of Coffee

* Weight = **-1.2**
* Bias = **5**
* Input = **6 cups**

#### Step 1:

```
z = (-1.2 × 6) + 5 = -7.2 + 5 = -2.2
```

#### Step 2:

```
sigmoid(-2.2) = 1 / (1 + e^(2.2)) ≈ 0.100
```

🔻 **Prediction: 10.0% chance of sleeping well**

---

### 🔄 What Does Sigmoid Do?

The **sigmoid function** is like a squishing function — it turns any number into a value between 0 and 1. That’s why it’s perfect for outputs that represent **probabilities**.

```
sigmoid(z) = 1 / (1 + e^(-z))
```

| z-value | sigmoid output |
| ------- | -------------- |
| -5      | \~0.0067       |
| 0       | 0.5            |
| 5       | \~0.993        |

---

### ⚙️ How the Model Learns

In training, the model starts with **random weight and bias**, and then improves them step-by-step:

1. **Make a prediction**
2. **Compare** it to the actual answer (label)
3. **Calculate error** using a function like binary crossentropy
4. **Adjust weight and bias** using gradient descent

This repeats for every data point, many times, until the model gets really good.

---

### 🎯 Goal of Training

Find the **best weight and bias** so the model can predict sleep quality accurately — just from the number of cups of coffee someone drinks!


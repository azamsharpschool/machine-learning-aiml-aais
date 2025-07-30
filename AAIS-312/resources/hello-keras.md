
# 👋 Hello Keras: Learning a Simple Math Rule (y = 2x + 1)

---

## 🧠 The Goal (in Plain English)

We want to build a program that can **learn** the math pattern:

```
If I give you a number x,
You give me back y = 2 * x + 1
```

But instead of giving the equation, we only give **examples** — and let the computer **figure out the rule** by itself.

This is what machine learning does: **learn from data** instead of being programmed with rules.

---

## 🧰 Step 1: Import Libraries and Make Data

```python
import tensorflow as tf
import numpy as np
```

* `tensorflow` is the library that includes Keras — it helps build and train machine learning models.
* `numpy` helps us create and work with arrays (lists of numbers).

Now, let's create our **training data** — examples of `x` and `y`:

```python
x_train = np.array([0, 1, 2, 3, 4, 5], dtype=float)
y_train = np.array([1, 3, 5, 7, 9, 11], dtype=float)
```

These follow the rule `y = 2x + 1`, but we’re **not telling the model the formula** — we just give it the numbers and let it figure it out.

---

## 🏗️ Step 2: Build a Simple Model

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])
```

Here’s what this means:

* `Sequential`: Our model will have layers stacked in order (only 1 layer in this case).
* `Dense(units=1)`: One neuron (like a single math brain cell).
* `input_shape=[1]`: Each input is a single number (like 3, 5, 10, etc.).

Think of this like:

```
x → [Neuron] → y
```

This neuron will try to learn the correct `y` for each `x`.

---

## ⚙️ Step 3: Compile the Model

```python
model.compile(optimizer='sgd', loss='mean_squared_error')
```

* `optimizer='sgd'`: Stands for **Stochastic Gradient Descent** — it helps the model get better over time.
* `loss='mean_squared_error'`: Measures how far the model’s guess is from the correct answer. Lower is better.

---

## 📚 Step 4: Train the Model

```python
model.fit(x_train, y_train, epochs=100)
```

We train the model using the examples for **100 times** (called epochs). Each time it gets better at guessing.

Think of it like this:

> “Okay, I guessed wrong this time. Let me adjust a little and try again…”

After enough tries, it gets really close to the real rule.

---

## 🔮 Step 5: Make a Prediction

```python
print("Prediction for x = 10:", model.predict([10.0]))
```

After training, the model can now predict answers for new numbers it never saw before. For example:

```
x = 10 → ?  
```

Expected output is `21` (because 2×10 + 1 = 21), and the model should return something **very close** to that:

```
Prediction for x = 10: [[20.99873]]
```

👏 That means our model **learned the rule by itself**!

---

## 🎉 What You Just Built

* A simple **neural network with 1 neuron**
* It learned the pattern `y = 2x + 1` **just from examples**
* It can now **predict new values** like a tiny calculator

---

## 🧪 Want to See the Equation It Learned?

```python
weights = model.layers[0].get_weights()
print("Weight:", weights[0])
print("Bias:", weights[1])
```

Example output:

```
Weight: [[2.0001]]
Bias: [0.9997]
```

That’s pretty much the same as:

```
y = 2x + 1
```

🤯 The model *discovered the formula* by learning from data!


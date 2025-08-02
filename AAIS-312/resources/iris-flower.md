
# 🌸 **Iris Flower Classifier: Learn Deep Learning the Easy Way**

In this project, we’ll use **a neural network** to **predict the species of an iris flower** based on some of its measurements.

Think of it like teaching a computer to recognize flowers based on how they look — like their **petal length**, **sepal width**, etc.

We'll use:

* A famous dataset (the Iris dataset)
* A simple neural network
* TensorFlow and Keras to build and train the model

---

## ✅ Step 1: Get Set Up

Before we begin coding, let’s make sure everything is ready.

### 🔧 1.1 Install TensorFlow

If you're using a computer, open a terminal or command prompt and type:

```bash
pip install tensorflow
```

> This installs TensorFlow — the brain of our model.

### 📚 1.2 Import the Tools

Python needs a few libraries (like tools in a toolbox). Add this to the top of your code:

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import matplotlib.pyplot as plt
```

---

## 🌱 Step 2: Load and Explore the Flower Data

### 🌸 2.1 What is the Iris Dataset?

The **Iris dataset** is a collection of **150 flower samples**. For each flower, we know:

* **Sepal Length** (how long the outer leaf is)
* **Sepal Width**
* **Petal Length** (how long the inside flower is)
* **Petal Width**
* **Species** (what kind of flower it is):

  * Setosa
  * Versicolor
  * Virginica

Let’s load it into our program:

```python
iris = load_iris()
data = iris.data             # flower measurements
target = iris.target         # species (0 = Setosa, 1 = Versicolor, 2 = Virginica)
feature_names = iris.feature_names
target_names = iris.target_names
```

---

### 🎨 2.2 Visualize the Flowers with a Scatter Plot

We’ll now **plot the flowers** using two measurements:

* Petal Length (x-axis)
* Petal Width (y-axis)

```python
colors = ['red', 'green', 'blue']
labels = ['Setosa', 'Versicolor', 'Virginica']

plt.figure(figsize=(8, 6))
for i in range(3):
    plt.scatter(data[target == i, 2], data[target == i, 3],
                color=colors[i], label=labels[i], alpha=0.7, edgecolors='black')

plt.title("Iris Flowers: Petal Length vs Petal Width")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.legend()
plt.grid(True)
plt.show()
```

✅ **Explanation**:

* Every dot is a flower.
* Colors show different species.
* You can see that **Setosa (red)** is very different, but **Versicolor and Virginica** are more similar.

---

### 🧠 2.3 Teach the Computer to Understand Labels

Computers don’t understand words like “Setosa” — so we convert the species into **one-hot encoding**:

```python
encoder = OneHotEncoder(sparse=False)
target = encoder.fit_transform(target.reshape(-1, 1))
```

Now the labels look like:

* Setosa → \[1, 0, 0]
* Versicolor → \[0, 1, 0]
* Virginica → \[0, 0, 1]

---

### 🔀 2.4 Split the Data

Let’s divide the data into:

* **Training data (80%)** → the model learns from this
* **Testing data (20%)** → we use this to see if the model is smart

```python
from sklearn.model_selection import train_test_split

train_data, test_data, train_labels, test_labels = train_test_split(
    data, target, test_size=0.2, random_state=42
)
```

---

## 🧠 Step 3: Build the Brain (Neural Network)

Now, we build a model that mimics the brain — a **neural network**.

```python
model = Sequential([
    Dense(10, activation='relu', input_shape=(4,)),
    Dense(10, activation='relu'),
    Dense(3, activation='softmax')
])
```

🔍 **Explanation**:

* `Dense` means a fully connected layer (every input connects to every neuron).
* First layer: takes in 4 inputs (the measurements) → 10 neurons → ReLU activation
* Second layer: 10 more neurons → ReLU
* Output layer: 3 neurons (one for each flower type) → softmax gives probabilities

---

### ⚙️ Compile the Model

We tell TensorFlow how to train the model:

```python
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
```

💡 Think of:

* **optimizer** = how the brain improves itself (Adam is fast)
* **loss** = how wrong it is
* **metrics** = how we measure success (accuracy)

---

## 🎓 Step 4: Train the Model (Let it Learn!)

Now we let the model train (learn from training data):

```python
history = model.fit(
    train_data, train_labels,
    epochs=50,
    validation_split=0.2
)
```

👀 **What’s happening here?**

* It looks at each flower and guesses.
* If it’s wrong, it adjusts.
* It does this 50 times (epochs).
* It also tests itself using part of the training data (validation).

---

## 🧪 Step 5: Test the Model

Once training is done, we test how well it performs on unseen data.

```python
test_loss, test_accuracy = model.evaluate(test_data, test_labels)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
```

🎉 A good model should get close to **95–100% accuracy**!

---

## 📊 Step 6: Plot Training Results

Let’s plot how well the model did over time (accuracy and loss):

```python
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(len(acc))

# Accuracy plot
plt.plot(epochs, acc, 'r', label='Training Accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation Accuracy')
plt.title('Training vs Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Loss plot
plt.plot(epochs, loss, 'r', label='Training Loss')
plt.plot(epochs, val_loss, 'b', label='Validation Loss')
plt.title('Training vs Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
```

📈 **You should see**:

* Accuracy going up
* Loss going down

---

## 🛠 Step 7: Try Improvements

Want to make your model smarter? Try:

* Adding more neurons or layers
* Changing the activation function (`tanh`, `leaky_relu`)
* Training for more epochs
* Using different optimizers

---

## ✅ Final Thoughts

You just built a flower-recognizing AI!

### 🧠 You Learned:

* How to load and explore data
* How to build a neural network
* How to visualize and evaluate results

This is **your first step into machine learning and AI**.

Would you like to:

* Make predictions with this model?
* Deploy it to a web app?
* Build a flower quiz game?


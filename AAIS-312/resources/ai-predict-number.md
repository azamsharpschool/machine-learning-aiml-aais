Here's a **very basic coding example** that demonstrates how an optimizer and loss function work in a simple AI model.

---

### **Example: AI Trying to Predict a Number**
Let’s say we want an AI to guess the number **10** based on some training.

#### **Step 1: Import Libraries**
```python
import tensorflow as tf
import numpy as np
```

#### **Step 2: Create Some Training Data**
The AI will try to learn the pattern:  
If **x = 2, then y = 4**,  
If **x = 3, then y = 6**,  
The pattern is **y = x × 2**.

```python
# Input (x) and Output (y) data
x_train = np.array([2, 3, 4, 5, 6], dtype=float)
y_train = np.array([4, 6, 8, 10, 12], dtype=float)
```

#### **Step 3: Build a Simple AI Model**
```python
# Create a simple model with one neuron
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])  # One neuron, one input
])
```

#### **Step 4: Compile the Model (Set Optimizer & Loss)**
```python
model.compile(optimizer='sgd', loss='mean_squared_error')
```
- **Optimizer:** `'sgd'` (Stochastic Gradient Descent) - Helps AI improve.  
- **Loss:** `'mean_squared_error'` - Measures how wrong AI is.

#### **Step 5: Train the Model**
```python
model.fit(x_train, y_train, epochs=500)
```
- The AI will **learn** from mistakes (loss) and **adjust** using the optimizer.  
- It repeats for **500 times (epochs)** to improve accuracy.

#### **Step 6: Test the Model**
```python
print("Predicting for x=10:", model.predict([10]))
```
- The AI **should** predict `20` (because `y = x × 2`).

---


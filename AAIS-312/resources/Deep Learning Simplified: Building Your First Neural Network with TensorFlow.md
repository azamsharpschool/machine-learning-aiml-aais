This walkthrough provides an **introductory guide** to deep learning by training a simple **neural network** using TensorFlow and Keras. The goal is to understand how a model can **learn to map inputs to outputs** using a basic mathematical relationship.

---

### **Overview**
The walkthrough trains a neural network to learn the **multiplication by 2** relationship:

- **Input**: `X = [1, 2, 3, 4, 5]`
- **Output**: `Y = [2, 4, 6, 8, 10]`

The trained model should be able to predict values for unseen inputs, like:
- `model.predict([6])` → **~12**
- `model.predict([10])` → **~20**

---

### **Step-by-Step Breakdown**
#### **Step 1: Install TensorFlow**
To install TensorFlow, run:
```sh
pip install tensorflow
```

#### **Step 2: Import Required Libraries**
The necessary TensorFlow and NumPy libraries are imported:
```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
```

#### **Step 3: Prepare the Dataset**
A simple dataset is created where:
- **X** represents the input numbers.
- **Y** represents the expected outputs (twice the input values).
```python
X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([2, 4, 6, 8, 10], dtype=float)
```

#### **Step 4: Build the Neural Network**
A simple neural network is defined using the **Sequential API**:
```python
model = Sequential([
    Dense(1, input_shape=[1])  # Single neuron with 1 input and 1 output
])
```
- **Single-layer model**: One **Dense** layer with **one neuron**.
- **Input shape `[1]`**: Expects a **single number** as input.

#### **Step 5: Compile the Model**
The model needs to be compiled with:
- **Optimizer**: `'sgd'` (Stochastic Gradient Descent)
- **Loss Function**: `'mean_squared_error'` (measures prediction errors)
```python
model.compile(optimizer='sgd', loss='mean_squared_error')
```

#### **Step 6: Train the Model**
Train the model using the input-output pairs for **500 epochs**:
```python
model.fit(X, Y, epochs=500)
```
- **Epochs**: The model updates its weights 500 times to minimize error.
- The model learns the **multiplication by 2** pattern over time.

#### **Step 7: Test the Model**
After training, we **test** the model with unseen inputs:
```python
print(model.predict([6]))  # Expected output: ~12
print(model.predict([10])) # Expected output: ~20
```

---

### **Full Code**
```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Step 1: Prepare Data
X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([2, 4, 6, 8, 10], dtype=float)

# Step 2: Define the Model
model = Sequential([
    Dense(1, input_shape=[1])  # 1 input neuron, 1 output neuron
])

# Step 3: Compile the Model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Step 4: Train the Model
model.fit(X, Y, epochs=500)

# Step 5: Test the Model
print(model.predict([6]))  # Predicts 12
print(model.predict([10])) # Predicts 20
```

---

### **Explanation**
1. **Data Representation**:  
   The input-output pairs follow a simple linear function:  
   \[
   Y = 2X
   \]
   
2. **Model Architecture**:
   - A **single neuron** takes the input `X` and applies a linear transformation to approximate `Y`.

3. **Training Process**:
   - The **weights** of the neuron are adjusted over 500 epochs.
   - The **loss function (MSE)** measures how well the model’s predictions match the actual values.
   - The **SGD optimizer** updates the weights gradually to minimize loss.

4. **Prediction**:
   - After training, the model generalizes the learned pattern and correctly predicts outputs for new inputs.

---

### **Expected Output**
After training, running predictions should yield:
```
[[12.]]
[[20.]]
```
This confirms the model has **successfully learned** the function `y = 2x`.

---

### **Next Steps**
This is a basic example of how a neural network **learns simple patterns**. You can extend this by:
- Using **more complex datasets** (e.g., non-linear relationships).
- Adding **more neurons** or **layers**.
- Experimenting with **different optimizers and activation functions**.

Would you like to see a more advanced walkthrough? 🚀
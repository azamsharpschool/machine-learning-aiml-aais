
1. What PyTorch is
2. How to use **tensors** (basic building block)
3. How to build a **simple neural network**
4. How to **train it** on dummy data

---

# 🔰 Beginner Walkthrough: PyTorch Basics

## 1. Install PyTorch

First, install PyTorch (if not already installed):

```bash
pip install torch torchvision
```

---

## 2. Import PyTorch

```python
import torch
import torch.nn as nn
import torch.optim as optim
```

---

## 3. Create Tensors

Tensors are just like NumPy arrays, but optimized for deep learning.

```python
# Create a tensor (like a list of numbers)
x = torch.tensor([1.0, 2.0, 3.0])

print("Tensor:", x)
print("Shape:", x.shape)
```

---

## 4. Simple Dummy Dataset

Let’s say we want to **predict y = 2x** (a very simple linear function).

```python
# Training data
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])  # input
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])  # output
```

---

## 5. Define a Simple Model

We’ll make a **linear regression model**: y = wx + b

```python
# Define model
model = nn.Linear(in_features=1, out_features=1)
```

---

## 6. Define Loss and Optimizer

We need:

* Loss function (how wrong we are)
* Optimizer (how to update weights)

```python
criterion = nn.MSELoss()            # Mean Squared Error
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Stochastic Gradient Descent
```

---

## 7. Train the Model

We loop many times, each time improving the model.

```python
# Training loop
for epoch in range(100):
    # Forward pass: prediction
    y_pred = model(X)
    
    # Compute loss
    loss = criterion(y_pred, y)
    
    # Backward pass: compute gradients
    optimizer.zero_grad()
    loss.backward()
    
    # Update weights
    optimizer.step()
    
    if (epoch+1) % 10 == 0:
        print(f"Epoch {epoch+1}: Loss = {loss.item():.4f}")
```

---

## 8. Test the Model

```python
# Test prediction
test_input = torch.tensor([[5.0]])
predicted = model(test_input).item()

print("Prediction for x=5:", predicted)
```

Expected output: close to **10** (since y = 2x). ✅

---

# 🎯 What You Learned

* **Tensors** (basic data structure in PyTorch)
* How to build a **linear model** (`nn.Linear`)
* How to use **loss functions** and **optimizers**
* How to run a **training loop**

---

Would you like me to make a **visual diagram** showing how data → model → loss → optimizer → updated model (the PyTorch workflow)? That would make this even clearer for beginners.

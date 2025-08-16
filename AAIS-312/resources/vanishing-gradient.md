
# 🧠 Vanishing Gradient Demo — Step-by-Step in Keras

This short example shows how **gradients shrink** in deep networks with sigmoid activations, causing the **vanishing gradient** problem.

---

## **1. Import Libraries**

```python
import tensorflow as tf
from tensorflow.keras import layers, Sequential
```

* `tensorflow as tf` — Loads TensorFlow with a short alias.
* `layers` — Lets us create building blocks like Dense layers.
* `Sequential` — A simple “stack” of layers (one after the other).

---

## **2. Create a Small Fake Dataset**

```python
x = tf.random.normal([1, 10])   # 1 sample, 10 features
y = tf.random.normal([1, 1])    # 1 target value
```

* **`x`** → Input data (shape: 1 row × 10 columns). Random numbers are fine here since we only care about gradients.
* **`y`** → Target output for that input (just 1 value).

---

## **3. Build a Deep Network with Sigmoid Activation**

```python
model = Sequential()
for _ in range(8):  # 8 hidden layers
    model.add(layers.Dense(10, activation="sigmoid"))
model.add(layers.Dense(1))
```

* **`Sequential()`** — Start with an empty model.
* **Loop (8 times)** — Add a Dense layer with:

  * 10 neurons (units)
  * Sigmoid activation → squashes values into (0, 1), which often causes vanishing gradients in deep nets.
* **Output layer** — 1 neuron, no activation (linear output).

**Shape flow:** `(1, 10) → 10 → 10 → ... (8 times) → 10 → 1`

---

## **4. Forward Pass + Loss Calculation**

```python
with tf.GradientTape() as tape:
    y_pred = model(x)  # Forward pass
    loss = tf.reduce_mean(tf.square(y_pred - y))  # MSE loss
```

* **`GradientTape`** — Records all operations so we can calculate gradients later.
* **Forward pass** — Input `x` goes through the network, producing prediction `y_pred`.
* **Loss** — Mean Squared Error between `y_pred` and `y`.

---

## **5. Compute Gradients**

```python
grads = tape.gradient(loss, model.trainable_weights)
```

* Finds the gradient (**derivative**) of the loss **w\.r.t.** every trainable weight in the model.
* The list `model.trainable_weights` contains:

  * Kernels (weight matrices)
  * Bias vectors
  * For each layer in order.

---

## **6. Display Gradient Sizes (Norms)**

```python
for i in range(0, len(grads), 2):  # step=2 to skip biases
    grad_norm = tf.norm(grads[i]).numpy()
    print(f"Layer {i//2+1} grad norm: {grad_norm:.10f}")
```

* **Step by 2** — Each Dense layer has 2 entries: kernel, bias. We skip the biases for clarity.
* **`tf.norm`** — Measures the size/magnitude of the gradient values for that kernel.
* **Formatted print** — Shows gradient norm for each layer’s weights.

---

## **7. What You’ll See**

* **Later layers** (near the output) → Larger gradient norms.
* **Earlier layers** (near the input) → Tiny gradient norms (e.g., `0.0000000010`).
* This shrinking is the **vanishing gradient** problem — the learning signal fades as it travels backward.

---

## **8. Quick Fix to See the Difference**

Replace `"sigmoid"` with `"relu"` in step 3:

```python
for _ in range(8):
    model.add(layers.Dense(10, activation="relu"))
```

Re-run:

* Gradients will be much healthier across all layers.
* Shows why ReLU is preferred in deep networks.

---

✅ **Key takeaway:**
Vanishing gradients happen when your network is deep **and** your activations squash values too much (like sigmoid/tanh). Early layers get almost no learning signal, slowing or stopping training.


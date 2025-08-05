
## 🌸 Goal

Build a neural network using TensorFlow to classify iris flowers into 3 species using the Iris dataset.

---

### 1️⃣ **Import Required Libraries**

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
```

* `load_iris`: Loads the Iris dataset.
* `train_test_split`: Splits the data into training and testing sets.
* `StandardScaler`: Standardizes features (mean = 0, std = 1).
* `tensorflow`: Library to build and train the neural network.

---

### 2️⃣ **Load and Prepare the Dataset**

```python
iris = load_iris()
X = iris["data"]
y = iris["target"]  # Integers: 0, 1, 2
```

* `iris = load_iris()` loads a dictionary-like object containing:

  * `data`: Features (sepal length, sepal width, petal length, petal width)
  * `target`: Labels (0 = Setosa, 1 = Versicolor, 2 = Virginica)
* `X` contains the input features.
* `y` contains the target classes (as integers).

---

### 3️⃣ **Scale the Input Features**

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

* **Why scale?** Neural networks perform better when features are on a similar scale.
* `fit_transform()` computes the mean and std, then scales each feature.
* Example: If sepal length ranges from 4.3 to 7.9, it will now range around -1 to 1.

---

### 4️⃣ **Split into Training and Test Sets**

```python
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```

* `test_size=0.2`: 20% of the data will be used for testing.
* `random_state=42`: Ensures reproducible results.
* `X_train`, `y_train`: Used for training the model.
* `X_test`, `y_test`: Used to evaluate the model after training.

---

### 5️⃣ **Build the Neural Network**

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation="relu", input_shape=(4,)),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(3, activation="softmax")
])
```

* `Sequential`: A linear stack of layers.
* `Dense(64, activation="relu")`: Fully connected layer with 64 neurons and ReLU activation.

  * The first layer takes 4 inputs (one for each feature).
* `Dense(3, activation="softmax")`: Output layer with 3 neurons (for the 3 flower classes).

  * `softmax` converts the output into class probabilities.

---

### 6️⃣ **Compile the Model**

```python
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```

* `optimizer='adam'`: Adaptive optimizer that adjusts learning rates — great for most tasks.
* `loss='sparse_categorical_crossentropy'`: Used when your target labels are **integers** (not one-hot encoded).
* `metrics=['accuracy']`: Track classification accuracy during training.

---

### 7️⃣ **Train the Model**

```python
model.fit(X_train, y_train, epochs=50, validation_split=0.2)
```

* Trains the model for **50 epochs** (passes through training data 50 times).
* `validation_split=0.2`: Uses 20% of the training data to monitor how well the model is doing on unseen data (validation set).
* During training, it prints:

  * `loss` and `accuracy` on training data
  * `val_loss` and `val_accuracy` on validation data

---

## ✅ What Happens Under the Hood?

1. Data is standardized and split into train/test.
2. A neural network with 2 hidden layers learns to separate flower species based on the input features.
3. After training, the model can be used to **predict flower species** given new measurements.


# Example: Predict on a single new iris sample
sample = np.array([[5.1, 3.5, 1.4, 0.2]])  # Raw input

# Scale it
```
sample_scaled = scaler.transform(sample)
```

# Predict
```
probs = model.predict(sample_scaled)
predicted_class = np.argmax(probs)

print(f"Predicted class: {predicted_class} ({iris['target_names'][predicted_class]})")
```

``` python 

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load the dataset
iris = load_iris()
df = pd.DataFrame(data=iris["data"], columns=iris["feature_names"])
df["target"] = iris["target"]
df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

# Rename for convenience
df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "target", "species"]

# Plot petal dimensions instead of sepal
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="petal_length",
    y="petal_width",
    hue="species",
    palette="Set2",
    s=100,
    edgecolor="black"
)

plt.title("Petal Length vs Petal Width by Iris Species")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.grid(True)
plt.legend(title="Species")
plt.tight_layout()
plt.show()

```


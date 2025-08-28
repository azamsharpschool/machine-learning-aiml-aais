
# 📝 Exercise: SMS Spam Detection Using Deep Learning

Follow the steps below to build a deep learning model that classifies SMS messages as **spam** or **ham (not spam)**.

---

### Step 1: Install Required Libraries

Install TensorFlow, Pandas, NumPy, Scikit-learn, and Matplotlib.

---

### Step 2: Import Libraries

Import the required libraries for deep learning, text preprocessing, and visualization.

---

### Step 3: Load the Dataset

[Download the Dataset](ham_spam_dataset_20k.csv)

---

### Step 4: Preprocess the Data

* Convert labels (`ham`, `spam`) into numerical values.
* Split the dataset into **training** and **testing** sets (80/20).
* Tokenize and pad/truncate messages to a fixed length (e.g., 100 words).

---

### Step 5: Build the Neural Network

* Use an **Embedding layer** to learn word representations.
* Add an **LSTM layer** for sequential text understanding.
* Add a **Dense hidden layer** with ReLU activation.
* Add an **output layer** with sigmoid activation for binary classification.

---

### Step 6: Train the Model

* Train the model for a few epochs (e.g., 5).
* Use **accuracy** as the main metric.
* Plot the training and validation accuracy/loss curves.

---

### Step 7: Evaluate the Model

* Evaluate the model on the test set.
* Print the **test accuracy**.

---

### Step 8: Make Predictions

* Write a function that takes a new message as input and predicts whether it is **Spam** or **Ham**.
* Test with at least two example messages (one spam-like, one normal).

---


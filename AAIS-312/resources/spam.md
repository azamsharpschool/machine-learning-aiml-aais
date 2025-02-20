### **Detailed Explanation of Spam Detection Using RNN**

This example demonstrates how a **Recurrent Neural Network (RNN)** can be used to classify text messages as **spam** or **not spam**. Let's break down each step in detail.

---

## **Step 1: Install Required Libraries**
To implement this, we need the following Python libraries:

- **TensorFlow**: For building and training the RNN model.
- **Scikit-learn (sklearn)**: For splitting data and processing text.
- **Matplotlib**: For visualizing the training progress.

Install these using:
```bash
pip install tensorflow scikit-learn matplotlib
```

---

## **Step 2: Import Libraries**
These libraries help us handle data, preprocess text, build our model, and visualize results.

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, Embedding
import matplotlib.pyplot as plt
```

---

## **Step 3: Create a Simple Dataset**
We create a small **sample dataset** containing short text messages. Each message is labeled as either **spam (1)** or **not spam (0).**

```python
# Sample messages and labels (1 = spam, 0 = not spam)
messages = [
    "Win a free iPhone now!",  # spam
    "Congratulations! You've won a lottery.",  # spam
    "Call me when you're free.",  # not spam
    "Let's catch up tomorrow.",  # not spam
    "You have been selected for a prize!",  # spam
    "Can we meet today?",  # not spam
    "Don't miss this chance to earn rewards!",  # spam
    "What time is our meeting?",  # not spam
    "Act now to claim your free gift!",  # spam
    "Hope you are doing well.",  # not spam
]
labels = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0]  # 1 = Spam, 0 = Not Spam
```

### **Understanding the Labels**
- **Spam messages** usually contain words like "Win," "Congratulations," "Free," "Prize," and "Gift."
- **Not spam messages** are normal conversations like "Call me when you're free."

---

## **Step 4: Preprocess the Data**
### **Convert Text to Numbers**
Since computers don't understand words directly, we use `CountVectorizer` to convert each **message into numerical form**.

```python
# Convert text into numerical features
vectorizer = CountVectorizer(binary=True)
X = vectorizer.fit_transform(messages).toarray()
```
- `CountVectorizer` converts each unique word into a number and creates a word frequency matrix.
- `binary=True` ensures that we only track whether a word is present (1) or not (0), instead of counting occurrences.

### **Split the Data for Training and Testing**
To evaluate our model, we divide our dataset into:
- **80% training data** (used to train the model).
- **20% testing data** (used to check model accuracy).

```python
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)
```

---

## **Step 5: Build the RNN Model**
Now, we define a **Recurrent Neural Network (RNN)** for spam detection.

```python
# Build a simple RNN model
model = Sequential([
    Embedding(input_dim=len(vectorizer.vocabulary_), output_dim=8, input_length=X_train.shape[1]),
    SimpleRNN(16, activation='relu'),
    Dense(1, activation='sigmoid')  # Sigmoid for binary classification
])
```

### **Breaking Down the Model**
1. **Embedding Layer**: Converts the input words into dense vector representations.
2. **SimpleRNN Layer**: Processes text sequences using a Recurrent Neural Network.
3. **Dense Layer**: A fully connected layer with a **sigmoid activation function** that predicts **spam (1) or not spam (0).**

### **Compile the Model**
```python
# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```
- **Adam Optimizer**: Helps the model adjust its learning rate efficiently.
- **Binary Crossentropy Loss**: Used for binary classification problems.
- **Accuracy Metric**: Measures how well the model classifies messages.

### **View Model Summary**
```python
model.summary()
```
This prints out the architecture of the RNN.

---

## **Step 6: Train the Model**
Now, we **train the model** using the prepared dataset.

```python
# Train the model
history = model.fit(X_train, np.array(y_train), epochs=10, batch_size=2, validation_split=0.2)
```

### **Understanding Training Parameters**
- **Epochs (10)**: The number of times the model sees the entire dataset.
- **Batch Size (2)**: The number of samples processed before the model updates weights.
- **Validation Split (20%)**: Keeps part of the training data aside to check progress.

### **Visualizing Training Progress**
To see how the model improves over time, we plot **training vs. validation accuracy**.

```python
plt.figure(figsize=(8, 5))
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
```

---

## **Step 7: Evaluate the Model**
After training, we test the model on unseen data.

```python
# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test, np.array(y_test))
print(f"Test Accuracy: {accuracy:.2f}")
```
- The **loss** shows how well the model is doing.
- **Accuracy** tells us how many messages were correctly classified.

---

## **Step 8: Test with New Messages**
Now, let's check if the model correctly predicts **spam** or **not spam** for new messages.

```python
# Predict new messages
new_messages = ["Claim your free gift now!", "How are you today?"]
new_features = vectorizer.transform(new_messages).toarray()
predictions = model.predict(new_features)

# Display results
for i, message in enumerate(new_messages):
    print(f"Message: {message} -> {'Spam' if predictions[i] > 0.5 else 'Not Spam'}")
```

### **Expected Output**
```
Message: Claim your free gift now! -> Spam
Message: How are you today? -> Not Spam
```
- **"Claim your free gift now!"** is classified as **spam**.
- **"How are you today?"** is classified as **not spam**.

---

## **Key Concepts Simplified for High School Students**
1. **Spam Detection**: Used in real-world applications like email filters.
2. **RNN (Recurrent Neural Network)**: A type of AI model that processes **sequential data** like text.
3. **Training**: Teaching the model to recognize patterns in spam messages.
4. **Evaluation**: Checking how well the model performs on new, unseen messages.

---

## **Conclusion**
This example demonstrates how a **Recurrent Neural Network (RNN)** can **classify messages** as **spam** or **not spam**. By processing **text data**, training the model, and evaluating performance, we can build a functional **spam detection system**. This is a **real-world AI application** that powers **email filters**, **chat moderation**, and **SMS spam detection**.

Would you like to explore **improving accuracy** or using **real-world datasets** like the **SMS Spam Collection Dataset**? 🚀
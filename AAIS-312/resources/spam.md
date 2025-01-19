Here's a **simplified real-world example** of using an RNN for **spam detection** in emails, designed for high school students. We'll use Python and libraries like `sklearn` and `tensorflow`. This example focuses on classifying messages as "spam" or "not spam."

---

### Step 1: Install Required Libraries
Run the following command to install necessary libraries:
```bash
pip install tensorflow scikit-learn matplotlib
```

---

### Step 2: Import Libraries
```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, Embedding
import matplotlib.pyplot as plt
```

---

### Step 3: Create a Simple Dataset
For simplicity, we'll use a small manually created dataset. This can be replaced with a larger one (e.g., the SMS Spam Collection Dataset).

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
labels = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0]  # Spam = 1, Not Spam = 0
```

---

### Step 4: Preprocess the Data
Convert text messages into numerical data using `CountVectorizer`.

```python
# Convert text into numerical features
vectorizer = CountVectorizer(binary=True)
X = vectorizer.fit_transform(messages).toarray()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)
```

---

### Step 5: Build the RNN Model
```python
# Build a simple RNN model
model = Sequential([
    Embedding(input_dim=len(vectorizer.vocabulary_), output_dim=8, input_length=X_train.shape[1]),
    SimpleRNN(16, activation='relu'),
    Dense(1, activation='sigmoid')  # Sigmoid for binary classification
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Model summary
model.summary()
```

---

### Step 6: Train the Model
```python
# Train the model
history = model.fit(X_train, np.array(y_train), epochs=10, batch_size=2, validation_split=0.2)

# Plot training history
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

### Step 7: Evaluate the Model
```python
# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test, np.array(y_test))
print(f"Test Accuracy: {accuracy:.2f}")
```

---

### Step 8: Test with New Messages
```python
# Predict new messages
new_messages = ["Claim your free gift now!", "How are you today?"]
new_features = vectorizer.transform(new_messages).toarray()
predictions = model.predict(new_features)

# Display results
for i, message in enumerate(new_messages):
    print(f"Message: {message} -> {'Spam' if predictions[i] > 0.5 else 'Not Spam'}")
```

---

### Explanation for High School Students
1. **Input Data:** We use simple text messages labeled as "spam" or "not spam."
2. **Preprocessing:** Text is converted into numbers that the computer can understand using a `CountVectorizer`.
3. **RNN Model:** A simple RNN processes the text data and predicts whether a message is spam.
4. **Training:** The model learns from examples of spam and not spam messages.
5. **Testing:** We check how well the model performs on unseen messages.

---

### Output Example
```
Message: Claim your free gift now! -> Spam
Message: How are you today? -> Not Spam
```

---

### Key Concepts Simplified for High School Students
- **Spam Detection:** A real-world application of AI used in email filters.
- **RNN:** A type of AI model that processes sequences, like text.
- **Training:** Teaching the model to recognize spam messages.
- **Evaluation:** Checking how well the model works on new data.

This example keeps the concepts simple and highlights the practical use of RNNs in everyday life!
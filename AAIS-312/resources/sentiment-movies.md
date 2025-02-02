### **Step-by-Step Walkthrough: Sentiment Analysis on IMDB Reviews Using Deep Learning**

---

## **Step 1: Install Required Libraries**
Ensure you have **TensorFlow**, **NumPy**, and **Scikit-learn** installed.

```bash
pip install tensorflow numpy scikit-learn matplotlib
```

---

## **Step 2: Import Necessary Libraries**
```python
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
```

---

## **Step 3: Load the IMDB Dataset**
TensorFlow provides the **IMDB movie reviews dataset**, which consists of **50,000 reviews** labeled as **positive (1) or negative (0)**.

```python
# Load dataset with the top 10,000 most common words
imdb = keras.datasets.imdb
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=10000)

# Check first review (numerical representation)
print("First review (numerical):", X_train[0])
print("First review label (sentiment):", y_train[0])  # 0 = Negative, 1 = Positive
```

---

## **Step 4: Preprocess the Data**
Since reviews have varying lengths, we **pad** or **truncate** them to a fixed size (e.g., **256 words**) using `pad_sequences`.

```python
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Define max length
max_length = 256

# Pad sequences to make them the same length
X_train = pad_sequences(X_train, maxlen=max_length, padding="post", truncating="post")
X_test = pad_sequences(X_test, maxlen=max_length, padding="post", truncating="post")

print("Shape of training data:", X_train.shape)  # Should be (25000, 256)
```

---

## **Step 5: Build the Neural Network**
We create a **sequential model** using:
- **An embedding layer** to learn word representations
- **An LSTM layer** for sequential understanding
- **A dense layer with ReLU activation**
- **A final sigmoid output layer** for binary classification

```python
# Define the model
model = keras.Sequential([
    keras.layers.Embedding(input_dim=10000, output_dim=64, input_length=max_length),  # Word embeddings
    keras.layers.LSTM(64, return_sequences=False),  # LSTM for sequential understanding
    keras.layers.Dense(32, activation='relu'),  # Fully connected layer
    keras.layers.Dense(1, activation='sigmoid')  # Output layer (binary classification)
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Display model summary
model.summary()
```

---

## **Step 6: Train the Model**
We train the model for **5 epochs**.

```python
# Train the model
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=5, batch_size=128)
```

---

## **Step 7: Evaluate the Model**
After training, we evaluate the model to check its performance.

```python
# Evaluate the model on test data
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc:.2f}")
```

---

## **Step 8: Make Predictions**
Now, let's predict whether a given review is **positive (1) or negative (0)**.

```python
# Function to predict sentiment
def predict_sentiment(review):
    word_index = imdb.get_word_index()  # Load IMDB word index
    words = review.lower().split()  # Split review into words
    encoded_review = [word_index.get(word, 2) for word in words]  # Convert words to indices (2 = unknown word)
    padded_review = pad_sequences([encoded_review], maxlen=max_length, padding="post")  # Pad sequence
    prediction = model.predict(padded_review)[0][0]  # Get model prediction
    return "Positive" if prediction > 0.5 else "Negative"

# Example reviews
print("Review Sentiment:", predict_sentiment("This movie was fantastic! I loved it."))
print("Review Sentiment:", predict_sentiment("The film was boring and slow."))
```

---

## **Step 9: Save and Load the Model**
Save the trained model for future use.

```python
# Save the model
model.save("sentiment_analysis_model.h5")

# Load the model
loaded_model = keras.models.load_model("sentiment_analysis_model.h5")
print("Model loaded successfully!")
```

---

## **Next Steps**
- **Expand dataset** with more reviews
- **Use pre-trained word embeddings** (e.g., GloVe, Word2Vec)
- **Deploy the model** as an API using FastAPI or Flask
- **Improve accuracy** by using **bidirectional LSTMs or GRUs**

This is a **simple but powerful deep learning model** for **IMDB sentiment analysis**! 🚀 Let me know if you have any questions or need modifications.
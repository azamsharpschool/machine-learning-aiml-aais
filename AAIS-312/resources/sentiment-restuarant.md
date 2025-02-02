### **Step-by-Step Walkthrough: Sentiment Analysis Using Word Embeddings in Keras**

In this walkthrough, we will **train a simple sentiment analysis model** using **word embeddings** in **Keras**. The model will classify **short restaurant reviews** as **positive (1) or negative (0)**.

---

## **Step 1: Install Required Libraries**  
Ensure you have **TensorFlow** installed.

```bash
pip install tensorflow numpy
```

---

## **Step 2: Import Necessary Libraries**  
```python
import numpy as np
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Embedding
```

---

## **Step 3: Prepare the Dataset**  
We have a **list of restaurant reviews** and their **corresponding sentiment labels**:
- **1** = Positive review
- **0** = Negative review  

```python
# Sample reviews
reviews = ['nice food',
           'amazing restaurant',
           'too good',
           'just loved it!',
           'will go again',
           'horrible food',
           'never go there',
           'poor service',
           'poor quality',
           'needs improvement']

# Corresponding sentiment labels
sentiment = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])  # 1 = Positive, 0 = Negative
```

---

## **Step 4: Convert Text to Numerical Representation**
Neural networks require numerical inputs, so we **one-hot encode** the words.

```python
# Define vocabulary size
vocab_size = 30  # Arbitrary vocabulary size

# Encode the reviews
encoded_reviews = [one_hot(review, vocab_size) for review in reviews]
print(encoded_reviews)
```

**Example Output (Each word is mapped to a unique integer):**
```
[[3, 18], [14, 25], [27, 15], [29, 15, 6], [6, 18, 22], [14, 18], [2, 18, 15], [29, 3], [29, 14], [24, 16]]
```

---

## **Step 5: Pad Sequences**
Since reviews have different lengths, we **pad shorter sequences with zeros** to ensure uniform input size.

```python
# Define max length
max_length = 4  

# Pad sequences to ensure uniform shape
padded_reviews = pad_sequences(encoded_reviews, maxlen=max_length, padding="post")
print(padded_reviews)
```

**Example Output (Zero-padded sequences):**
```
[[ 3 18  0  0]
 [14 25  0  0]
 [27 15  0  0]
 [29 15  6  0]
 [ 6 18 22  0]
 [14 18  0  0]
 [ 2 18 15  0]
 [29  3  0  0]
 [29 14  0  0]
 [24 16  0  0]]
```

---

## **Step 6: Build the Neural Network**
We use:
- **Embedding layer** to convert words into meaningful vector representations.
- **Flatten layer** to transform embeddings into a single vector.
- **Dense layer** for binary classification.

```python
# Define embedding vector size
embedding_vector_size = 5

# Build the model
model = Sequential()
model.add(Embedding(vocab_size, embedding_vector_size, input_length=max_length, name="embedding"))
model.add(Flatten())
model.add(Dense(1, activation="sigmoid"))  # Sigmoid for binary classification

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Display model summary
model.summary()
```

---

## **Step 7: Train the Model**
```python
# Define inputs (X) and outputs (y)
X = padded_reviews
y = sentiment

# Train the model
model.fit(X, y, epochs=50, verbose=1)
```

The training output shows **loss and accuracy** improving over time.

---

## **Step 8: Make Predictions**
Now, let's classify new reviews.

### **1. Predict Sentiment of Encoded Data**
```python
# Example input (manually encoded and padded)
prediction = model.predict(np.array([[14, 25, 0, 0]]))  # "amazing restaurant"
prediction = (prediction > 0.5).astype("int32")  # Convert probability to 0 or 1
print(prediction)
```

**Example Output:**
```
[[1]]  # Positive sentiment
```

---

### **2. Predict Sentiment of New Reviews**
We need to **encode and pad** any new review before prediction.

```python
def predict_review(review):
    # Convert text to numerical encoding
    encoded_review = one_hot(review, vocab_size)
    
    # Pad the sequence
    padded_review = pad_sequences([encoded_review], maxlen=max_length, padding="post")
    
    # Make prediction
    prediction = model.predict(padded_review)
    sentiment = "Positive" if prediction > 0.5 else "Negative"
    
    return sentiment

# Test new reviews
print(predict_review("good food"))  # Expected: Positive
print(predict_review("awful service"))  # Expected: Negative
```

---

## **Step 9: Save and Load the Model**
Save the trained model for future use.

```python
# Save the model
model.save("sentiment_analysis_model.h5")

# Load the model
from tensorflow.keras.models import load_model
loaded_model = load_model("sentiment_analysis_model.h5")
print("Model loaded successfully!")
```

---

## **Next Steps**
- **Use a larger dataset** for better accuracy.
- **Use pre-trained word embeddings** like Word2Vec or GloVe.
- **Deploy the model** using **Flask or FastAPI**.
- **Experiment with different architectures**, such as adding LSTMs for sequential analysis.

This walkthrough provides a **complete guide** to **sentiment classification using word embeddings in Keras**! 🚀 Let me know if you need modifications or explanations.
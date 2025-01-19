Sure! Let's create a **simpler real-world example** of an RNN for high school students using NLP. We’ll build a **text sentiment analysis** model that predicts whether a sentence is positive or negative. This is a practical, beginner-friendly example of using an RNN for Natural Language Processing (NLP).

---

### Problem:
We’ll use a small dataset of sentences labeled as **positive** or **negative** and train an RNN to classify them.

---

### Step 1: Install Required Libraries
```bash
pip install tensorflow numpy matplotlib
```

---

### Step 2: Import Libraries
```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
import matplotlib.pyplot as plt
```

---

### Step 3: Prepare the Dataset
Here’s a small dataset of sentences with their corresponding labels:
- 1: Positive sentiment
- 0: Negative sentiment

```python
# Sample dataset: sentences and their sentiment labels
sentences = [
    "I love this movie",
    "This was an excellent day",
    "I feel great about the project",
    "The weather is beautiful today",
    "I am so happy",
    "This is terrible",
    "I hate this experience",
    "This is the worst day ever",
    "I feel so bad",
    "This is awful"
]

labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]  # Positive: 1, Negative: 0
```

---

### Step 4: Tokenize and Pad the Text Data
Convert the text into numerical sequences and ensure they are of the same length for RNN input.

```python
# Tokenize the sentences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print("Word Index:", word_index)

# Convert sentences to sequences
sequences = tokenizer.texts_to_sequences(sentences)

# Pad sequences to make them of equal length
padded_sequences = pad_sequences(sequences, padding='post')
print("Padded Sequences:", padded_sequences)
```

---

### Step 5: Build the RNN Model
An RNN processes the input sequence step by step to understand the sentence meaning.

```python
# Define the model
model = Sequential([
    Embedding(input_dim=len(word_index) + 1, output_dim=8, input_length=padded_sequences.shape[1]),
    SimpleRNN(16, activation='relu'),
    Dense(1, activation='sigmoid')  # Output layer for binary classification
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()
```

---

### Step 6: Train the Model
Split the data into training and testing sets, then train the model.

```python
# Convert labels to numpy array
labels = np.array(labels)

# Train the model
history = model.fit(padded_sequences, labels, epochs=10, batch_size=2)
```

---

### Step 7: Test the Model
Use new sentences to test the model’s predictions.

```python
# New sentences to predict sentiment
test_sentences = ["I am so excited", "This is the worst experience"]

# Tokenize and pad the test sentences
test_sequences = tokenizer.texts_to_sequences(test_sentences)
test_padded = pad_sequences(test_sequences, maxlen=padded_sequences.shape[1], padding='post')

# Predict sentiment
predictions = model.predict(test_padded)

# Print results
for i, sentence in enumerate(test_sentences):
    sentiment = "Positive" if predictions[i] > 0.5 else "Negative"
    print(f"'{sentence}' -> {sentiment}")
```

---

### Step 8: Visualize the Training Process
Plot the training accuracy to see how the model improved.

```python
# Plot accuracy
plt.plot(history.history['accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.show()
```

---

### Complete Code

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
import matplotlib.pyplot as plt

# Dataset
sentences = [
    "I love this movie",
    "This was an excellent day",
    "I feel great about the project",
    "The weather is beautiful today",
    "I am so happy",
    "This is terrible",
    "I hate this experience",
    "This is the worst day ever",
    "I feel so bad",
    "This is awful"
]
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# Tokenize and pad sequences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(sentences)
padded_sequences = pad_sequences(sequences, padding='post')

# Build the model
model = Sequential([
    Embedding(input_dim=len(word_index) + 1, output_dim=8, input_length=padded_sequences.shape[1]),
    SimpleRNN(16, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

# Train the model
labels = np.array(labels)
history = model.fit(padded_sequences, labels, epochs=10, batch_size=2)

# Test the model
test_sentences = ["I am so excited", "This is the worst experience"]
test_sequences = tokenizer.texts_to_sequences(test_sentences)
test_padded = pad_sequences(test_sequences, maxlen=padded_sequences.shape[1], padding='post')
predictions = model.predict(test_padded)

# Print results
for i, sentence in enumerate(test_sentences):
    sentiment = "Positive" if predictions[i] > 0.5 else "Negative"
    print(f"'{sentence}' -> {sentiment}")

# Plot accuracy
plt.plot(history.history['accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.show()
```

---

### Key Points:
1. **Dataset Simplicity:** Small dataset with a clear purpose.
2. **Readable Code:** Easy to follow with minimal complexity.
3. **Immediate Results:** Students can see the model predict sentiments for test sentences.

This example uses simple NLP tasks that high school students can relate to, making it an engaging way to introduce RNNs.
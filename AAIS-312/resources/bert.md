# **Step-by-Step Walkthrough: Using BERT for Text Classification with Keras**
In this walkthrough, we will use **BERT (Bidirectional Encoder Representations from Transformers)** from Hugging Face's Transformers library with **TensorFlow and Keras** to build a **sentiment classification model**.

---

## **Step 1: Install Required Libraries**
Ensure you have **TensorFlow**, **transformers**, and **Hugging Face datasets** installed.

```bash
pip install tensorflow transformers datasets
```

---

## **Step 2: Import Necessary Libraries**
```python
import tensorflow as tf
import numpy as np
from transformers import BertTokenizer, TFBertForSequenceClassification
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from datasets import load_dataset
```

---

## **Step 3: Load a Pre-Trained BERT Model**
We will use **BERT base uncased** fine-tuned for sentiment classification.

```python
# Load pre-trained tokenizer and model
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = TFBertForSequenceClassification.from_pretrained(model_name, num_labels=2)  # 2 labels (positive & negative)
```

---

## **Step 4: Load and Preprocess the Dataset**
We will use the **IMDB movie reviews dataset**.

```python
# Load dataset
dataset = load_dataset("imdb")

# Split into train and test
train_texts, train_labels = dataset["train"]["text"], dataset["train"]["label"]
test_texts, test_labels = dataset["test"]["text"], dataset["test"]["label"]
```

### **Tokenize the Data**
BERT requires tokenized input, so we **convert text to input IDs and attention masks**.

```python
# Tokenize training and test data
train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=512, return_tensors="tf")
test_encodings = tokenizer(test_texts, truncation=True, padding=True, max_length=512, return_tensors="tf")

# Convert labels to tensors
train_labels = np.array(train_labels)
test_labels = np.array(test_labels)
```

---

## **Step 5: Build the BERT Classifier Model**
We will use **Keras Functional API** to integrate BERT with additional layers.

```python
# Define input layers
input_ids = tf.keras.layers.Input(shape=(512,), dtype=tf.int32, name="input_ids")
attention_mask = tf.keras.layers.Input(shape=(512,), dtype=tf.int32, name="attention_mask")

# Get BERT outputs
bert_outputs = model.bert(input_ids, attention_mask=attention_mask)[1]  # Pooled output

# Add a Dense layer for classification
dense = tf.keras.layers.Dense(128, activation="relu")(bert_outputs)
output = tf.keras.layers.Dense(2, activation="softmax")(dense)  # Binary classification (positive/negative)

# Create the final model
bert_classifier = tf.keras.Model(inputs=[input_ids, attention_mask], outputs=output)

# Compile the model
bert_classifier.compile(
    optimizer=Adam(learning_rate=2e-5),
    loss=SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"]
)

# Display model summary
bert_classifier.summary()
```

---

## **Step 6: Train the Model**
Train the **BERT sentiment classifier** using the IMDB dataset.

```python
# Train the model
bert_classifier.fit(
    x={"input_ids": train_encodings["input_ids"], "attention_mask": train_encodings["attention_mask"]},
    y=train_labels,
    validation_data=(
        {"input_ids": test_encodings["input_ids"], "attention_mask": test_encodings["attention_mask"]},
        test_labels
    ),
    epochs=3,
    batch_size=8
)
```

---

## **Step 7: Evaluate the Model**
Check model performance on the test set.

```python
# Evaluate on test data
loss, accuracy = bert_classifier.evaluate(
    {"input_ids": test_encodings["input_ids"], "attention_mask": test_encodings["attention_mask"]},
    test_labels
)

print(f"Test Accuracy: {accuracy * 100:.2f}%")
```

---

## **Step 8: Make Predictions**
Now, let's predict the sentiment of a new text input.

```python
# Function to classify text
def predict_sentiment(text):
    tokens = tokenizer(text, truncation=True, padding="max_length", max_length=512, return_tensors="tf")
    prediction = bert_classifier.predict({"input_ids": tokens["input_ids"], "attention_mask": tokens["attention_mask"]})
    sentiment = "Positive" if np.argmax(prediction) == 1 else "Negative"
    return sentiment

# Example predictions
print(predict_sentiment("This movie was absolutely amazing!"))
print(predict_sentiment("I hated this film. It was the worst."))
```

**Example Output:**
```
Positive
Negative
```

---

## **Step 9: Save and Load the Model**
Save the trained model for future use.

```python
# Save the model
bert_classifier.save("bert_sentiment_model.h5")

# Load the model
loaded_model = tf.keras.models.load_model("bert_sentiment_model.h5", custom_objects={"TFBertForSequenceClassification": TFBertForSequenceClassification})
print("Model loaded successfully!")
```

---

## **Next Steps**
- **Fine-tune BERT** on your custom dataset.
- **Use a different pre-trained model**, such as **DistilBERT** for faster inference.
- **Deploy the model** using **FastAPI or Flask**.
- **Convert the model** to TensorFlow Lite for mobile applications.

This walkthrough provides a **complete guide** to **training and using BERT for sentiment analysis** with **TensorFlow and Keras**. 🚀 Let me know if you have any questions!
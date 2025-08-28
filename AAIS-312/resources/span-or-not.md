
# Step-by-Step Walkthrough: Ham vs Spam Detection Using Deep Learning

## Step 1: Install Required Libraries

We’ll use TensorFlow/Keras for the model, NumPy/Pandas for data, and Scikit-learn for metrics.

```bash
pip install tensorflow numpy pandas scikit-learn matplotlib
```

---

## Step 2: Import Necessary Libraries

```python
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt
```

---

## Step 3: Load the Ham/Spam Dataset

Your CSV should have two columns: `message` (text) and `label` (`ham` or `spam`).

```python
df = pd.read_csv("ham_spam_dataset_20k.csv")

print(df.head())
print(df['label'].value_counts())   # sanity check
```

**Why this matters:**

* Quick inspection helps confirm columns and class balance.
* If the dataset is skewed (e.g., more ham than spam), we might use class weights later.

---

## Step 4: Preprocess the Data

We’ll encode `ham`→0 and `spam`→1, split into train/test, then **tokenize** (convert words to integer IDs) and **pad** (make all sequences the same length).

```python
# Encode labels: ham->0, spam->1
le = LabelEncoder()
y = le.fit_transform(df['label'].astype(str))

# Train/test split (80/20), stratified to keep class balance
X_train_text, X_test_text, y_train, y_test = train_test_split(
    df['message'].astype(str).values,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Tokenize
num_words = 10000      # keep top 10k words
oov_token = "<OOV>"    # for out-of-vocabulary words
tokenizer = Tokenizer(num_words=num_words, oov_token=oov_token)
tokenizer.fit_on_texts(X_train_text)

# Convert texts -> integer sequences
X_train_seq = tokenizer.texts_to_sequences(X_train_text)
X_test_seq  = tokenizer.texts_to_sequences(X_test_text)

# Pad/truncate to fixed length (short SMS often < 60 tokens)
max_length = 60
X_train = pad_sequences(X_train_seq, maxlen=max_length, padding="post", truncating="post")
X_test  = pad_sequences(X_test_seq,  maxlen=max_length, padding="post", truncating="post")

print("Train shape:", X_train.shape)  # (N_train, 60)
print("Test shape:", X_test.shape)    # (N_test, 60)
```

**Why tokenization & padding?**

* Neural nets expect fixed-size numeric tensors.
* Tokenization maps each word to an ID; padding ensures equal length.

---

## Step 5: Build the Neural Network

We’ll use an **Embedding** (learns word meaning), then an **LSTM** (sequence understanding), and dense layers to classify.

```python
model = keras.Sequential([
    layers.Embedding(input_dim=num_words, output_dim=64, input_length=max_length),
    layers.LSTM(64, return_sequences=False),
    layers.Dense(32, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(1, activation='sigmoid')  # probability of spam
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()
```

**Why these choices?**

* `Embedding`: turns words into dense vectors that capture similarity (e.g., “offer” \~ “deal”).
* `LSTM`: captures order/context—useful for phrases like “verify your account now.”

---

## Step 6: Train the Model

We’ll also add **EarlyStopping** to avoid overfitting.

```python
callbacks = [
    keras.callbacks.EarlyStopping(monitor="val_loss", patience=2, restore_best_weights=True)
]

history = model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=5,
    batch_size=128,
    callbacks=callbacks,
    verbose=1
)

# Optional: visualize training curves
plt.figure()
plt.plot(history.history["accuracy"], label="train_acc")
plt.plot(history.history["val_accuracy"], label="val_acc")
plt.title("Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()
```

**Notes:**

* `batch_size=128` means we process 128 messages per step (faster & more stable than 1-by-1).
* If validation accuracy plateaus or drops, EarlyStopping halts training and restores the best model.

---

## Step 7: Evaluate the Model

We’ll print accuracy, precision/recall/F1, and AUC. We’ll also look at a **confusion matrix** to see error types.

```python
# Basic accuracy
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {test_acc:.4f}")

# Detailed metrics
y_prob = model.predict(X_test).ravel()          # probabilities (0..1)
y_pred = (y_prob >= 0.5).astype(int)            # default threshold 0.5

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["ham","spam"]))

print("ROC-AUC:", roc_auc_score(y_test, y_prob))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix (rows=true, cols=pred):\n", cm)
```

**Interpreting results:**

* **Precision (spam)**: Of messages tagged spam, how many truly spam?
* **Recall (spam)**: Of all spam messages, how many did we catch?
* **AUC**: Threshold-independent measure of separability (higher is better).
* **Confusion matrix**:

  * `cm[0,0]`: ham correctly predicted as ham
  * `cm[0,1]`: ham incorrectly predicted as spam (false positives)
  * `cm[1,0]`: spam missed as ham (false negatives)
  * `cm[1,1]`: spam correctly predicted as spam

---

## Step 8: Threshold Tuning (Optional but Useful)

If you prefer **fewer false positives** (don’t annoy users by flagging legit messages), adjust the threshold.

```python
def evaluate_at_threshold(th):
    yp = (y_prob >= th).astype(int)
    print(f"\n--- Threshold = {th:.2f} ---")
    print(classification_report(y_test, yp, target_names=["ham","spam"]))
    print("Confusion matrix:\n", confusion_matrix(y_test, yp))

for th in [0.3, 0.5, 0.7]:
    evaluate_at_threshold(th)
```

**Tip:** Pick a threshold based on your use case (compliance teams value recall; user UX teams value precision).

---

## Step 9: Make Predictions (Inference)

Helper that tokenizes, pads, predicts, and returns a label + score.

```python
def predict_spam(text, threshold=0.5):
    seq = tokenizer.texts_to_sequences([text])
    pad = pad_sequences(seq, maxlen=max_length, padding="post", truncating="post")
    p = model.predict(pad, verbose=0)[0][0]
    label = "spam" if p >= threshold else "ham"
    return label, float(p)

# Try it
print(predict_spam("Congratulations! You've won a $1000 gift card. Click here now!"))
print(predict_spam("Hey, are we still meeting at 3 pm?"))
```

---

## Step 10: Save and Load the Model + Tokenizer

You need both the model **and** the tokenizer (vocabulary) to reproduce predictions later.

```python
# Save model
model.save("ham_spam_model.h5")

# Save tokenizer
import json
tokenizer_json = tokenizer.to_json()
with open("tokenizer.json", "w") as f:
    f.write(tokenizer_json)

# Load later
loaded_model = keras.models.load_model("ham_spam_model.h5")
print("Model loaded!")

from tensorflow.keras.preprocessing.text import tokenizer_from_json
with open("tokenizer.json", "r") as f:
    loaded_tokenizer = tokenizer_from_json(json.load(f))
```

---

## Step 11: Common Improvements (Optional)

* **Bidirectional LSTM/GRU**: Better context capture.

  ```python
  model = keras.Sequential([
      layers.Embedding(num_words, 128, input_length=max_length),
      layers.Bidirectional(layers.LSTM(64)),
      layers.Dense(64, activation="relu"),
      layers.Dropout(0.4),
      layers.Dense(1, activation="sigmoid")
  ])
  ```
* **TextVectorization** (Keras layer) instead of `Tokenizer` for an all-Keras pipeline.
* **Conv1D** model (faster) for short messages:

  ```python
  model = keras.Sequential([
      layers.Embedding(num_words, 128, input_length=max_length),
      layers.Conv1D(128, 5, activation="relu"),
      layers.GlobalMaxPool1D(),
      layers.Dense(64, activation="relu"),
      layers.Dropout(0.3),
      layers.Dense(1, activation="sigmoid")
  ])
  ```
* **Pretrained embeddings** (e.g., GloVe) for richer word semantics.
* **Regularization**: Dropout, L2.
* **Class weights** if labels are imbalanced:

  ```python
  from sklearn.utils.class_weight import compute_class_weight
  classes = np.array([0,1])
  cw = compute_class_weight("balanced", classes=classes, y=y_train)
  class_weight = {0: cw[0], 1: cw[1]}
  # then pass class_weight=class_weight in model.fit(...)
  ```

---

## Step 12: Deployment Next Steps

* **Batch inference**: read a CSV of messages, add predictions.
* **API**: Wrap `predict_spam()` in **FastAPI** or **Flask**.
* **Monitoring**: Track precision/recall drift over time; retrain if needed.
* **Abuse protection**: Rate limiting, logging, and threshold tuning.

---


Sure! Below is a **PyTorch-based walkthrough** for **BERT-based sentiment classification** using a **small dataset**. This guide covers **loading BERT, preparing a dataset, training, evaluation, and inference** using Hugging Face's `transformers` and PyTorch.

---

# **Step-by-Step Walkthrough: Using BERT for Sentiment Classification in PyTorch**

## **Step 1: Install Required Libraries**
Before running the code, install the necessary libraries:

```bash
pip install torch transformers datasets
```
- **`torch`**: PyTorch, a deep learning framework for model training.
- **`transformers`**: Hugging Face's library for pre-trained NLP models.
- **`datasets`**: Provides NLP datasets (optional for this small dataset example).

---

## **Step 2: Import Required Libraries**
```python
import torch
import numpy as np
from torch.utils.data import DataLoader, Dataset
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import AdamW
from torch.nn import functional as F
```

### **What each import does:**
- **`torch`**: Main PyTorch library for tensors and model training.
- **`np` (NumPy)**: Handles numerical arrays.
- **`DataLoader, Dataset`**: Helps manage and batch the dataset efficiently.
- **`BertTokenizer`**: Tokenizes input text.
- **`BertForSequenceClassification`**: A BERT model specifically for classification tasks.
- **`AdamW`**: An improved version of the Adam optimizer for fine-tuning transformers.
- **`functional as F`**: Provides functions like softmax, cross-entropy loss, etc.

---

## **Step 3: Load a Pre-Trained BERT Model**
```python
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)
```

### **Explanation:**
- **Loads the BERT tokenizer** to convert text into input tokens.
- **Loads a pre-trained BERT model** with a classification head for **binary classification (`num_labels=2`)**.

#### **Why use a pre-trained model?**
BERT has been pre-trained on **massive text datasets**, so it already understands **language patterns**. Fine-tuning adapts it for sentiment classification.

---

## **Step 4: Prepare a Small Custom Dataset**
Instead of a large dataset, we manually define a small dataset.

```python
train_texts = [
    "I love this movie!", "This film was fantastic!", "Amazing experience!", 
    "Worst movie ever.", "I hated the plot.", "Terrible acting!"
]
train_labels = [1, 1, 1, 0, 0, 0]  # 1 = Positive, 0 = Negative

test_texts = ["This was a great movie!", "I did not enjoy this film."]
test_labels = [1, 0]
```

### **Explanation:**
- **train_texts**: Small set of positive and negative **movie reviews**.
- **train_labels**: Sentiment labels (`1` = **Positive**, `0` = **Negative**).
- **test_texts/test_labels**: A small test set for model evaluation.

---

## **Step 5: Tokenize the Data**
We need to convert the text into **numerical input IDs and attention masks**.

```python
train_encodings = tokenizer(train_texts, truncation=True, padding=True, return_tensors="pt")
test_encodings = tokenizer(test_texts, truncation=True, padding=True, return_tensors="pt")

# Convert labels to PyTorch tensors
train_labels = torch.tensor(train_labels)
test_labels = torch.tensor(test_labels)
```

### **What happens here?**
- **Tokenization**: Converts text into numerical representations.
- **`truncation=True`**: Ensures that long texts are **truncated** to fit the model.
- **`padding=True`**: Ensures all sentences are the **same length**.
- **`return_tensors="pt"`**: Returns PyTorch tensors.
- **Converts labels to tensors (`torch.tensor`)** for compatibility with PyTorch.

---

## **Step 6: Create a PyTorch Dataset**
We define a custom dataset class that returns **input tensors and labels**.

```python
class SentimentDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}, self.labels[idx]
```

### **What happens here?**
- **Inherits from `Dataset`** to work with PyTorch `DataLoader`.
- **`__getitem__`**: Returns tokenized inputs (`input_ids`, `attention_mask`) and labels.
- **`__len__`**: Returns the dataset size.

Now, we **create dataset objects**:

```python
train_dataset = SentimentDataset(train_encodings, train_labels)
test_dataset = SentimentDataset(test_encodings, test_labels)
```

---

## **Step 7: Load Data in Batches**
We use a **DataLoader** to efficiently load data during training.

```python
train_loader = DataLoader(train_dataset, batch_size=2, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=2, shuffle=False)
```

### **What happens here?**
- **`batch_size=2`**: The model processes two samples per batch.
- **`shuffle=True`**: Randomizes training data order.

---

## **Step 8: Fine-Tune BERT**
Now, we **define an optimizer and loss function**:

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

optimizer = AdamW(model.parameters(), lr=2e-5)
loss_fn = torch.nn.CrossEntropyLoss()
```

### **What happens here?**
- **Moves the model to GPU (`cuda`) if available** for faster training.
- **Uses AdamW** for optimized weight updates.
- **Defines CrossEntropyLoss**, suitable for classification.

### **Train the Model**
```python
model.train()

for epoch in range(3):
    total_loss = 0
    for batch in train_loader:
        inputs, labels = batch
        inputs = {key: val.to(device) for key, val in inputs.items()}
        labels = labels.to(device)

        optimizer.zero_grad()
        outputs = model(**inputs)
        loss = loss_fn(outputs.logits, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}: Loss = {total_loss:.4f}")
```

### **Explanation:**
- **`model.train()`**: Sets the model to training mode.
- **Iterates over batches**:
  - Moves inputs & labels to **GPU (if available)**.
  - **Zeroes gradients** before backpropagation.
  - **Computes loss**, **backpropagates**, and updates weights.
  - **Accumulates loss** to track training progress.

---

## **Step 9: Evaluate the Model**
Now, we check the model's accuracy.

```python
model.eval()
correct = 0
total = 0

with torch.no_grad():
    for batch in test_loader:
        inputs, labels = batch
        inputs = {key: val.to(device) for key, val in inputs.items()}
        labels = labels.to(device)

        outputs = model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=1)
        correct += (predictions == labels).sum().item()
        total += labels.size(0)

print(f"Test Accuracy: {100 * correct / total:.2f}%")
```

### **Explanation:**
- **`model.eval()`**: Sets the model to evaluation mode.
- **No gradients are computed (`torch.no_grad()`)** to save memory.
- **Predictions are compared to actual labels** to compute accuracy.

---

## **Step 10: Make Predictions**
```python
def predict_sentiment(text):
    tokens = tokenizer(text, truncation=True, padding="max_length", max_length=512, return_tensors="pt")
    tokens = {key: val.to(device) for key, val in tokens.items()}

    with torch.no_grad():
        outputs = model(**tokens)
        prediction = torch.argmax(outputs.logits, dim=1).item()

    return "Positive" if prediction == 1 else "Negative"

print(predict_sentiment("I absolutely loved this film!"))
print(predict_sentiment("This was the worst experience ever."))
```

---

## **Next Steps**
- Train on a **larger dataset**.
- Use **DistilBERT** for **faster inference**.
- Deploy the model using **FastAPI or Flask**.

This is a **complete PyTorch-based BERT text classifier**. 🚀 Let me know if you have questions!
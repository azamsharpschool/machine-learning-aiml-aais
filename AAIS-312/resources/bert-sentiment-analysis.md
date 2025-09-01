
# 🧠 Walkthrough: Using BERT for Sentiment Analysis

---

## 🎯 Goal

We’ll use a pretrained **BERT** model to figure out whether a sentence expresses a **positive** or **negative** feeling.

---

## 🔧 Step 1: Install the Tools

Run this once in your terminal:

```bash
pip install transformers torch
```

---

## 📦 Step 2: Import the Pipeline

```python
from transformers import pipeline
```

---

## 🏗️ Step 3: Load a Pretrained BERT Sentiment Model

```python
sentiment_analyzer = pipeline("sentiment-analysis")
```

This automatically downloads a BERT-based model trained on movie reviews (positive/negative).

---

## ✍️ Step 4: Write Sentences to Test

```python
texts = [
    "I love this new iPhone, it’s amazing!",
    "The cafeteria food is terrible.",
    "My teacher is really kind and helpful.",
    "This movie was boring and way too long."
]
```

---

## 🤖 Step 5: Run the Model

```python
results = sentiment_analyzer(texts)
```

---

## 🖨️ Step 6: Print the Results

```python
for t, r in zip(texts, results):
    print(f"Text: {t}")
    print(f"Sentiment: {r['label']} (score: {r['score']:.2f})")
    print("-" * 40)
```

---

## ✅ Example Output

```
Text: I love this new iPhone, it’s amazing!
Sentiment: POSITIVE (score: 0.99)
----------------------------------------
Text: The cafeteria food is terrible.
Sentiment: NEGATIVE (score: 0.99)
----------------------------------------
Text: My teacher is really kind and helpful.
Sentiment: POSITIVE (score: 0.99)
----------------------------------------
Text: This movie was boring and way too long.
Sentiment: NEGATIVE (score: 0.98)
----------------------------------------
```

---

# 🎉 What We Learned

* BERT can judge the **tone or mood** of a sentence.
* It looks at the **words in context**, not just individually.
* We can feed in **multiple sentences at once** and get results.

---


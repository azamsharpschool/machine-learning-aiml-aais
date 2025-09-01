
# 🧠 Walkthrough: Using a Pretrained Model for Summarization

---

## 🎯 Goal

Take a long paragraph and let the model generate a **short summary**.

---

## 🔧 Step 1: Install the Tools

Run this once:

```bash
pip install transformers torch
```

---

## 📦 Step 2: Import the Pipeline

```python
from transformers import pipeline
```

---

## 🏗️ Step 3: Load a Pretrained Summarization Model

```python
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
```

This loads **BART**, trained on news articles for summarization.

---

## 📖 Step 4: Provide a Long Text

```python
article = """
The Amazon rainforest, often referred to as the lungs of the planet, is home to more than 
three million species of plants and animals. It produces 20% of the world’s oxygen and plays 
a critical role in regulating global climate. However, deforestation has been increasing in 
recent decades due to logging, agriculture, and urbanization. Scientists warn that continued 
destruction could have catastrophic effects, not just for biodiversity, but also for the 
millions of people who depend on the rainforest for food, medicine, and shelter.
"""
```

---

## 🤖 Step 5: Run the Model

```python
summary = summarizer(article, max_length=60, min_length=25, do_sample=False)
```

* `max_length` → maximum number of words in the summary
* `min_length` → minimum number of words in the summary
* `do_sample=False` → makes the output more consistent

---

## 🖨️ Step 6: Print the Summary

```python
print("Original text:\n", article)
print("\n--- SUMMARY ---")
print(summary[0]['summary_text'])
```

---

## ✅ Example Output

```
Original text:
The Amazon rainforest, often referred to as the lungs of the planet, is home to more than 
three million species of plants and animals...

--- SUMMARY ---
The Amazon rainforest produces 20% of the world’s oxygen and regulates climate. 
Deforestation threatens biodiversity and millions of people who rely on it.
```

---

# 🎉 What We Learned

* Pretrained models like **BART** can **read long passages** and **summarize them automatically**.
* We don’t need to train it ourselves — just give it text and it does the hard work.
* Students can paste their own paragraphs (from a science book, news story, or even Wikipedia) and instantly get a summary.


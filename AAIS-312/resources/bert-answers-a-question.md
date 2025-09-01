
# 🧠 Walkthrough: Using BERT to Answer Questions from Text

---

## 🎯 Goal

We’ll use **BERT**, a pretrained language model, to **read a short passage** and then **answer questions** about it.

---

## 🔧 Step 1: Install the Tools

We need a library called **transformers** (from Hugging Face) that gives us access to pretrained models.

Open your terminal (or command prompt) and run:

```bash
pip install transformers torch
```

---

## 📦 Step 2: Import the Pipeline

In Python, a **pipeline** is like a ready-to-use shortcut for common AI tasks.

```python
from transformers import pipeline
```

---

## 🏗️ Step 3: Load a Pretrained BERT Model

We’ll use a BERT model that has already been trained to answer questions.

```python
qa = pipeline(
    "question-answering",
    model="bert-large-uncased-whole-word-masking-finetuned-squad"
)
```

* `"question-answering"` tells the pipeline what we want to do.
* The model name points to a BERT model that was trained on the **SQuAD dataset** (a big set of questions/answers).

---

## 📖 Step 4: Give BERT a Passage (Context)

BERT needs some text to “read” before it can answer.

```python
context = """
The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. 
It is named after the engineer Gustave Eiffel, whose company designed and built the tower. 
It was constructed from 1887 to 1889 as the centerpiece of the 1889 World's Fair.
"""
```

---

## ❓ Step 5: Ask a Question

Now we ask something about the passage.

```python
question = "When was the Eiffel Tower built?"
```

---

## 🤖 Step 6: Run the Model

Let’s give BERT the **context** and **question**, and see what it finds.

```python
result = qa(question=question, context=context)
```

---

## 🖨️ Step 7: Print the Answer

Finally, display the result:

```python
print("Question:", question)
print("Answer:", result["answer"])
```

---

## ✅ Example Output

```
Question: When was the Eiffel Tower built?
Answer: 1887 to 1889
```

---

# 🎉 What We Learned

* BERT reads the **whole passage** at once.
* It understands words in **context** (both left and right).
* It can **find exact answers** from text, just like a student searching a paragraph.


# **Walkthrough: Basic Functionalities of spaCy in Python**

## **Introduction to spaCy**
**spaCy** is an advanced, high-performance **Natural Language Processing (NLP)** library designed for **tokenization, Named Entity Recognition (NER), Part-of-Speech (POS) tagging, dependency parsing, lemmatization**, and more.

### **Why Use spaCy?**
✅ **Fast and Efficient** – Optimized for real-world NLP tasks.  
✅ **Pre-trained Models** – Provides ready-to-use models for multiple languages.  
✅ **Production-Ready** – Widely used in enterprise applications.  

---

## **1. Installation**
Before using spaCy, install the package and download a language model:

```bash
pip install spacy
python -m spacy download en_core_web_sm
```
- `en_core_web_sm` is a **small English language model** with basic NLP features.
- Other models include:
  - `en_core_web_md` (Medium model, includes word vectors)
  - `en_core_web_lg` (Large model with better accuracy)

---

## **2. Loading a Language Model**
```python
import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Apple Inc. is planning to build a new office in San Francisco."
doc = nlp(text)
```
- `nlp` **processes** the text and returns a **Doc** object (`doc`).
- `doc` contains **tokens, POS tags, named entities, dependency structure, and more**.

---

## **3. Tokenization**
Tokenization is the process of **splitting text** into meaningful units (**tokens**).
```python
for token in doc:
    print(token.text)
```
**Output:**
```
Apple
Inc.
is
planning
to
build
a
new
office
in
San
Francisco
.
```
🔹 **spaCy's tokenization preserves punctuation and special characters**.

---

## **4. Stopword Removal**
**Stopwords** are common words like `"the"`, `"is"`, `"a"` that don’t add much meaning.
```python
filtered_tokens = [token.text for token in doc if not token.is_stop]
print(filtered_tokens)
```
**Output:**
```
['Apple', 'Inc.', 'planning', 'build', 'new', 'office', 'San', 'Francisco', '.']
```
🔹 **Only meaningful words remain**.

---

## **5. Lemmatization**
Lemmatization converts words into their **root (dictionary) form**.
```python
for token in doc:
    print(f"{token.text} → {token.lemma_}")
```
**Output:**
```
Apple → Apple
Inc. → Inc.
is → be
planning → plan
to → to
build → build
a → a
new → new
office → office
in → in
San → San
Francisco → Francisco
. → .
```
🔹 `"planning"` becomes `"plan"`, `"is"` becomes `"be"`.

---

## **6. Part-of-Speech (POS) Tagging**
Each token is assigned a **grammatical category** (e.g., noun, verb, adjective).
```python
for token in doc:
    print(f"{token.text}: {token.pos_}")
```
**Output:**
```
Apple: PROPN
Inc.: PROPN
is: AUX
planning: VERB
to: PART
build: VERB
a: DET
new: ADJ
office: NOUN
in: ADP
San: PROPN
Francisco: PROPN
.: PUNCT
```
🔹 `"planning"` is labeled as a `VERB`, `"Apple"` as a `PROPN` (Proper Noun).

---

## **7. Named Entity Recognition (NER)**
spaCy identifies **real-world entities** like companies, locations, and dates.
```python
for ent in doc.ents:
    print(f"{ent.text}: {ent.label_}")
```
**Output:**
```
Apple Inc.: ORG
San Francisco: GPE
```
🔹 `"Apple Inc."` is labeled as an `ORG` (Organization), `"San Francisco"` as `GPE` (Geopolitical Entity).

---

## **8. Dependency Parsing**
Dependency parsing shows **relationships between words** in a sentence.
```python
for token in doc:
    print(f"{token.text} → {token.dep_} → {token.head.text}")
```
**Output:**
```
Apple → compound → Inc.
Inc. → nsubj → planning
is → aux → planning
planning → ROOT → planning
to → aux → build
build → xcomp → planning
a → det → office
new → amod → office
office → dobj → build
in → prep → build
San → compound → Francisco
Francisco → pobj → in
. → punct → planning
```
🔹 `"planning"` is the **ROOT** (main verb), `"Apple"` is the **subject**.

---

## **9. Visualizing NLP Features**
### **Dependency Tree Visualization**
```python
from spacy import displacy
displacy.render(doc, style="dep", jupyter=True)
```
**Output:**  
➡️ **Dependency tree graph** showing how words are connected.

### **NER Visualization**
```python
displacy.render(doc, style="ent", jupyter=True)
```
**Output:**  
➡️ Entities are **highlighted** in different colors.

---

## **10. Custom Stopwords**
You can **add or remove** stopwords.
```python
# Add "planning" as a stopword
nlp.Defaults.stop_words.add("planning")

# Remove "the" from stopwords
nlp.Defaults.stop_words.remove("the")
```
🔹 Useful for **custom NLP pipelines**.

---

## **11. Custom Tokenizer**
You can create a **custom tokenizer** for domain-specific NLP.
```python
from spacy.tokenizer import Tokenizer

# Create a custom tokenizer
custom_tokenizer = Tokenizer(nlp.vocab, rules={"AI": [{"ORTH": "AI"}]})
nlp.tokenizer = custom_tokenizer

# Test custom tokenizer
doc = nlp("AI is changing the world.")
print([token.text for token in doc])
```
**Output:**
```
['AI', 'is', 'changing', 'the', 'world', '.']
```
🔹 `"AI"` is treated as a **single token**.

---

## **12. Text Similarity**
spaCy can measure **semantic similarity** between texts.
```python
doc1 = nlp("I love cats.")
doc2 = nlp("I adore felines.")

# Compute similarity
print(doc1.similarity(doc2))
```
**Output:**  
```
0.85  # (High similarity)
```
🔹 `"cats"` and `"felines"` are similar due to **word embeddings**.

---

## **13. Sentiment Analysis (via Pre-trained Models)**
While spaCy does not include built-in sentiment analysis, it can be done using external libraries like **TextBlob** or **VADER**:
```python
from textblob import TextBlob

text = "I love spaCy! It's the best NLP tool."
sentiment = TextBlob(text).sentiment
print(sentiment)
```
**Output:**
```
Sentiment(polarity=0.9, subjectivity=0.75)
```
🔹 **Polarity** = 0.9 (Very positive sentiment).  
🔹 **Subjectivity** = 0.75 (Highly opinionated).

---

## **Summary**
✅ **Tokenization** – Splitting text into words/sentences.  
✅ **Stopword Removal** – Removing unimportant words.  
✅ **Lemmatization** – Converting words to base forms.  
✅ **POS Tagging** – Identifying word types (noun, verb, etc.).  
✅ **Named Entity Recognition (NER)** – Identifying real-world entities.  
✅ **Dependency Parsing** – Understanding grammatical structure.  
✅ **Visualization** – Displaying NLP features using **displacy**.  
✅ **Customization** – Creating **custom stopwords, tokenizers, and rules**.  
✅ **Similarity & Sentiment Analysis** – Measuring **semantic similarity** and **emotion**.  

---

## **What’s Next?**
🔹 **Train a Custom NLP Model** – Fine-tune spaCy for **your dataset**.  
🔹 **Use spaCy for Chatbots** – Build an intelligent **AI assistant**.  
🔹 **Integrate spaCy with Machine Learning** – Combine **NLP & ML models**.  

🚀 **Now you’re ready to use spaCy for real-world NLP tasks!** 🚀
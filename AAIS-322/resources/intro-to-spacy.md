
# 🧑‍🏫 Introduction to spaCy in Google Colab

---

## 🔹 1. Install and Load spaCy

```python
# Install spaCy (latest version)
!pip install -U spacy

# Download a small English model (fast, ~12MB)
!python -m spacy download en_core_web_sm
```

**Explanation:**

* `!pip install` installs packages in Colab.
* `en_core_web_sm` is a pretrained English pipeline. It knows about tokenization rules, POS tagging, dependency parsing, and named entities.
* You can use larger models (`md`, `lg`) for better accuracy, but they’re bigger.

```python
import spacy
nlp = spacy.load("en_core_web_sm")  # load the pipeline
```

The `nlp` object is your **processing pipeline**. Every time you call `nlp(text)`, spaCy runs the text through multiple components (tokenizer, POS tagger, parser, NER, etc.).

---

## 🔹 2. Doc, Token, Span — The Core Data Structures

```python
doc = nlp("Apple is looking at buying U.K. startup for $1 billion.")

print("Whole doc:", doc.text)              # the entire text
print("Tokens:", [token.text for token in doc])  # tokenized words

span = doc[1:4]   # slice of doc = Span
print("Span:", span.text)
```

**Explanation:**

* `Doc`: the container object for processed text.
* `Token`: individual words/punctuation with lots of attributes.
* `Span`: a slice of tokens (like Python list slicing).
* Think of a `Doc` like a smart list of `Token` objects.

---

## 🔹 3. Token Attributes: Lemma & Stopwords

```python
doc = nlp("Running runners run quickly, but better results come from training.")

for token in doc:
    print(f"{token.text:<10} lemma={token.lemma_:<10} stopword={token.is_stop}")
```

**Explanation:**

* **Lemma**: base or dictionary form of a word.

  * `Running` → `run`
  * `better` → `good`
* **Stopword**: common words that often add little meaning (`the`, `is`, `but`).
* These attributes are useful for text cleaning and normalization.

---

## 🔹 4. Part-of-Speech (POS) and Dependency Parsing

```python
doc = nlp("The quick brown fox jumps over the lazy dog.")

for token in doc:
    print(f"{token.text:<10} POS={token.pos_:<6} DEP={token.dep_:<10} HEAD={token.head.text}")
```

**Explanation:**

* **POS** (`pos_`): grammatical role (NOUN, VERB, ADJ, etc.).
* **DEP** (`dep_`): dependency relation (subject, object, modifier).
* **HEAD**: the word that this token is attached to in the dependency tree.

This lets spaCy build a **syntactic structure** of the sentence.

---

## 🔹 5. Named Entity Recognition (NER)

```python
doc = nlp("Google is opening a new office in Berlin on July 15, 2025.")

for ent in doc.ents:
    print(ent.text, ent.label_)
```

**Explanation:**

* NER finds **real-world objects** in text:

  * `Google` → ORG
  * `Berlin` → GPE (Geo-Political Entity)
  * `July 15, 2025` → DATE
* Useful for extracting people, places, organizations, dates, money amounts.

**Visualize in Colab:**

```python
from spacy import displacy
displacy.render(doc, style="ent", jupyter=True)
```

This will highlight entities inside the notebook.

---

## 🔹 6. Pipelines: What Happens Inside `nlp`

```python
print("Pipeline steps:", nlp.pipe_names)
```

**Explanation:**

* Example output: `['tok2vec','tagger','parser','attribute_ruler','lemmatizer','ner']`
* Each is a **component** that processes the text in sequence.

You can disable components if you don’t need them (faster processing):

```python
with nlp.select_pipes(disable=["ner"]):
    doc = nlp("This is processed without NER.")
    print([t.text for t in doc])
```

---

## 🔹 7. Rule-Based Matching with `Matcher`

```python
from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)
pattern = [{"LEMMA": {"IN": ["buy", "acquire"]}}, {"POS": "PROPN", "OP": "+"}]
matcher.add("ACQUISITION", [pattern])

doc = nlp("Meta will acquire InstaTech. They may also buy FutureAI.")
for match_id, start, end in matcher(doc):
    print("Matched:", doc[start:end].text)
```

**Explanation:**

* **Matcher** lets you create rules for word patterns.
* This pattern matches:

  * A verb with lemma “buy” or “acquire”
  * Followed by one or more proper nouns (company names).
* Useful when pretrained NER misses something specific.

---

## 🔹 8. PhraseMatcher for Exact Phrases

```python
from spacy.matcher import PhraseMatcher

phrases = ["machine learning", "natural language processing"]
patterns = [nlp.make_doc(p) for p in phrases]

pm = PhraseMatcher(nlp.vocab)
pm.add("ML_TERMS", patterns)

doc = nlp("This course teaches machine learning and natural language processing.")
print([doc[start:end].text for _, start, end in pm(doc)])
```

**Explanation:**

* **PhraseMatcher** is faster than `Matcher` for fixed phrases.
* Great for keyword spotting (skills in resumes, product names, etc.).

---

## 🔹 9. Adding a Custom Component

```python
from spacy.language import Language

@Language.component("custom_component")
def custom_component(doc):
    # Flag if the text contains "AI"
    doc.user_data["has_ai"] = any(token.text.lower() == "ai" for token in doc)
    return doc

nlp.add_pipe("custom_component", last=True)

doc = nlp("AI is transforming industries.")
print("Contains 'AI'? ->", doc.user_data["has_ai"])
```

**Explanation:**

* You can extend the pipeline with your **own rules or ML models**.
* Here, we added a component that tags the doc if it contains “AI”.
* Components are just Python functions that receive and return a `Doc`.

---

✅ **Summary**:
By now, you know how to:

1. Install & load spaCy in Colab
2. Use `Doc`, `Token`, `Span`
3. Get lemmas, stopwords, POS tags, and dependencies
4. Extract entities (NER) and visualize them
5. Work with pipelines
6. Create rule-based matchers
7. Add your own pipeline components

---


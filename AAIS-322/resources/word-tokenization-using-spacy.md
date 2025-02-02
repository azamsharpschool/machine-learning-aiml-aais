# **Step-by-Step Walkthrough: Word Tokenization with spaCy**

## **Objective**
In this exercise, we will **tokenize text into individual words** using **spaCy**, a powerful Natural Language Processing (NLP) library in Python.

By the end of this tutorial, you will learn:
- How to tokenize text using spaCy
- How to handle punctuation in tokenization
- How to extract additional linguistic attributes like lemma, part of speech (POS), and stop words

---

## **Step 1: Install and Set Up spaCy**

### **1.1 Install spaCy**
If you haven’t installed spaCy yet, you can do so using **pip**:

```bash
pip install spacy
```

### **1.2 Download the English Language Model**
spaCy provides various pre-trained language models. For this exercise, we will use the **small English model (`en_core_web_sm`)**.

```bash
python -m spacy download en_core_web_sm
```

This model includes **tokenization, part-of-speech tagging, lemmatization, and named entity recognition**.

---

## **Step 2: Import spaCy and Load the Language Model**
Once installed, import the spaCy module and load the English language model.

```python
import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")
```

---

## **Step 3: Define the Input Text**
We need a sample text to **tokenize**. Let’s define a simple sentence:

```python
text = "Hello, world! Welcome to the world of Natural Language Processing."
```

---

## **Step 4: Process the Text with spaCy**
The `nlp` object processes the text and creates a **Doc object** that contains all the linguistic information.

```python
# Process the text using spaCy
doc = nlp(text)
```

---

## **Step 5: Tokenize the Text**
Now, we **iterate through the `doc` object** and print each token (word).

```python
# Extract and print tokens (words)
for token in doc:
    print(token.text)
```

### **Expected Output:**
```
Hello
,
world
!
Welcome
to
the
world
of
Natural
Language
Processing
.
```

Each token is printed on a new line, including **punctuation marks**.

---

## **Step 6: Handling Punctuation**
Since punctuation marks (`!`, `,`, `.`) are considered tokens, we may want to **filter them out**.

We can use **`is_punct`** to check whether a token is punctuation.

```python
# Print tokens while ignoring punctuation
for token in doc:
    if not token.is_punct:
        print(token.text)
```

### **Output (Punctuation Removed):**
```
Hello
world
Welcome
to
the
world
of
Natural
Language
Processing
```

---

## **Step 7: Explore Additional Token Attributes**
spaCy provides **various linguistic attributes** for each token, such as:
- **Lemma (`lemma_`)** → The base form of a word
- **Part of Speech (`pos_`)** → The grammatical category of the word (noun, verb, adjective, etc.)
- **Stop Word (`is_stop`)** → Whether the word is a common stop word (e.g., "the", "is", "and")

Let’s extract and print these attributes.

```python
# Print token attributes
for token in doc:
    print(f"Token: {token.text}, Lemma: {token.lemma_}, POS: {token.pos_}, Is Stopword: {token.is_stop}")
```

### **Example Output:**
```
Token: Hello, Lemma: hello, POS: INTJ, Is Stopword: False
Token: ,, Lemma: ,, POS: PUNCT, Is Stopword: False
Token: world, Lemma: world, POS: NOUN, Is Stopword: False
Token: !, Lemma: !, POS: PUNCT, Is Stopword: False
Token: Welcome, Lemma: welcome, POS: VERB, Is Stopword: False
Token: to, Lemma: to, POS: ADP, Is Stopword: True
Token: the, Lemma: the, POS: DET, Is Stopword: True
Token: world, Lemma: world, POS: NOUN, Is Stopword: False
Token: of, Lemma: of, POS: ADP, Is Stopword: True
Token: Natural, Lemma: natural, POS: ADJ, Is Stopword: False
Token: Language, Lemma: Language, POS: NOUN, Is Stopword: False
Token: Processing, Lemma: Processing, POS: NOUN, Is Stopword: False
Token: ., Lemma: ., POS: PUNCT, Is Stopword: False
```

### **Observations:**
- The **lemma** for `"Welcome"` is `"welcome"` (lowercased).
- `"to"` and `"the"` are **stop words**.
- `"Processing"` is classified as a **noun (NOUN)**.

---

## **Step 8: Count Word Frequencies**
Now, let’s **count the occurrences of each word** (excluding punctuation and stopwords).

```python
from collections import Counter

# Create a list of non-stopword tokens
words = [token.text.lower() for token in doc if not token.is_punct and not token.is_stop]

# Count word frequencies
word_freq = Counter(words)

# Print word frequency
print(word_freq)
```

### **Example Output:**
```
Counter({'world': 2, 'hello': 1, 'welcome': 1, 'natural': 1, 'language': 1, 'processing': 1})
```

✅ **"world" appears twice, while other words appear once.**

---

## **Step 9: Tokenization for Complex Texts**
Let’s try tokenizing a **longer paragraph**.

```python
paragraph = """Apple is expected to launch its new iPhone this year. 
Steve Jobs introduced the first iPhone in 2007, and it changed the smartphone industry forever!"""

doc2 = nlp(paragraph)

# Print tokens
print([token.text for token in doc2])
```

### **Example Output:**
```
['Apple', 'is', 'expected', 'to', 'launch', 'its', 'new', 'iPhone', 'this', 'year', '.', 
 'Steve', 'Jobs', 'introduced', 'the', 'first', 'iPhone', 'in', '2007', ',', 'and', 'it', 
 'changed', 'the', 'smartphone', 'industry', 'forever', '!']
```

---

## **Next Steps**
- **Try other languages** → Use `spacy.load("fr_core_news_sm")` for French.
- **Use custom stop words** → Add domain-specific words to the stop word list.
- **Build a chatbot or NLP application** using tokenization as a preprocessing step.

This walkthrough provides a **complete guide to word tokenization using spaCy**! 🚀 Let me know if you have any questions.
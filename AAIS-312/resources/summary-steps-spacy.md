### **Step 1: Data Preprocessing**

Data preprocessing is the first and crucial step in Natural Language Processing (NLP). It involves cleaning and structuring the text so that it can be effectively analyzed and processed by machine learning models.

#### **1.1 Tokenization**
Tokenization is the process of breaking down a text into individual words or sentences.

```python
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "The quick brown fox jumps over the lazy dog."

# Tokenization
doc = nlp(text)

# Word tokens
word_tokens = [token.text for token in doc]
print("Word Tokens:", word_tokens)

# Sentence tokens
sentence_tokens = [sent.text for sent in doc.sents]
print("Sentence Tokens:", sentence_tokens)
```

##### **Explanation**
- We load a pre-trained NLP model (`en_core_web_sm`) from spaCy.
- The `nlp(text)` processes the input text into a `doc` object.
- We extract **word tokens** (`token.text for token in doc`), which splits the text into words.
- We extract **sentence tokens** (`sent.text for sent in doc.sents`), which breaks the text into sentences.

#### **1.2 Stopword Removal**
Stopwords are common words (e.g., "is", "and", "the") that do not add much meaning to the text.

```python
# Stopword removal
filtered_tokens = [token.text for token in doc if not token.is_stop]
print("Tokens after Stopword Removal:", filtered_tokens)
```

##### **Explanation**
- We filter out tokens that are stopwords (`token.is_stop`).
- This helps reduce noise and improves efficiency in further processing.

#### **1.3 Lemmatization**
Lemmatization reduces words to their base form (e.g., "running" → "run").

```python
# Lemmatization
lemmatized_tokens = [token.lemma_ for token in doc]
print("Lemmatized Tokens:", lemmatized_tokens)
```

##### **Explanation**
- Lemmatization helps in standardizing words, which reduces redundancy and improves model accuracy.

---

### **Step 2: Text Representation**
Once the text is preprocessed, we need to convert it into a numerical form for analysis.

#### **2.1 TF-IDF (Term Frequency - Inverse Document Frequency)**
TF-IDF is a statistical measure that evaluates how important a word is in a document relative to a collection of documents.

```python
from sklearn.feature_extraction.text import TfidfVectorizer

# Example sentences
sentences = ["Machine learning is amazing.", "I love natural language processing."]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(sentences)

# Display TF-IDF scores
print("TF-IDF Matrix:\n", tfidf_matrix.toarray())
print("Vocabulary:", vectorizer.get_feature_names_out())
```

##### **Explanation**
- `TfidfVectorizer()` converts text into a matrix of TF-IDF features.
- `fit_transform(sentences)` computes the TF-IDF scores for the words in the input text.
- The resulting matrix represents the importance of words based on their frequency in the document.

---

### **Step 3: Summarization Process**
Text summarization is the process of shortening long pieces of text while preserving key information.

#### **3.1 Extractive Summarization (TextRank)**
Extractive summarization selects the most important sentences from the text.

```python
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import defaultdict
import heapq

# Input text
text = """
Machine learning is a branch of artificial intelligence that enables computers to learn from data. 
It is used in various applications such as image recognition, natural language processing, and recommendation systems. 
Deep learning, a subset of machine learning, uses neural networks to model complex patterns in data.
"""

# Process the text
doc = nlp(text)

# Build a word frequency dictionary
word_frequencies = defaultdict(int)
for word in doc:
    if word.text.lower() not in STOP_WORDS and word.text.lower() not in punctuation:
        word_frequencies[word.text.lower()] += 1

# Normalize word frequencies
max_frequency = max(word_frequencies.values())
for word in word_frequencies:
    word_frequencies[word] /= max_frequency

# Score sentences based on word frequencies
sentence_scores = defaultdict(int)
for sent in doc.sents:
    for word in sent:
        if word.text.lower() in word_frequencies:
            sentence_scores[sent] += word_frequencies[word.text.lower()]

# Extract top 2 sentences as summary
summary_sentences = heapq.nlargest(2, sentence_scores, key=sentence_scores.get)
summary = " ".join([sent.text for sent in summary_sentences])
print("Extractive Summary:\n", summary)
```

##### **Explanation**
- We calculate word frequencies, ignoring stopwords and punctuation.
- We normalize frequencies to prevent bias from common words.
- Sentences are scored based on the sum of their word frequencies.
- We extract the top-ranked sentences as the summary.

---

### **Step 4: Post-processing & Evaluation**
Post-processing refines the summary, and evaluation ensures its accuracy.

#### **4.1 Post-processing**
Grammar correction and redundancy removal improve readability.

```python
# Post-process the summary
processed_summary = nlp(summary)
print("Post-processed Summary:\n", processed_summary.text)
```

##### **Explanation**
- `nlp(summary)` ensures grammatical correctness.
- This step is essential for abstractive summarization.

#### **4.2 Evaluation Metrics**
ROUGE (Recall-Oriented Understudy for Gisting Evaluation) measures similarity between the generated and reference summaries.

```python
from rouge import Rouge

# Reference and generated summaries
reference = "Machine learning is a branch of AI that enables computers to learn."
generated = "Machine learning helps computers learn."

# Calculate ROUGE score
rouge = Rouge()
scores = rouge.get_scores(generated, reference)
print("ROUGE Scores:\n", scores)
```

##### **Explanation**
- **ROUGE-1**: Measures overlap of unigrams (single words).
- **ROUGE-2**: Measures overlap of bigrams (two consecutive words).
- **ROUGE-L**: Measures longest common subsequence.

---

### **Step 5: Applications**
For abstractive summarization, we use deep learning models like T5 or BART.

```python
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load pre-trained T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

# Input text
input_text = "Machine learning is a branch of artificial intelligence that enables computers to learn from data."

# Tokenize and generate summary
input_ids = tokenizer.encode("summarize: " + input_text, return_tensors="pt", max_length=512, truncation=True)
summary_ids = model.generate(input_ids, max_length=50, min_length=25, length_penalty=2.0, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("Abstractive Summary:\n", summary)
```

##### **Explanation**
- **T5 Model**: A transformer-based model designed for text generation.
- The model generates a new summary instead of extracting key sentences.
- **Beam search**: Optimizes generated text for quality.

---

### **Summary**
| Step | Process |
|------|---------|
| **Step 1: Data Preprocessing** | Tokenization, Stopword Removal, Lemmatization |
| **Step 2: Text Representation** | TF-IDF, Word Embeddings |
| **Step 3: Summarization** | Extractive (TextRank), Abstractive (T5) |
| **Step 4: Post-processing & Evaluation** | Grammar correction, ROUGE scores |
| **Step 5: Applications** | T5, BART, GPT-based summarization |

This guide covers both rule-based and deep learning approaches to text summarization. Let me know if you need more examples! 🚀
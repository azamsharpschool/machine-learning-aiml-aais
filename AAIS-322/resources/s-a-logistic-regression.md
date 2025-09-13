
## 🎬 Example: Movie Review Sentiment Analysis

### Step 1 – Install dependencies

```bash
pip install spacy scikit-learn
python -m spacy download en_core_web_sm
```

---

### Step 2 – Sample dataset

(You can replace this with real IMDB reviews, tweets, or product reviews.)

```python
reviews = [
    ("This movie was fantastic! I loved the story and the acting.", "positive"),
    ("Absolutely terrible. Worst film I’ve seen in years.", "negative"),
    ("Great performances and stunning visuals!", "positive"),
    ("I didn’t enjoy this movie. It was boring and too long.", "negative"),
    ("A masterpiece. Brilliantly directed and beautifully written.", "positive"),
    ("Waste of time. The plot made no sense.", "negative"),
]
```

---

### Step 3 – Preprocessing with spaCy

We’ll lemmatize (reduce words to base form) and remove stopwords.

```python
import spacy

nlp = spacy.load("en_core_web_sm")

def spacy_tokenizer(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc 
              if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

# Quick test
print(spacy_tokenizer("This movie was fantastic! I loved the story and the acting."))
```

✅ Output:

```
movie fantastic love story act
```

---

### Step 4 – Train a classifier

We’ll use **TF-IDF** (classic NLP feature extraction) + **Logistic Regression**.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Build pipeline: spaCy tokenizer → TF-IDF → Logistic Regression
model = Pipeline([
    ("tfidf", TfidfVectorizer(tokenizer=spacy_tokenizer)),
    ("clf", LogisticRegression())
])

# Train
X, y = zip(*reviews)
model.fit(X, y)
```

---

### Step 5 – Test it

```python
tests = [
    "What a wonderful movie! Brilliant acting and story.",
    "This was the worst waste of 2 hours. Absolutely dreadful.",
    "I liked some parts but overall it was too slow."
]

for t in tests:
    print(t, "->", model.predict([t])[0])
```

✅ Example Output:

```
What a wonderful movie! Brilliant acting and story. -> positive
This was the worst waste of 2 hours. Absolutely dreadful. -> negative
I liked some parts but overall it was too slow. -> negative
```

---

### Why this is practical

* Shows **text preprocessing** (spaCy).
* Applies **classic ML pipeline** (scikit-learn).
* Can easily scale with a bigger dataset.
* Real-world use: classify reviews, feedback, support tickets, tweets.


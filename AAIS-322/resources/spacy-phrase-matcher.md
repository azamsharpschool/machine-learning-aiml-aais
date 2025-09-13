
## 🔹 Example 1 – `Matcher` (pattern-based rules)

`Matcher` lets you define rules on **tokens** (words, lemmas, POS, etc.).

```python
import spacy
from spacy.matcher import Matcher

# Load English pipeline
nlp = spacy.load("en_core_web_sm")

# Initialize the matcher
matcher = Matcher(nlp.vocab)

# Example: find patterns like "buy iPhone" or "acquire company"
pattern = [
    {"LEMMA": {"IN": ["buy", "acquire"]}},  # first word must be "buy" or "acquire"
    {"POS": "PROPN", "OP": "+"}             # followed by one or more proper nouns
]

matcher.add("ACQUISITION_PATTERN", [pattern])

doc = nlp("Apple plans to acquire Beats. Google may buy DeepMind.")

matches = matcher(doc)
for match_id, start, end in matches:
    print("Matched:", doc[start:end].text)
```

**Output:**

```
Matched: acquire Beats
Matched: buy DeepMind
```

---

## 🔹 Example 2 – `PhraseMatcher` (dictionary of phrases)

`PhraseMatcher` is faster when you just want to detect **fixed phrases**.

```python
import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

# Initialize the PhraseMatcher
phrase_matcher = PhraseMatcher(nlp.vocab)

# List of phrases to look for
phrases = ["machine learning", "artificial intelligence", "natural language processing"]

# Convert phrases into spaCy docs
patterns = [nlp.make_doc(p) for p in phrases]

phrase_matcher.add("AI_TERMS", patterns)

doc = nlp("This course teaches machine learning and natural language processing.")

matches = phrase_matcher(doc)
for match_id, start, end in matches:
    print("Matched:", doc[start:end].text)
```

**Output:**

```
Matched: machine learning
Matched: natural language processing
```

---

👉 Think of it this way:

* **`Matcher`** = flexible, rule-based patterns (POS, lemma, attributes).
* **`PhraseMatcher`** = fast dictionary lookup for exact phrases.

---



---

## 🔹 Option 1: Use `EntityRuler` (best for fixed patterns/keywords)

If you want spaCy to always recognize certain words or phrases as entities, you can use the **EntityRuler**.
This is rule-based, so it’s easy and doesn’t require retraining.

```python
import spacy
from spacy.pipeline import EntityRuler

nlp = spacy.load("en_core_web_sm")

# Create EntityRuler and add to pipeline BEFORE ner
ruler = nlp.add_pipe("entity_ruler", before="ner")

# Add patterns (you can assign them to any label you want)
patterns = [
    {"label": "TECH", "pattern": "scikit-learn"},
    {"label": "TECH", "pattern": "SwiftUI"},
    {"label": "ORG", "pattern": "AzamSharp School"}
]
ruler.add_patterns(patterns)

doc = nlp("I am learning SwiftUI and scikit-learn with AzamSharp School.")

for ent in doc.ents:
    print(ent.text, ent.label_)
```

**Output:**

```
SwiftUI TECH
scikit-learn TECH
AzamSharp School ORG
```

👉 This is the easiest way to **add custom entities** without training.

---

## 🔹 Option 2: Add with `PhraseMatcher` + custom logic

If you don’t want to mess with the pipeline, you can use a `PhraseMatcher` and then create entities in code:

```python
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")

matcher = PhraseMatcher(nlp.vocab)
terms = ["FastAPI", "PyTorch", "Core ML"]
patterns = [nlp.make_doc(t) for t in terms]
matcher.add("TECH", patterns)

doc = nlp("We used FastAPI and Core ML for deployment.")

matches = matcher(doc)
new_ents = []
for match_id, start, end in matches:
    span = Span(doc, start, end, label="TECH")
    new_ents.append(span)

doc.ents = list(doc.ents) + new_ents

for ent in doc.ents:
    print(ent.text, ent.label_)
```

---

## 🔹 Option 3: Retrain the NER model (generalization)

If you want spaCy to **learn from examples** and generalize (e.g., recognizing *any* university name, not just “Harvard”), you need to **train** the `ner` component.

Steps:

1. Prepare **training data**: a list of `(text, {"entities": [(start, end, label)]})`.
2. Add new labels with `ner.add_label("MY_LABEL")`.
3. Update the pipeline with examples (`nlp.update`).

Training is more involved, but it’s powerful for broad categories.

---

✅ In summary:

* **EntityRuler** → best for fixed phrases/keywords.
* **PhraseMatcher + Span** → manual control, flexible.
* **NER retraining** → best if you need generalization to unseen data.


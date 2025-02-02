# **Step-by-Step Walkthrough: Named Entity Recognition (NER) Using spaCy**  

In this walkthrough, we will **use spaCy’s Named Entity Recognition (NER) model** to extract **people, organizations, dates, and products** from text. We will also **modify entity labels** and visualize the results using `displacy`.

---

## **Step 1: Install Required Libraries**
Ensure that `spaCy` and the **English language model** are installed.

```bash
pip install spacy
python -m spacy download en_core_web_sm
```

---

## **Step 2: Import Necessary Libraries**
```python
import spacy
```

---

## **Step 3: Load spaCy’s Pre-Trained NER Model**
We will use **`en_core_web_sm`**, a small but effective English NLP model.

```python
# Load spaCy model
nlp = spacy.load("en_core_web_sm")
```

---

## **Step 4: Extract Named Entities from Text**
We will analyze the following **example sentence**:

```python
text = "Steve Jobs and Tim Cook from Apple announced iPhone in 2007."
```

Pass the text through spaCy’s model:

```python
# Process text with spaCy NER
doc = nlp(text)

# Print named entities
for ent in doc.ents:
    print(ent.text, " | ", ent.label_, " | ", spacy.explain(ent.label_))
```

**Output:**
```
Steve Jobs  |  PERSON  |  People, including fictional
Tim Cook  |  PERSON  |  People, including fictional
Apple  |  ORG  |  Companies, agencies, institutions, etc.
iPhone  |  ORG  |  Companies, agencies, institutions, etc.
2007  |  DATE  |  Absolute or relative dates or periods
```

### **Observations:**
- The model correctly identifies **Steve Jobs** and **Tim Cook** as **persons**.
- **Apple** is classified as an **organization**.
- **iPhone** is incorrectly classified as an **organization** instead of a **product**.
- **2007** is correctly recognized as a **date**.

---

## **Step 5: View Supported Entity Labels**
```python
# List all entity labels recognized by the model
print(nlp.pipe_labels["ner"])
```

**Output:**
```
['CARDINAL', 'DATE', 'EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 'MONEY', 
 'NORP', 'ORDINAL', 'ORG', 'PERCENT', 'PERSON', 'PRODUCT', 'QUANTITY', 'TIME', 'WORK_OF_ART']
```
These are the **different entity types** that spaCy can recognize.

---

## **Step 6: Correcting Incorrect Entity Labels**
We noticed that **iPhone** was misclassified as an **organization** (`ORG`). Let’s manually **change its entity type** to **product** (`PRODUCT`).

```python
from spacy.tokens import Span

# Select the word "iPhone" in the document
word = doc[8:9]  # iPhone

# Check its type
print(type(word))  # Expected Output: spacy.tokens.span.Span

# Modify the entity label of "iPhone" to "PRODUCT"
span1 = Span(doc, 8, 9, label="PRODUCT")

# Update the document's entity list
doc.set_ents([span1], default="unmodified")

# Print entities after modification
for ent in doc.ents:
    print(ent.text, " | ", ent.label_, " | ", spacy.explain(ent.label_))
```

**Updated Output:**
```
Steve Jobs  |  PERSON  |  People, including fictional
Tim Cook  |  PERSON  |  People, including fictional
Apple  |  ORG  |  Companies, agencies, institutions, etc.
iPhone  |  PRODUCT  |  Objects, vehicles, foods, etc. (not services)
2007  |  DATE  |  Absolute or relative dates or periods
```

✅ Now **iPhone is correctly classified as a product!** 🎉

---

## **Step 7: Visualizing Named Entities**
To **highlight entities in a sentence**, we use **spaCy’s displaCy visualizer**.

```python
from spacy import displacy

# Render named entity visualization
displacy.render(doc, style="ent")
```

This will generate a **color-coded visualization** in a Jupyter Notebook.

Example output:
```
Steve Jobs PERSON and Tim Cook PERSON from Apple ORG announced iPhone PRODUCT in 2007 DATE .
```
Each entity is labeled with a distinct color.

---

## **Step 8: Save and Reuse the Model**
To **save the modified entity model** for future use:

```python
# Save the modified model
nlp.to_disk("modified_ner_model")

# Load it again
nlp2 = spacy.load("modified_ner_model")
print("Model loaded successfully!")
```

---

## **Next Steps**
- **Fine-tune the model** on custom datasets.
- **Train spaCy to recognize new entities**, such as **custom product names**.
- **Deploy the NER model** in a chatbot or **customer support** system.

This walkthrough provides a **simple but effective way to extract named entities from text** using **spaCy**! 🚀 Let me know if you have any questions!
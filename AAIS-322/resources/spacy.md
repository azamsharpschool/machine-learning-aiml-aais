Here’s a detailed step-by-step walkthrough for **Named Entity Recognition (NER) Using spaCy** with additional explanations, expected outputs, and best practices.

---

# **Step-by-Step Walkthrough: Named Entity Recognition (NER) Using spaCy**  

In this tutorial, we will **use spaCy’s Named Entity Recognition (NER) model** to extract **people, organizations, dates, and products** from text. We will also **modify entity labels** and visualize the results using `displacy`.

---

## **Step 1: Install Required Libraries**
### **Why is this needed?**
To use **spaCy** for Named Entity Recognition (NER), we need to install its core library and a pre-trained English language model.

### **Run the following command in your terminal:**
```bash
pip install spacy
python -m spacy download en_core_web_sm
```
- `spacy` is the main NLP library.
- `en_core_web_sm` is a **pre-trained** small English NLP model that supports tokenization, part-of-speech tagging, and NER.

---

## **Step 2: Import Necessary Libraries**
We need to import `spacy` before using its features.

```python
import spacy
```
- This will allow us to load the **spaCy model** and work with its built-in NLP capabilities.

---

## **Step 3: Load spaCy’s Pre-Trained NER Model**
Now, let’s load the **English language model**:

```python
nlp = spacy.load("en_core_web_sm")
```
- The **`nlp` object** processes text and applies **Named Entity Recognition** (NER).
- The model **automatically detects entities** like names, locations, and organizations.

---

## **Step 4: Extract Named Entities from Text**
### **Example Text**
We will analyze the following sentence:
```python
text = "Steve Jobs and Tim Cook from Apple announced iPhone in 2007."
```
### **Processing the Text**
```python
doc = nlp(text)

# Print named entities
for ent in doc.ents:
    print(ent.text, " | ", ent.label_, " | ", spacy.explain(ent.label_))
```

### **Expected Output**
```
Steve Jobs  |  PERSON  |  People, including fictional
Tim Cook  |  PERSON  |  People, including fictional
Apple  |  ORG  |  Companies, agencies, institutions, etc.
iPhone  |  ORG  |  Companies, agencies, institutions, etc.
2007  |  DATE  |  Absolute or relative dates or periods
```
### **Observations**
- ✅ `Steve Jobs` and `Tim Cook` are correctly classified as **PERSON**.
- ✅ `Apple` is correctly classified as an **ORG** (Organization).
- ❌ `iPhone` is incorrectly classified as an **ORG** instead of a **PRODUCT**.
- ✅ `2007` is correctly classified as a **DATE**.

---
## **Step 5: View Supported Entity Labels**
To check **all available entity labels**, run:

```python
print(nlp.pipe_labels["ner"])
```

### **Output:**
```
['CARDINAL', 'DATE', 'EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 'MONEY', 
 'NORP', 'ORDINAL', 'ORG', 'PERCENT', 'PERSON', 'PRODUCT', 'QUANTITY', 'TIME', 'WORK_OF_ART']
```
### **What do these labels mean?**
- `PERSON` → Names of people.
- `ORG` → Organizations.
- `PRODUCT` → Objects, vehicles, food, etc.
- `DATE` → Dates or time periods.

---

## **Step 6: Correcting Incorrect Entity Labels**
Since **iPhone** was misclassified as an **organization** (`ORG`), we will manually **change its entity type** to **PRODUCT**.

### **How to Fix Entity Labels in spaCy**
```python
from spacy.tokens import Span

# Select the word "iPhone" in the document
word = doc[8:9]  # iPhone

# Print its current entity type
print(type(word))  # Expected Output: <class 'spacy.tokens.span.Span'>

# Change "iPhone" from ORG to PRODUCT
span1 = Span(doc, 8, 9, label="PRODUCT")

# Update the document’s entity list
doc.set_ents([span1], default="unmodified")

# Print the updated entities
for ent in doc.ents:
    print(ent.text, " | ", ent.label_, " | ", spacy.explain(ent.label_))
```

### **Updated Output**
```
Steve Jobs  |  PERSON  |  People, including fictional
Tim Cook  |  PERSON  |  People, including fictional
Apple  |  ORG  |  Companies, agencies, institutions, etc.
iPhone  |  PRODUCT  |  Objects, vehicles, foods, etc. (not services)
2007  |  DATE  |  Absolute or relative dates or periods
```
✅ **Now, "iPhone" is correctly classified as a PRODUCT!** 🎉

---

## **Step 7: Visualizing Named Entities**
To **highlight entities in a sentence**, we use **spaCy’s displaCy visualizer**.

```python
from spacy import displacy

# Render named entity visualization
displacy.render(doc, style="ent")
```

### **How It Works**
- This will generate a **color-coded visualization** in a Jupyter Notebook.
- Each entity is labeled with a distinct color.

Example output:
```
Steve Jobs PERSON and Tim Cook PERSON from Apple ORG announced iPhone PRODUCT in 2007 DATE .
```

---

## **Step 8: Save and Reuse the Model**
To save the **updated NLP model** for future use:

```python
# Save the modified model
nlp.to_disk("modified_ner_model")

# Load the saved model
nlp2 = spacy.load("modified_ner_model")
print("Model loaded successfully!")
```

✅ **Now, we can reuse our modified entity recognizer anytime!** 🎯

---

## **Next Steps: Expanding Your NLP Model**
Here’s how you can **extend this project**:
1. **Fine-Tune the Model** 🏋️‍♂️  
   - Train spaCy’s model on a **custom dataset** to improve entity recognition.

2. **Recognizing New Entities** 🔍  
   - Teach spaCy to **identify product names, technical terms, or legal phrases**.

3. **Deploy the NER Model** 🌍  
   - Use this model in **chatbots, search engines, and customer support applications**.

---

## **Final Thoughts**
🎉 **Congratulations!** You’ve built a working **Named Entity Recognition (NER) system** using **spaCy**.

Now, you can:
- Extract structured **information from unstructured text**.
- **Modify entity labels** and improve accuracy.
- **Visualize named entities** for easier understanding.

🔹 **Want to go further?** Try training a **custom NER model** with your own dataset! 🚀

---

This detailed walkthrough ensures that **even beginners** can follow along while also providing deeper insights for those looking to expand their knowledge. Let me know if you need further clarifications! 😊
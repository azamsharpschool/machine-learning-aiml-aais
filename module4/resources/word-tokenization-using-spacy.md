
### **Exercise: Word Tokenization with spaCy**

**Objective:**  
Learn how to tokenize text into individual words using the spaCy library in Python.

**Prerequisites:**  
- Basic knowledge of Python programming
- Understanding of Natural Language Processing (NLP) concepts

**Setup:**  
Before you begin, ensure you have spaCy installed in your environment. You can install it using pip:

```bash
pip install spacy
```

Also, download the English model:

```bash
python -m spacy download en_core_web_sm
```

**Steps:**

1. **Import the spaCy library**  
   Start by importing the necessary spaCy module and loading the English language model:

   ```python
   import spacy

   # Load the English language model
   nlp = spacy.load('en_core_web_sm')
   ```

2. **Input Text**  
   Define a sample text for tokenization. You can start with a simple sentence:

   ```python
   text = "Hello, world! Welcome to the world of Natural Language Processing."
   ```

3. **Process the Text**  
   Pass the text through the spaCy language model to create a `Doc` object, which contains the processed text:

   ```python
   doc = nlp(text)
   ```

4. **Tokenize the Text**  
   Extract the tokens (words) from the `Doc` object and print them:

   ```python
   for token in doc:
       print(token.text)
   ```

   **Expected Output:**
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

5. **Challenge**  
   - **Handling Punctuation:** Modify the code to ignore punctuation marks when printing tokens. Hint: Use the `is_punct` attribute.
   - **Custom Text:** Try tokenizing a more complex paragraph or a different language. Load a different language model if necessary.
   - **Word Frequencies:** Count the frequency of each token in the text and display the results.

6. **Bonus Task**  
   Explore additional spaCy token attributes like `lemma_`, `is_stop`, or `pos_`, and print them alongside each token.

   ```python
   for token in doc:
       print(f"Token: {token.text}, Lemma: {token.lemma_}, POS: {token.pos_}, Is Stopword: {token.is_stop}")
   ```

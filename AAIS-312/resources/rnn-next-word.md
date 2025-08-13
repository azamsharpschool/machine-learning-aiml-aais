
```python
from transformers import pipeline

# Load GPT-2 text generation pipeline
generator = pipeline("text-generation", model="gpt2")

def predict_next_word(prompt):
    # Generate just enough tokens for ONE new word
    result = generator(
        prompt,
        max_new_tokens=1,           # instead of max_length, only add 1 token
        num_return_sequences=1,
        do_sample=False             # greedy pick (most likely word)
    )
    generated_text = result[0]['generated_text']
    
    # Extract only the part after the prompt
    next_part = generated_text[len(prompt):].strip()
    return next_part

# Example
prompt = "I was in the gym and then"
next_word = predict_next_word(prompt)
print(f"Prompt: {prompt}")
print(f"Next word: {next_word}")
```

---

Here’s a clear, line-by-line walkthrough of what your code does, plus a few gotchas and small improvements.

---

## What the code is doing

```python
from transformers import pipeline
```

* Imports Hugging Face’s high-level **`pipeline`** helper. It bundles a model + tokenizer + generation logic so you can call one function to get results.

```python
# Load GPT-2 text generation pipeline
generator = pipeline("text-generation", model="gpt2")
```

* Builds a **text-generation** pipeline using the pretrained **GPT-2** model.
* On the first run, it downloads the model and tokenizer (then caches them).
* `generator(...)` will: tokenize your prompt → run the model → decode tokens back to text.

```python
def predict_next_word(prompt):
    # Generate just enough tokens for ONE new word
    result = generator(
        prompt,
        max_new_tokens=1,           # instead of max_length, only add 1 token
        num_return_sequences=1,
        do_sample=False             # greedy pick (most likely word)
    )
    generated_text = result[0]['generated_text']
    
    # Extract only the part after the prompt
    next_part = generated_text[len(prompt):].strip()
    return next_part
```

* **`max_new_tokens=1`**: ask GPT-2 to append **exactly one token** to your prompt.

  * Important: a *token* is not always a whole word. With GPT-2’s byte-pair encoding, a single “word” may be split into multiple tokens (e.g., `"apples"` might become 2+ tokens). So this returns the *next token*, which often—but not always—looks like a whole word.
* **`num_return_sequences=1`**: return just one completion.
* **`do_sample=False`**: use **greedy decoding** (always choose the highest-probability token). If you set `do_sample=True` and add `temperature`/`top_k`/`top_p`, you’ll get more variety but less determinism.
* The pipeline returns a list of dicts like:

  ```python
  [{'generated_text': '<your prompt><new text>'}]
  ```
* You slice off the original prompt (`generated_text[len(prompt):]`) so only the new token remains, then `.strip()` to remove leading/trailing spaces or newlines.

```python
# Example
prompt = "I was in the gym and then"
next_word = predict_next_word(prompt)
print(f"Prompt: {prompt}")
print(f"Next word: {next_word}")
```

* Calls the function and prints the predicted **next token**.

---

## Why you sometimes won’t get a “whole word”

* GPT-2 uses **subword tokens**. The *first* token of a new word often includes a leading space (e.g., `" gym"`), and some words are split into multiple tokens (`"interestingly"` → `"interest"`, `"ingly"`).
* Because you only ask for **1 token**, you might get:

  * A full word (nice!),
  * A leading space + word fragment,
  * Just punctuation,
  * A fragment like `"ly"` or `"##ing"` (conceptually; GPT-2 doesn’t use `##` but the idea holds).

Your `.strip()` helps hide the leading space, but it doesn’t turn fragments into a full word.

---

## Small improvements (drop-in)

1. **Ask the pipeline to return only new text**
   You can skip manual slicing by setting `return_full_text=False`:

```python
generator = pipeline("text-generation", model="gpt2", return_full_text=False)
```

Then:

```python
generated_text = result[0]['generated_text']  # already just the new text
```

2. **Avoid pad warnings (GPT-2)**
   GPT-2 has no pad token; you may see a warning. You can set:

```python
generator.model.config.pad_token_id = generator.model.config.eos_token_id
```

3. **Make results reproducible**

```python
from transformers import set_seed
set_seed(42)
```

---

## If you truly want the **next whole word**

Keep generating tokens until you cross a word boundary (e.g., you’ve emitted at least one non-space token *and* then see a space/punctuation or the next token starts a new word). A simple, practical approach:

```python
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2", return_full_text=False)
generator.model.config.pad_token_id = generator.model.config.eos_token_id

def predict_next_whole_word(prompt, max_extra_tokens=5):
    text = ""
    for _ in range(max_extra_tokens):
        # add one token at a time
        out = generator(prompt + text, max_new_tokens=1, num_return_sequences=1, do_sample=False)
        piece = out[0]['generated_text']
        text += piece

        # stop if we just ended a word (space or punctuation seen)
        if piece.endswith((" ", ".", ",", "!", "?", ":", ";")) and text.strip():
            break

    return text.strip()

print(predict_next_whole_word("I was in the gym and then"))
```

* This remains greedy and short, but is more “word-like” to a user.

---

## Quick FAQ

* **Can I get multiple candidates?** Yes: set `num_return_sequences=5` and inspect each `['generated_text']`.
* **Can I make it more creative?** Set `do_sample=True`, add `temperature=0.8`, `top_p=0.9`, or `top_k=50`.
* **Is GPT-2 the best choice?** It’s fine for demos. For stronger predictions, use a larger model (e.g., `gpt2-medium`) or modern LLMs via APIs.

---

If you want, I can wrap this into a tiny function that returns the **top-k next-word candidates with probabilities**, so you can show a “predictive text” bar like on phones.


# 🌟 **LLM Introduction Walkthrough for Students (Google Colab Ready)**

### **Goal:** Learn how to interact with an LLM using simple code.

---

# 📘 **SECTION 1 — Install & Import Gemini (Simplest Way)**

> This requires an API key, but it is the easiest way to get high-quality results.

```python
!pip install -q google-generativeai

import google.generativeai as genai
```

---

# 📘 **SECTION 2 — Configure API Key**

Explain to students:
**The API key lets you talk to the LLM hosted on Google servers.**

```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```

(To avoid exposing your key, you can store it in an environment variable or use `input()`.)

---

# 📘 **SECTION 3 — List Available Models**

Explain: **LLMs come in different sizes and capabilities.**

```python
for m in genai.list_models():
    print(m.name)
```

Pick one:

```python
model = genai.GenerativeModel("gemini-2.5-flash")
```

---

# 📘 **SECTION 4 — Your First LLM Prompt**

Explain:

* You send **text in** (“prompt”)
* The LLM sends **text out** (“completion”)

```python
response = model.generate_content("Explain what machine learning is in simple terms.")
print(response.text)
```

Try modifying the question!

---

# 📘 **SECTION 5 — Creative Generation**

Example of creative writing:

```python
prompt = "Write a short story about a robot learning to cook."
print(model.generate_content(prompt).text)
```

Example of itinerary generation:

```python
print(model.generate_content("Give me a 1-day itinerary for Denver.").text)
```

---

# 📘 **SECTION 6 — Summarization**

Students paste long text → LLM → summary.

```python
text = """
Machine learning is a branch of artificial intelligence that...
"""

prompt = f"Summarize this text in 3 bullet points:\n\n{text}"
print(model.generate_content(prompt).text)
```

Great exercise:
**Have students summarize their lecture notes.**

---

# 📘 **SECTION 7 — Ask the LLM to Explain Code**

```python
code = """
def add(a, b):
    return a + b
"""

prompt = f"Explain what this Python function does:\n{code}"
print(model.generate_content(prompt).text)
```

Great for CS students.

---

# 📘 **SECTION 8 — Multi-Turn Chat (Conversation Mode)**

Explain: LLM remembers context within the session.

```python
chat = model.start_chat(history=[])

print(chat.send_message("Hi, you're my ML tutor! What is overfitting?").text)
print(chat.send_message("Give me an example with numbers.").text)
print(chat.send_message("Give me a quiz question about it.").text)
```

Students LOVE this part.

---

# 📘 **SECTION 9 — Controlling Creativity (Temperature)**

Explain:

* Low temp → factual, stable
* High temp → creative, random

```python
prompt = "Give me 3 startup ideas."

response = model.generate_content(
    prompt,
    generation_config={"temperature": 0.2}
)
print("Low temperature:\n", response.text)

response = model.generate_content(
    prompt,
    generation_config={"temperature": 1.2}
)
print("\nHigh temperature:\n", response.text)
```

This is an excellent discussion point.

---

# 📘 **SECTION 10 — OPTIONAL: Using an LLM Without an API Key (GPT-2)**

Explain: Some models can run locally because they’re small.

```python
!pip install transformers torch --quiet

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model2 = AutoModelForCausalLM.from_pretrained("gpt2")

inputs = tokenizer("What is AI?", return_tensors="pt")
outputs = model2.generate(**inputs, max_length=60)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

Students see the difference:

* **GPT-2 is older and weaker**
* **Modern models (Gemini) are far more capable**

This comparison gives them intuition.

---

# 📘 **SECTION 11 — A Mini Assignment (Optional)**

Have students do this:

### **Task**

Use LLM to create a structured 2-day travel itinerary **in JSON format**, then parse it and print each activity.

This combines:

* prompting
* JSON
* Python parsing

---

# 🌟 What Students Learn in This Walkthrough

✔ What an LLM is
✔ How to interact with it in Python
✔ Basic tasks: Q&A, summaries, creative writing
✔ Conversation memory
✔ Temperature & creativity
✔ Difference between local (GPT-2) and cloud (Gemini) LLMs
✔ Basic prompt engineering
✔ Practical understanding of LLM capabilities

---


# Exercise: English → Spanish Translator with Flask (Server-Side Rendered)

## Objective

Build a **server-side rendered (SSR)** Flask app that translates **English → Spanish** using Hugging Face `transformers` with `Helsinki-NLP/opus-mt-en-es`. All rendering must be done on the server. 

## Requirements

### 1) Routes & Rendering (SSR only)

* `GET /`

  * Render a page with a **textarea** for English input and a **Translate** button.
* `POST /`

  * Receive the textarea content, perform translation on the server, and **re-render the same page** with the Spanish output shown beneath the form.

### 2) Translation Logic

* Use `pipeline("translation_en_to_es", model="Helsinki-NLP/opus-mt-en-es")`.
* Initialize the pipeline **once at app startup** (not per request).

### 3) Validation & UX

* Handle empty input gracefully with a friendly message rendered server-side.
* Enforce a reasonable max length (e.g., 2,000 chars) and show a server-rendered error if exceeded.
* Use minimal CSS (inline or a small stylesheet) to keep the page readable.

### 6) Test Examples

* Input: `Good morning, how are you?`
  Output should include something close to: `Buenos días, ¿cómo estás?`

## Reference

You may use this guide for background and ideas:
**RNN Language Translation (GitHub)** — [https://github.com/azamsharpschool/machine-learning-aiml-aais/blob/main/AAIS-312/resources/rnn-language-translation.md](https://github.com/azamsharpschool/machine-learning-aiml-aais/blob/main/AAIS-312/resources/rnn-language-translation.md)

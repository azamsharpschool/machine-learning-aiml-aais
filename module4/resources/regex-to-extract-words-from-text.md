### Exercise: Extract Email Addresses from Text using Regex

#### Problem Description
Write a Python function called `extract_emails` that takes a string as input and returns a list of all email addresses found in the string. An email address is defined as a sequence of characters that includes an "@" symbol and a domain.

#### Input
- A single string `text` which may contain letters, numbers, spaces, punctuation, etc.

#### Output
- A list of strings, where each string is an email address extracted from the input text.

#### Example
```python
text = "Please contact us at support@example.com, sales@example.org or admin@example.net."

extract_emails(text)
```
Output:
```python
['support@example.com', 'sales@example.org', 'admin@example.net']
```

#### Instructions
1. Use the `re` module in Python to create a regular expression that matches email addresses.
2. Use the `findall` method of the `re` module to find all matches of the regex pattern in the input text.
3. Return the list of matched email addresses.

#### Solution Template
```python
import re

def extract_emails(text):
    # Your code here
    pass

# Test the function
text = "Please contact us at support@example.com, sales@example.org or admin@example.net."
print(extract_emails(text))  # Expected output: ['support@example.com', 'sales@example.org', 'admin@example.net']
```

### Explanation
- `r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'`: This regex pattern matches email addresses.
  - `[a-zA-Z0-9._%+-]+`: Matches the username part of the email address, which can include letters, digits, dots, underscores, percent signs, plus signs, and hyphens.
  - `@`: Matches the "@" symbol.
  - `[a-zA-Z0-9.-]+`: Matches the domain name part of the email address, which can include letters, digits, dots, and hyphens.
  - `\.[a-zA-Z]{2,}`: Matches the top-level domain (TLD), which must start with a dot and include at least two letters.
- `re.findall(pattern, text)`: This function returns a list of all non-overlapping matches of the pattern in the string `text`.

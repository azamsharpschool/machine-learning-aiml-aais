
### Exercise: Extract Order Number from Email using Regex

#### Problem Description
Write a Python function called `extract_order_number` that takes a string (representing an email) as input and returns the order number found in the string. The order number is represented in the format `#12345678`, where `#` is followed by a sequence of digits.

#### Input
- A single string `email` which may contain letters, numbers, spaces, punctuation, etc.

#### Output
- A string representing the order number extracted from the input text. If no order number is found, return `None`.

#### Example
```python
email = "Dear Customer, your order number #31886263 has been shipped. Thank you for shopping with us."

extract_order_number(email)
```
Output:
```python
'#31886263'
```

#### Instructions
1. Use the `re` module in Python to create a regular expression that matches the order number pattern.
2. Use the `search` method of the `re` module to find the order number in the input text.
3. If an order number is found, return it; otherwise, return `None`.

#### Solution Template
```python
import re

def extract_order_number(email):
    # Your code here
    pass

# Test the function
email = "Dear Customer, your order number #31886263 has been shipped. Thank you for shopping with us."
print(extract_order_number(email))  # Expected output: '#31886263'
```

### Explanation
- `r'#\d{8}'`: This regex pattern matches the order number format.
  - `#`: Matches the literal `#` character.
  - `\d{8}`: Matches exactly 8 digits.
- `re.search(pattern, email)`: This function searches for the pattern in the string `email` and returns a match object if the pattern is found, or `None` if it is not.

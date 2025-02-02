### **Step-by-Step Walkthrough: Extracting Order Number from an Email using Regex in Python**  

In this walkthrough, we will build a Python function that **extracts an order number** from an email using **regular expressions (regex)**.

---

## **Step 1: Install Required Libraries**
The `re` module is included in Python’s standard library, so no additional installation is needed.

```python
import re
```

---

## **Step 2: Understand the Problem**
We need to extract the **order number** from an email.  
The order number follows the **format `#12345678`**, where:
- `#` is a literal character.
- It is followed by exactly **8 digits**.

**Example Input:**
```python
email = "Dear Customer, your order number #31886263 has been shipped. Thank you for shopping with us."
```

**Expected Output:**
```
'#31886263'
```

---

## **Step 3: Define the Regular Expression**
Regular expressions help us identify patterns in text.  
We will use the following regex pattern:  

```python
r'#\d{8}'
```

### **Explanation:**
- `#` → Matches the literal `#` character.
- `\d{8}` → Matches **exactly 8 digits** (`\d` means a digit, `{8}` specifies 8 occurrences).

---

## **Step 4: Implement the Function**
We will:
1. **Use `re.search()`** to find the order number.
2. **Return the matched order number** if found.
3. **Return `None`** if no order number is found.

```python
import re

def extract_order_number(email):
    # Define the regex pattern
    pattern = r'#\d{8}'
    
    # Search for the pattern in the email
    match = re.search(pattern, email)
    
    # Return the matched order number if found, else return None
    return match.group() if match else None
```

---

## **Step 5: Test the Function**
```python
# Test Case 1: Email contains an order number
email1 = "Dear Customer, your order number #31886263 has been shipped. Thank you for shopping with us."
print(extract_order_number(email1))  # Expected Output: '#31886263'

# Test Case 2: Email does NOT contain an order number
email2 = "Hello, your package is on the way, but we could not find your order number."
print(extract_order_number(email2))  # Expected Output: None

# Test Case 3: Multiple order numbers (should return the first one)
email3 = "Your orders #12345678 and #87654321 are being processed."
print(extract_order_number(email3))  # Expected Output: '#12345678'

# Test Case 4: Order number with more than 8 digits (should not match)
email4 = "Here is your order number #1234567890."
print(extract_order_number(email4))  # Expected Output: None
```

---

## **Step 6: Save and Reuse the Function**
You can save the function in a Python file (`order_extraction.py`) and reuse it in your projects.

```python
# Save in order_extraction.py
def extract_order_number(email):
    pattern = r'#\d{8}'
    match = re.search(pattern, email)
    return match.group() if match else None
```

---

## **Next Steps**
- **Enhance the function** to extract multiple order numbers using `re.findall()`.
- **Use it in real-world applications**, such as:
  - Automating order processing for customer emails.
  - Extracting order details from customer support tickets.

This walkthrough provides a **simple but powerful solution** to **extracting structured information from text using regex**. 🚀 Let me know if you have any questions!
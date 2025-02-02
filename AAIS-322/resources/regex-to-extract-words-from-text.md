# **Step-by-Step Walkthrough: Extracting Email Addresses from Text using Python & Regex**

In this walkthrough, we will **write a Python function** to **extract email addresses** from a given text using **regular expressions (regex)**.

---

## **Step 1: Install Required Library**  
Python’s **re** module (Regular Expressions) is built-in, so there’s no need for installation. However, ensure you have Python installed.

```bash
pip install python
```

---

## **Step 2: Import Necessary Libraries**  
```python
import re
```
The **re module** in Python allows us to work with **regular expressions**, which help in **pattern matching** within text.

---

## **Step 3: Define the Problem Statement**  
We need to create a function **`extract_emails(text)`** that takes a **string** as input and returns **a list of email addresses** found in the text.

---

## **Step 4: Understand the Email Regex Pattern**
A valid **email address** consists of:
- A **username** (letters, numbers, dots, underscores, percent signs, plus signs, and hyphens)
- The **@ symbol**
- A **domain name** (letters, numbers, dots, and hyphens)
- A **top-level domain (TLD)** (e.g., `.com`, `.org`, `.net`)

### **Regular Expression for Email Matching**
```regex
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

### **Breaking Down the Regex Pattern**
| **Regex Part**        | **Meaning** |
|-----------------------|------------|
| `[a-zA-Z0-9._%+-]+`  | Matches the **username** (letters, digits, and special characters) |
| `@`                  | Matches the **@ symbol** |
| `[a-zA-Z0-9.-]+`     | Matches the **domain name** |
| `\.[a-zA-Z]{2,}`     | Matches the **TLD** (must have at least 2 letters) |

---

## **Step 5: Implement the Function**
Now, let’s write the **extract_emails** function using **re.findall()**, which returns all matches in the text.

```python
import re

def extract_emails(text):
    # Define the regex pattern for email addresses
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all email addresses in the text
    emails = re.findall(pattern, text)
    
    return emails
```

---

## **Step 6: Test the Function**
Let's check if our function correctly extracts emails.

```python
# Test Case
text = "Please contact us at support@example.com, sales@example.org or admin@example.net."

# Run function and print output
print(extract_emails(text))
```

**Expected Output:**
```python
['support@example.com', 'sales@example.org', 'admin@example.net']
```

---

## **Step 7: Handle Edge Cases**
Let’s test the function with more complex cases.

### **Test Case 1: Emails with Subdomains**
```python
text = "Reach us at info@mail.example.co.uk, team@company.org, and boss@office.com"
print(extract_emails(text))
```
✅ Expected Output:
```python
['info@mail.example.co.uk', 'team@company.org', 'boss@office.com']
```

---

### **Test Case 2: Emails Mixed with Other Text**
```python
text = "My email is john.doe@gmail.com, but you can also reach me at jane_doe@company.io."
print(extract_emails(text))
```
✅ Expected Output:
```python
['john.doe@gmail.com', 'jane_doe@company.io']
```

---

### **Test Case 3: No Email in Text**
```python
text = "This is a random sentence without an email."
print(extract_emails(text))
```
✅ Expected Output:
```python
[]
```

---

## **Step 8: Save the Extracted Emails to a File**
If we want to save the results to a text file:

```python
def save_emails_to_file(emails, filename="emails.txt"):
    with open(filename, "w") as file:
        for email in emails:
            file.write(email + "\n")
    print(f"Emails saved to {filename}")

# Example Usage
emails = extract_emails(text)
save_emails_to_file(emails)
```

---

## **Step 9: Next Steps**
✅ **Enhance the regex pattern** to handle more email formats.  
✅ **Use Named Groups** for more structured extraction.  
✅ **Build an API** that takes text input and returns extracted emails.  
✅ **Integrate it with Web Scraping** to extract emails from websites.  

---

### **Conclusion**
🎯 **You have successfully built a Python function to extract email addresses using regex!** 🚀
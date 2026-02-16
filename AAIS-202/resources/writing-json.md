

# 🟦 What Is JSON?

**JSON** stands for **JavaScript Object Notation**.

It’s just a way to store data in a structured format using:

* Curly braces `{}` → for objects (like dictionaries)
* Square brackets `[]` → for lists
* Key-value pairs → `"name": "Azam"`

Example JSON:

```json
{
  "name": "Azam",
  "age": 40,
  "isInstructor": true,
  "skills": ["Python", "Swift", "AI"]
}
```

In Python, this is basically a **dictionary**.

---

# 🟦 Step 1: Import the JSON Module

Python has a built-in module called `json`.

You must import it:

```python
import json
```

That’s it. No installation needed.

---

# 🟦 Step 2: Writing JSON to a File

Let’s say we want to store student data.

## Step 2.1: Create Python Data

```python
student = {
    "name": "Ali",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8,
    "courses": ["Python", "Data Structures", "AI"]
}
```

This is a normal Python dictionary.

---

## Step 2.2: Write It to a JSON File

```python
import json

student = {
    "name": "Ali",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8,
    "courses": ["Python", "Data Structures", "AI"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```

### 🔎 What’s happening?

* `"w"` → write mode (creates or overwrites file)
* `json.dump()` → writes Python data to JSON
* `indent=4` → makes file pretty and readable

---

## 📄 What Does student.json Look Like?

```json
{
    "name": "Ali",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8,
    "courses": [
        "Python",
        "Data Structures",
        "AI"
    ]
}
```

Nice and clean.

---

# 🟦 Step 3: Reading JSON From a File

Now let’s read it back into Python.

```python
import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
```

### 🔎 What’s happening?

* `"r"` → read mode
* `json.load()` → converts JSON file back into Python dictionary

---

## 🟢 Accessing Data

```python
print(data["name"])
print(data["gpa"])
print(data["courses"][0])
```

Output:

```
Ali
3.8
Python
```

Now it behaves exactly like a normal dictionary.

---

# 🟦 Step 4: Working With Lists of Objects

Often JSON stores multiple items.

## Writing Multiple Students

```python
students = [
    {"name": "Ali", "age": 22},
    {"name": "Sara", "age": 21},
    {"name": "John", "age": 23}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)
```

---

## Reading Them Back

```python
with open("students.json", "r") as file:
    students_data = json.load(file)

for student in students_data:
    print(student["name"])
```

Output:

```
Ali
Sara
John
```

---

# 🟦 Step 5: Common Beginner Mistakes

## ❌ Mistake 1: Using json.dumps instead of dump

* `dump()` → writes to file
* `dumps()` → returns JSON string

Example:

```python
json_string = json.dumps(student)
print(json_string)
```

This does NOT write to a file.

---

## ❌ Mistake 2: Forgetting to Open File in Write Mode

```python
open("file.json", "r")  # This won't allow writing
```

Use `"w"` for writing.

---

## ❌ Mistake 3: Invalid JSON Types

JSON supports:

* string
* number
* boolean
* list
* object
* null

JSON does NOT support:

* sets
* complex numbers
* custom classes

---

# 🟦 Real Beginner Practice Exercise

Try this:

1. Create a dictionary with:

   * name
   * age
   * favorite_color
   * hobbies (list)

2. Save it to `profile.json`

3. Read it back

4. Print only the hobbies

---

# 🟦 When Do We Use JSON?

* Storing configuration files
* Saving app data
* Sending data between frontend and backend
* APIs
* Machine learning datasets

JSON is everywhere.

---

# 🟦 Quick Summary

| Task                | Function       |
| ------------------- | -------------- |
| Write JSON          | `json.dump()`  |
| Read JSON           | `json.load()`  |
| Convert to string   | `json.dumps()` |
| Convert from string | `json.loads()` |


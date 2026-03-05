
# Assignment: Log File Analysis Using Regular Expressions

## Objective

In this assignment, you will use **Python and Regular Expressions (regex)** to analyze a **server log file**. Log files are commonly used in real systems to record events such as user logins, errors, and system activity.

You will write a Python program that **extracts useful information from a log file using regex patterns**.

---

# Step 1: Create the Log File

Create a file called:

```
server_log.txt
```

Paste the following log entries into the file:

```
2026-03-01 08:12:45 INFO User john logged in from 192.168.1.15
2026-03-01 08:14:10 ERROR Failed login attempt for user mike from 192.168.1.22
2026-03-01 08:15:02 INFO User sarah logged in from 192.168.1.18
2026-03-01 08:17:55 WARNING Disk space low on server01
2026-03-01 08:20:11 INFO User john logged out
2026-03-01 08:22:31 ERROR Database connection timeout
2026-03-01 08:25:17 INFO User david logged in from 192.168.1.35
2026-03-01 08:27:42 ERROR Failed login attempt for user mike from 192.168.1.22
2026-03-01 08:29:00 INFO User sarah logged out
```

---

# Step 2: Extract Information Using Regex

Write a Python program that reads the file and extracts the following information using **regular expressions**.

### 1️⃣ Extract all IP addresses

Example output:

```
192.168.1.15
192.168.1.22
192.168.1.18
192.168.1.35
```

---

### 2️⃣ Extract all usernames

Example output:

```
john
mike
sarah
david
```

---

### 3️⃣ Count how many ERROR messages appear

Example output:

```
Total Errors: 3
```

---

### 4️⃣ Count how many login attempts happened

Example output:

```
Total Login Attempts: 5
```

---

# Step 3: Save Results

Create a file called:

```
analysis.txt
```

Save the following information:

```
Unique Users:
john
mike
sarah
david

IP Addresses:
192.168.1.15
192.168.1.22
192.168.1.18
192.168.1.35

Total Errors: 3
```

---

# Example Regex Patterns Students Might Use

Extract IP addresses

```
\d+\.\d+\.\d+\.\d+
```

Extract usernames

```
User (\w+)
```

Extract error messages

```
ERROR
```

---

# HARD MODE (Optional)

Add the following features to your program:

### 1️⃣ Detect suspicious activity

Print any IP address that attempted **multiple failed logins**.

Example:

```
Suspicious Activity Detected:
192.168.1.22 attempted 2 failed logins
```

---

### 2️⃣ Extract timestamps

Regex example:

```
\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}
```




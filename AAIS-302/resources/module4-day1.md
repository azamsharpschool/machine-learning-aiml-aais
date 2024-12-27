### **Walkthrough: Real-World Scenario for Supervised Learning and Classification**

---

#### **Title:** Spam Email Classification  

**Objective:**  
Introduce the concept of supervised learning and classification by building a simple model to distinguish between spam and non-spam emails.

---

### **Scenario Description**

Imagine you're managing an email service and want to help users avoid spam. Using historical email data labeled as **"spam"** or **"not spam,"** you will train a supervised learning model to classify incoming emails into these two categories.

---

### **Step-by-Step Walkthrough**

---

#### **Step 1: Understanding the Dataset**

1. **Dataset Description:**
   - A dataset containing email content and labels:
     - **Feature:** Words or phrases in the email (e.g., "win," "free," "offer").
     - **Label:** "Spam" (1) or "Not Spam" (0).

2. **Example Data:**

| **Email Content**                   | **Label** |
|-------------------------------------|-----------|
| "Congratulations! You won a prize." | 1 (Spam)  |
| "Meeting scheduled for tomorrow."   | 0 (Not Spam) |
| "Claim your free gift now!"         | 1 (Spam)  |
| "Project update attached."          | 0 (Not Spam) |

---

#### **Step 2: Represent the Data**

1. Convert email content into numerical format using **Bag of Words** or **TF-IDF**:
   - Example:
     - Words: ["Congratulations", "won", "free", "meeting", "project"]
     - Email 1: [1, 1, 0, 0, 0] (contains "Congratulations" and "won").
     - Email 2: [0, 0, 0, 1, 0] (contains "meeting").

2. Use Python libraries like `sklearn` to preprocess the data:
   ```python
   from sklearn.feature_extraction.text import CountVectorizer
   
   # Example email data
   emails = [
       "Congratulations! You won a prize.",
       "Meeting scheduled for tomorrow.",
       "Claim your free gift now!",
       "Project update attached."
   ]
   labels = [1, 0, 1, 0]  # Spam or Not Spam
   
   # Convert text to numerical format
   vectorizer = CountVectorizer()
   X = vectorizer.fit_transform(emails)
   print(X.toarray())  # Numerical representation of emails
   ```

---

#### **Step 3: Train the Classification Model**

1. **Choose a Supervised Learning Algorithm:**
   - Use a simple classifier like Logistic Regression or Naive Bayes.

2. **Train the Model:**
   ```python
   from sklearn.model_selection import train_test_split
   from sklearn.naive_bayes import MultinomialNB
   
   # Split data into training and test sets
   X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)
   
   # Train the model
   model = MultinomialNB()
   model.fit(X_train, y_train)
   ```

---

#### **Step 4: Test and Evaluate the Model**

1. **Make Predictions:**
   ```python
   predictions = model.predict(X_test)
   ```

2. **Evaluate Accuracy:**
   ```python
   from sklearn.metrics import accuracy_score
   
   # Calculate accuracy
   accuracy = accuracy_score(y_test, predictions)
   print(f"Model Accuracy: {accuracy * 100:.2f}%")
   ```

3. **Discussion:**
   - What percentage of spam emails were correctly identified?  
   - How can the model be improved (e.g., more features, advanced algorithms)?

---

#### **Step 5: Real-World Application**

1. **Deploy the Model:**
   - Integrate the trained model into the email service.  
   - Automatically classify new emails as "spam" or "not spam."

2. **Discussion:**
   - Ask students where else classification models can be applied:
     - Detecting fake news.
     - Predicting whether a loan applicant will default.
     - Identifying tumors in medical images.

---

### **Wrap-Up**

- **Key Takeaways:**
  - Supervised learning uses labeled data to train models.  
  - Classification divides data into categories based on input features.  
  - Spam detection is a classic real-world example of supervised learning.  

- **Outcome:**  
  Students understand the basic workflow of supervised learning and how classification models can be applied to solve real-world problems.
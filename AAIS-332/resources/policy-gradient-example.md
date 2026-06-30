
```python
import random
import math

emails = ["Discount Coupon", "Free Shipping"]

# Policy preferences
preferences = {
    "Discount Coupon": 0.0,
    "Free Shipping": 0.0
}

learning_rate = 0.05


def softmax(prefs):
    total = sum(math.exp(v) for v in prefs.values())
    return {
        action: math.exp(value) / total
        for action, value in prefs.items()
    }


def choose_email(policy):
    r = random.random()

    if r < policy["Discount Coupon"]:
        return "Discount Coupon"
    return "Free Shipping"


for customer in range(20):

    policy = softmax(preferences)

    email = choose_email(policy)

    # Simulated customer response
    if email == "Discount Coupon":
        purchase = random.random() < 0.75
    else:
        purchase = random.random() < 0.35

    reward = 10 if purchase else -2

    # Policy Gradient update
    preferences[email] += learning_rate * reward

    print(f"Customer {customer + 1}")
    print(f"Email Sent: {email}")
    print(f"Purchased: {purchase}")
    print(f"Reward: {reward}")
    print(f"Current Policy: {softmax(preferences)}")
    print("-" * 40)
```

---

# Scenario

Imagine you work for an online shopping company.

Every time a customer visits your website, your AI must decide which promotion email to send.

It has two choices:

* **Discount Coupon**
* **Free Shipping**

Initially, the AI has **no idea** which promotion works better.

Its goal is to learn which promotion results in more purchases.

---

# Step 1: Import Libraries

```python
import random
import math
```

We need:

* **random** to simulate customers.
* **math** because Policy Gradient uses the exponential function when calculating probabilities.

---

# Step 2: Define Possible Actions

```python
emails = ["Discount Coupon", "Free Shipping"]
```

These are the actions.

Instead of moving left or right like Q-learning, our agent chooses which email to send.

```
Customer
    |
    V
+-------------------+
| Discount Coupon   |
| Free Shipping     |
+-------------------+
```

---

# Step 3: Policy Preferences

```python
preferences = {
    "Discount Coupon": 0.0,
    "Free Shipping": 0.0
}
```

This is **not** a Q-table.

It stores how much the AI currently prefers each action.

Initially

| Action          | Preference |
| --------------- | ---------: |
| Discount Coupon |          0 |
| Free Shipping   |          0 |

Since both are equal, neither action is preferred.

---

# Step 4: Learning Rate

```python
learning_rate = 0.05
```

This controls how quickly the AI changes its behavior.

Small learning rate

```
Old Preference
      |
      V
Small Change
```

Large learning rate

```
Old Preference
      |
      V
Big Jump
```

---

# Step 5: Convert Preferences into Probabilities

```python
def softmax(prefs):
```

This function converts preferences into probabilities.

Suppose

```
Discount Coupon = 2
Free Shipping = 1
```

Softmax converts them into something like

| Action          | Probability |
| --------------- | ----------: |
| Discount Coupon |         73% |
| Free Shipping   |         27% |

Notice

```
73% + 27% = 100%
```

The robot can now randomly choose according to these probabilities.

---

# Step 6: Choose an Email

```python
def choose_email(policy):
```

Suppose the policy is

```
Discount Coupon = 80%
Free Shipping = 20%
```

The algorithm generates

```python
r = random.random()
```

Example

```
r = 0.32
```

Since

```
0.32 < 0.80
```

it selects

```
Discount Coupon
```

If instead

```
r = 0.95
```

then

```
0.95 > 0.80
```

it selects

```
Free Shipping
```

Notice that **both actions are still possible**.

This exploration happens naturally.

---

# Step 7: Process Each Customer

```python
for customer in range(20):
```

Suppose we have 20 customers.

For every customer we repeat the same process.

```
Customer 1
↓

Customer 2
↓

Customer 3
↓

...
```

---

# Step 8: Calculate Current Policy

```python
policy = softmax(preferences)
```

Initially

Preferences

```
Discount Coupon = 0
Free Shipping = 0
```

Policy becomes

```
50%
50%
```

Later

Preferences

```
Discount Coupon = 5
Free Shipping = 1
```

Policy becomes

```
98%
2%
```

---

# Step 9: Choose Promotion

```python
email = choose_email(policy)
```

Suppose

```
Policy

Discount Coupon = 70%
Free Shipping = 30%
```

Most customers receive

```
Discount Coupon
```

but occasionally

```
Free Shipping
```

This is important because the AI continues exploring.

---

# Step 10: Simulate Customer Behavior

```python
if email == "Discount Coupon":
    purchase = random.random() < 0.75
else:
    purchase = random.random() < 0.35
```

This represents the environment.

If we send

```
Discount Coupon
```

there is a

```
75%
```

chance the customer buys something.

If we send

```
Free Shipping
```

only

```
35%
```

purchase.

We intentionally made one promotion better than the other.

The AI does **not** know this.

It must discover it.

---

# Step 11: Compute Reward

```python
reward = 10 if purchase else -2
```

If customer purchases

```
Reward = +10
```

Otherwise

```
Reward = -2
```

Example

| Email    | Purchased | Reward |
| -------- | --------- | -----: |
| Discount | Yes       |     10 |
| Discount | No        |     -2 |
| Shipping | Yes       |     10 |
| Shipping | No        |     -2 |

---

# Step 12: Policy Gradient Update

```python
preferences[email] += learning_rate * reward
```

This is the heart of Policy Gradient.

Suppose

Current preference

```
Discount Coupon = 2.0
```

Customer buys

```
Reward = 10
```

Learning rate

```
0.05
```

Update

```
2.0 + (0.05 × 10)

= 2.5
```

The preference increases.

Now Discount Coupon becomes more likely.

---

Suppose instead

```
Reward = -2
```

Then

```
2.0 + (0.05 × -2)

= 1.9
```

The preference decreases.

Now it becomes slightly less likely.

---

# Step 13: Print Results

```python
print(...)
```

Output might look like

```
Customer 1

Email:
Discount Coupon

Purchased:
True

Reward:
10

Policy

Discount Coupon 62%

Free Shipping 38%
```

Later

```
Customer 12

Discount Coupon

Purchased:
True

Reward:
10

Policy

Discount Coupon 91%

Free Shipping 9%
```

Eventually

```
Discount Coupon 98%

Free Shipping 2%
```

---

# What Is the Agent Actually Learning?

Notice that it never learns this:

| Action          | Value |
| --------------- | ----- |
| Discount Coupon | 8.2   |
| Free Shipping   | 4.1   |

That would be **Q-learning**.

Instead, it learns this:

| Action          | Probability |
| --------------- | ----------: |
| Discount Coupon |         98% |
| Free Shipping   |          2% |

It is directly learning the **policy**, which answers the question:

> "Given this situation, how likely should I be to choose each action?"

---

# Key Takeaway for Students

At the end of the lesson, emphasize the distinction:

| Q-Learning                                  | Policy Gradient                                                        |
| ------------------------------------------- | ---------------------------------------------------------------------- |
| Learns action values (Q-values)             | Learns action probabilities directly                                   |
| Chooses the action with the highest Q-value | Samples actions according to learned probabilities                     |
| Uses a Q-table or value function            | Uses a policy (often represented by probabilities or a neural network) |
| Answers: "How good is this action?"         | Answers: "How likely should I choose this action?"                     |

A good closing sentence is:

> **Policy Gradient does not try to estimate how valuable an action is. Instead, it directly learns how likely each action should be, increasing the probability of actions that lead to higher rewards and decreasing the probability of actions that lead to poorer outcomes.**

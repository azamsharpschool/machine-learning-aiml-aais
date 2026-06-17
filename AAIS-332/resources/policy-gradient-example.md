For high school students, I would avoid the actual policy gradient math and focus on the core idea:

> Instead of learning how good an action is (Q-Learning), Policy Gradient learns the probability of taking an action.

A simple example is a **robot choosing between two doors**.

### Scenario

A robot sees two doors:

```text
Door A
Door B
```

One door contains candy.

```text
Door A = No Candy
Door B = Candy
```

Initially, the robot chooses randomly.

```text
Door A = 50%
Door B = 50%
```

If the robot finds candy, it becomes more likely to choose that door in the future.

---

### Code Example

```python
import random

# Initial policy
prob_door_a = 0.5
prob_door_b = 0.5

learning_rate = 0.05

for episode in range(100):

    # Choose a door based on probabilities
    choice = random.choices(
        ["A", "B"],
        weights=[prob_door_a, prob_door_b]
    )[0]

    # Door B always has candy
    if choice == "B":
        reward = 1
    else:
        reward = 0

    # Update policy
    if reward == 1:
        prob_door_b += learning_rate
        prob_door_a -= learning_rate

    # Keep probabilities valid
    prob_door_a = max(0.01, prob_door_a)
    prob_door_b = min(0.99, prob_door_b)

print("Final Policy")
print(f"Door A: {prob_door_a:.2f}")
print(f"Door B: {prob_door_b:.2f}")
```

### What Students Should Learn

#### Policy

A policy is simply a strategy.

Initially:

```text
Choose Door A: 50%
Choose Door B: 50%
```

This is the robot's policy.

#### Reward

If the robot chooses Door B:

```text
Reward = 1
```

Otherwise:

```text
Reward = 0
```

#### Learning

When the robot gets a reward, it increases the probability of choosing that door again.

```python
prob_door_b += learning_rate
prob_door_a -= learning_rate
```

Over time:

```text
Door A = 10%
Door B = 90%
```

The robot has learned:

> Door B is usually the better choice.

---

### Connection to Policy Gradient

Q-Learning learns:

```text
How good is an action?
```

Policy Gradient learns:

```text
What is the probability of taking an action?
```

For high school students, this is usually the easiest way to explain the difference:

* **Q-Learning** keeps score for actions.
* **Policy Gradient** directly improves the strategy for choosing actions.

That single idea is enough for an introductory Day 3 lesson before introducing neural networks or gradient calculations.

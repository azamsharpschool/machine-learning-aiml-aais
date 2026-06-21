
``` py
import random

# Positions: 0 1 2 3 4
# Goal is position 4
position = 0
goal = 4

# Possible actions
actions = ["left", "right"]

# One episode with a maximum of 10 steps
for step in range(10):
    # Agent randomly chooses an action
    action = random.choice(actions)

    # Update position based on action
    if action == "right":
        position += 1
    else:
        position -= 1

    # Keep agent inside the environment
    position = max(0, min(position, goal))

    # Give reward
    reward = 10 if position == goal else -1

    # Show what happened
    print(f"Step: {step}, Action: {action}, Position: {position}, Reward: {reward}")

    # End episode if goal is reached
    if position == goal:
        print("Goal reached!")
        break

```

# Step 1: Import the Random Module

```python
import random
```

We need a way for the agent to make random decisions.

At this point, the agent does not know anything about the environment, so it will randomly choose actions.

---

# Step 2: Define the Environment

```python
# Positions: 0 1 2 3 4
# Goal is position 4
position = 0
goal = 4
```

Imagine a hallway with five locations:

```text
[0] [1] [2] [3] [4]
                 ^
               Goal
```

The agent starts at position `0`.

```text
A   _   _   _   G
```

Where:

* A = Agent
* G = Goal

This hallway is the **environment**.

In Reinforcement Learning terminology:

* Environment = the world
* State = where the agent currently is

Initially:

```python
position = 0
```

So the current state is `0`.

---

# Step 3: Define Possible Actions

```python
actions = ["left", "right"]
```

The agent has only two choices:

* Move left
* Move right

In RL terminology:

**Action Space**

```text
Action Space = {left, right}
```

---

# Step 4: Begin the Episode

```python
for step in range(10):
```

An episode is one attempt to reach the goal.

We allow at most 10 moves.

```text
Episode
 ├─ Step 0
 ├─ Step 1
 ├─ Step 2
 └─ ...
```

---

# Step 5: Choose an Action

```python
action = random.choice(actions)
```

The agent randomly chooses:

```text
left
or
right
```

Suppose it chooses:

```python
right
```

---

# Step 6: Update the State

```python
if action == "right":
    position += 1
else:
    position -= 1
```

If the agent moves right:

```text
Before: position = 0
After : position = 1
```

Visualization:

```text
Before

A  _  _  _  G

After

_  A  _  _  G
```

The state changed from:

```text
State 0 → State 1
```

This is called a **state transition**.

---

# Step 7: Keep the Agent Inside the World

```python
position = max(0, min(position, goal))
```

Without this line, the agent could move outside the hallway.

Example:

```python
position = -1
```

would be invalid.

This line forces:

```text
Minimum = 0
Maximum = 4
```

Examples:

```python
position = -1
```

becomes

```python
position = 0
```

and

```python
position = 5
```

becomes

```python
position = 4
```

---

# Step 8: Calculate Reward

```python
reward = 10 if position == goal else -1
```

This is the most important part of Reinforcement Learning.

Reward tells the agent whether it did something good or bad.

If it reaches the goal:

```python
reward = 10
```

Otherwise:

```python
reward = -1
```

Example:

Position = 2

```text
Reward = -1
```

Position = 4

```text
Reward = +10
```

Why a negative reward?

Because we want the agent to find the goal quickly.

Every extra move costs:

```text
-1
```

---

# Step 9: Display What Happened

```python
print(
    f"Step: {step}, Action: {action}, Position: {position}, Reward: {reward}"
)
```

Example output:

```text
Step: 0, Action: right, Position: 1, Reward: -1
Step: 1, Action: right, Position: 2, Reward: -1
Step: 2, Action: left, Position: 1, Reward: -1
Step: 3, Action: right, Position: 2, Reward: -1
```

This lets us observe the agent interacting with the environment.

---

# Step 10: Check for Success

```python
if position == goal:
    print("Goal reached!")
    break
```

If the agent reaches position 4:

```text
_  _  _  _  A
```

it receives:

```text
Reward = +10
```

and the episode ends.

Output:

```text
Step: 6, Action: right, Position: 4, Reward: 10
Goal reached!
```

---

# Mapping to Reinforcement Learning Concepts

| RL Concept  | Example in Code                       |
| ----------- | ------------------------------------- |
| Agent       | The player moving through the hallway |
| Environment | Positions 0–4                         |
| State       | Current position                      |
| Action      | left or right                         |
| Reward      | +10 or -1                             |
| Policy      | Currently random choices              |
| Episode     | One run of the loop                   |
| Goal        | Reach position 4                      |

---

# What Is Missing?

This example is **not learning yet**.

The agent:

```python
action = random.choice(actions)
```

always chooses randomly.

A true RL algorithm like:

* Q-Learning
* SARSA
* Deep Q Networks (DQN)

would remember past rewards and gradually learn:

```text
From position 0 → go right
From position 1 → go right
From position 2 → go right
From position 3 → go right
```

so that it reaches the goal efficiently.


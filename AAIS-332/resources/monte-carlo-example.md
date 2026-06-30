### Monte Carlo Mouse and Cheese Example – Code Walkthrough


# Step 1: Import Random Module

```python
import random
```

We import Python's `random` module so the mouse can make random decisions.

Without randomness, the mouse would always do the same thing and would never explore different paths.

---

# Step 2: Define the Goal

```python
goal = 4
```

Our world contains 5 positions:

```text
0    1    2    3    4
🐭   _    _    _    🧀
```

Position 4 contains the cheese.

The mouse starts at position 0.

---

# Step 3: Initialize Learning Storage

```python
action_scores = {
    "left": 0,
    "right": 0
}
```

This dictionary stores what the mouse has learned.

Initially:

```text
left  = 0
right = 0
```

The mouse has no idea whether moving left or right is better.

---

# Step 4: Run Multiple Episodes

```python
for episode in range(10):
```

The mouse will play 10 complete games.

An **episode** is one complete attempt to find the cheese.

```text
Episode 1
Episode 2
Episode 3
...
Episode 10
```

Learning occurs across episodes.

---

# Step 5: Start a New Episode

```python
position = 0
actions_taken = []
rewards = []
```

At the beginning of each episode:

The mouse returns to the starting position.

```text
🐭 _ _ _ 🧀
```

We also clear previous actions and rewards.

---

# Step 6: Maximum of 10 Steps

```python
for step in range(10):
```

Each episode can contain at most 10 moves.

This prevents the mouse from wandering forever.

---

# Step 7: Exploration Phase

```python
if episode < 3:
    action = random.choice(["left", "right"])
```

For the first three episodes, the mouse explores randomly.

Possible actions:

```text
left
right
```

The purpose is to gather experience.

Think of a child trying different routes to school before learning the best one.

---

# Step 8: Exploitation Phase

```python
else:
    if action_scores["right"] >= action_scores["left"]:
        action = "right"
    else:
        action = "left"
```

After the first three episodes, the mouse starts using what it learned.

Example:

```python
{
    "left": -15,
    "right": 28
}
```

Since:

```text
28 > -15
```

the mouse chooses:

```python
action = "right"
```

This is called **exploitation**.

---

# Step 9: Remember the Action

```python
actions_taken.append(action)
```

Every action is stored.

Example:

```python
["right", "right", "left", "right"]
```

Later, Monte Carlo learning will review these actions.

---

# Step 10: Move the Mouse

```python
if action == "right":
    position += 1
else:
    position -= 1
```

Examples:

```text
Position 0 + right = Position 1

Position 1 + right = Position 2

Position 2 + left = Position 1
```

---

# Step 11: Stay Inside the World

```python
position = max(0, min(position, goal))
```

This keeps the mouse within valid positions.

Examples:

```text
Position -1 becomes 0

Position 5 becomes 4
```

The mouse cannot leave the world.

---

# Step 12: Calculate Reward

```python
reward = 10 if position == goal else -1
```

If the mouse reaches the cheese:

```text
Reward = 10
```

Otherwise:

```text
Reward = -1
```

This encourages finding the cheese quickly.

---

# Step 13: Store Reward

```python
rewards.append(reward)
```

Example:

```python
[-1, -1, -1, 10]
```

These rewards describe the episode.

---

# Step 14: Draw the Environment

```python
world = ["_"] * 5
world[goal] = "🧀"
world[position] = "🐭"
```

Suppose:

```python
position = 2
```

The output becomes:

```text
_ _ 🐭 _ 🧀
```

This visualizes the mouse's location.

---

# Step 15: Display Current Step

```python
print(f"Step: {step}, Action: {action}, Reward: {reward}")
```

Example output:

```text
Step: 2, Action: right, Reward: -1
```

Students can see exactly what happened.

---

# Step 16: End Episode When Cheese Is Found

```python
if position == goal:
    print("🐭 Found the cheese!")
    break
```

If the mouse reaches the cheese:

```text
🐭 _ _ _ 🧀
```

the episode immediately ends.

---

# Step 17: Monte Carlo Evaluation

This is the most important part.

```python
total_reward = sum(rewards)
```

Suppose:

```python
rewards = [-1, -1, -1, 10]
```

Then:

```python
total_reward = 7
```

This evaluates the entire episode.

Monte Carlo waits until the episode is finished before learning.

---

# Step 18: Review the Episode

```python
print(f"Actions Taken: {actions_taken}")
print(f"Rewards: {rewards}")
print(f"Total Reward: {total_reward}")
```

Example:

```text
Actions Taken:
['right', 'right', 'right', 'right']

Rewards:
[-1, -1, -1, 10]

Total Reward:
7
```

Now we can judge whether the episode was successful.

---

# Step 19: Learn From the Episode

```python
for action in actions_taken:
    action_scores[action] += total_reward
```

Suppose:

```python
actions_taken = ["right", "right", "right", "right"]
total_reward = 7
```

Then:

```text
right += 7
right += 7
right += 7
right += 7
```

Result:

```python
{
    "left": 0,
    "right": 28
}
```

The mouse begins to associate moving right with successful outcomes.

---

# Step 20: Display Learned Knowledge

```python
print("Learned Scores:", action_scores)
```

Example:

```python
{
    "left": -12,
    "right": 35
}
```

This represents what the mouse has learned from previous episodes.

---

# Step 21: Final Knowledge

```python
print(action_scores)
```

Possible output:

```python
{
    "left": -43,
    "right": 126
}
```

The mouse has learned that moving right generally leads to better rewards.

---

# The Big Picture

The algorithm follows this cycle:

```text
Start Episode
      ↓
Take Actions
      ↓
Collect Rewards
      ↓
Episode Ends
      ↓
Calculate Total Reward
      ↓
Update Knowledge
      ↓
Use Knowledge in Future Episodes
```

This is the central idea behind Monte Carlo learning:


```python
import random

goal = 4
actions = ["left", "right"]

# Q-table: each position has scores for each action
q_table = {
    0: {"left": 0, "right": 0},
    1: {"left": 0, "right": 0},
    2: {"left": 0, "right": 0},
    3: {"left": 0, "right": 0},
    4: {"left": 0, "right": 0}
}

learning_rate = 0.1   # alpha
discount = 0.9        # gamma
epsilon = 0.3         # exploration chance

for episode in range(10):

    print(f"\n=== Episode {episode + 1} ===")

    position = 0

    for step in range(10):

        # Exploration vs exploitation
        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            action = max(q_table[position], key=q_table[position].get)

        old_position = position

        if action == "right":
            position += 1
        else:
            position -= 1

        position = max(0, min(position, goal))

        reward = 10 if position == goal else -1

        old_q = q_table[old_position][action]

        best_future_q = max(q_table[position].values())

        new_q = old_q + learning_rate * (
            reward + discount * best_future_q - old_q
        )

        q_table[old_position][action] = new_q

        world = ["_"] * 5
        world[goal] = "🧀"
        world[position] = "🐭"

        print(" ".join(world))
        print(f"Step: {step}")
        print(f"State: {old_position}")
        print(f"Action: {action}")
        print(f"Next State: {position}")
        print(f"Reward: {reward}")
        print(f"Old Q: {old_q:.2f}")
        print(f"Best Future Q: {best_future_q:.2f}")
        print(f"New Q: {new_q:.2f}")
        print()

        if position == goal:
            print("Cheese was found.")
            break

print("\n=== Final Q-Table ===")
for state, actions in q_table.items():
    print(f"State {state}: {actions}")
```

Main change:

```python
action_scores[action] += total_reward
```

became:

```python
q_table[old_position][action] = new_q
```

So now the agent is not just learning:

```text
left is good
right is good
```

It is learning:

```text
At position 0, left/right has this value
At position 1, left/right has this value
At position 2, left/right has this value
```

That is the key difference.


# Q-Learning Code Walkthrough

## Step 1: Define the Environment

```python
goal = 4
actions = ["left", "right"]
```

We create a simple one-dimensional world with five positions (0–4). The mouse starts at position 0 and tries to reach the cheese located at position 4.

The mouse has only two possible actions:

* Move left
* Move right

---

## Step 2: Create the Q-Table

```python
q_table = {
    0: {"left": 0, "right": 0},
    1: {"left": 0, "right": 0},
    2: {"left": 0, "right": 0},
    3: {"left": 0, "right": 0},
    4: {"left": 0, "right": 0}
}
```

The Q-table is the agent's memory.

Each row represents a state (position), and each column represents an action.

Initially, every value is zero because the mouse has never explored the environment.

For example,

```text
State 2

Left  = 0
Right = 0
```

means the mouse currently believes both actions are equally good because it has no experience.

---

## Step 3: Learning Parameters

```python
learning_rate = 0.1
discount = 0.9
epsilon = 0.3
```

These values control how the agent learns.

* **learning_rate (α)** determines how much new information influences the current Q-value.
* **discount (γ)** determines how much future rewards are valued.
* **epsilon (ε)** controls exploration. With a 30% probability, the mouse will randomly explore instead of choosing the best-known action.

---

## Step 4: Run Multiple Episodes

```python
for episode in range(10):
```

An episode is one complete attempt to find the cheese.

At the beginning of every episode, the mouse starts from the beginning of the world.

However, the Q-table is **not reset**.

The mouse remembers everything it learned in previous episodes.

---

## Step 5: Start at the Beginning

```python
position = 0
```

Every episode begins with the mouse at position 0.

Initially, it does not know the best path.

---

## Step 6: Exploration vs. Exploitation

```python
if random.random() < epsilon:
    action = random.choice(actions)
else:
    action = max(q_table[position], key=q_table[position].get)
```

This is one of the most important parts of Q-Learning.

The agent has two choices.

**Exploration**

The mouse tries a random action to discover new possibilities.

**Exploitation**

The mouse uses what it has already learned by selecting the action with the highest Q-value.

For example, suppose the Q-table contains

```text
State 2

Left  = 3
Right = 8
```

The mouse will choose **Right** because 8 is greater than 3.

---

## Step 7: Save the Current State

```python
old_position = position
```

Before moving, we save the current position.

This is important because we must update the Q-value associated with the state where the action started.

---

## Step 8: Move the Mouse

```python
if action == "right":
    position += 1
else:
    position -= 1
```

The mouse performs the selected action.

If it chooses Right, it moves one position to the right.

If it chooses Left, it moves one position to the left.

---

## Step 9: Keep the Mouse Inside the World

```python
position = max(0, min(position, goal))
```

This prevents the mouse from moving outside the environment.

If it attempts to move beyond either end of the world, it remains at the boundary.

---

## Step 10: Assign a Reward

```python
reward = 10 if position == goal else -1
```

The reward tells the mouse how well it performed.

* Reaching the cheese gives a reward of +10.
* Every other move gives a reward of -1.

The negative reward encourages the mouse to find the shortest path instead of wandering around.

---

## Step 11: Read the Current Q-Value

```python
old_q = q_table[old_position][action]
```

Before updating, we retrieve the current Q-value.

For example,

```text
Q(State 2, Right) = 4
```

This represents the mouse's current estimate of how valuable that action is.

---

## Step 12: Look Ahead

```python
best_future_q = max(q_table[position].values())
```

This is the Bellman idea.

After arriving at the next state, the mouse asks:

> "What is the best action I know from here?"

Suppose the next state's Q-values are

```text
Left  = 2
Right = 8
```

The best future value is

```text
max(2, 8) = 8
```

The agent assumes it will make the best possible decision from the next state onward.

---

## Step 13: Update the Q-Value

```python
new_q = old_q + learning_rate * (
    reward + discount * best_future_q - old_q
)
```

This is the Q-Learning update rule.

The agent combines:

* The reward it just received.
* The best future reward it currently knows about.
* Its previous estimate.

Instead of replacing the old value, the learning rate gradually adjusts it toward the new estimate.

Over many episodes, these values become more accurate.

---

## Step 14: Store the Updated Value

```python
q_table[old_position][action] = new_q
```

The updated Q-value is written back into the Q-table.

This is the learning step.

Each time the mouse moves, it slightly improves its understanding of the environment.

---

## Step 15: Display the World

```python
world = ["_"] * 5
world[goal] = "🧀"
world[position] = "🐭"
```

This creates a simple visualization showing where the mouse and the cheese are located after each move.

Students can watch the mouse explore the environment while the Q-table changes.

---

## Step 16: Stop When the Goal Is Reached

```python
if position == goal:
    break
```

Once the mouse reaches the cheese, the episode ends.

A new episode then begins, but the Q-table remains intact.

The mouse continues learning from all previous experiences.

---

## Step 17: Print the Final Q-Table

```python
for state, actions in q_table.items():
    print(f"State {state}: {actions}")
```

After several episodes, the Q-table contains the agent's learned knowledge.

A typical result might look like:

```text
State 0: Left=-2.3  Right=4.6
State 1: Left=0.5   Right=6.2
State 2: Left=2.1   Right=8.0
State 3: Left=5.4   Right=10.0
```

Notice that the values for moving right become larger as the mouse gets closer to the cheese.

This happens because the reward gradually propagates backward through the Q-table over multiple episodes.

The agent does not memorize the path. Instead, it learns the quality of each action in every state, and the optimal path naturally emerges by repeatedly choosing the highest-valued action.

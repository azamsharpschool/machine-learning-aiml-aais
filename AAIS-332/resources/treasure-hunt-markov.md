### Grid World Reinforcement Learning Example

The following example demonstrates the core concepts of reinforcement learning using a simple grid world environment.

### Full Code

```python
import random

grid = [
    ["S", ".", ".", "."],
    [".", "X", ".", "."],
    [".", ".", ".", "T"]
]

start_state = (0, 0)
treasure_state = (2, 3)
wall_state = (1, 1)

actions = ["up", "down", "left", "right"]

def step(state, action):
    row, col = state

    if action == "up":
        next_state = (row - 1, col)
    elif action == "down":
        next_state = (row + 1, col)
    elif action == "left":
        next_state = (row, col - 1)
    elif action == "right":
        next_state = (row, col + 1)

    next_row, next_col = next_state

    # Check if move is outside the grid
    if next_row < 0 or next_row >= 3 or next_col < 0 or next_col >= 4:
        return state, -5, False

    # Check if move hits the wall
    if next_state == wall_state:
        return state, -5, False

    # Check if treasure is found
    if next_state == treasure_state:
        return next_state, 10, True

    # Normal move
    return next_state, -1, False


state = start_state
done = False
total_reward = 0

while not done:
    action = random.choice(actions)
    next_state, reward, done = step(state, action)

    print(
        f"State: {state}, "
        f"Action: {action}, "
        f"Reward: {reward}, "
        f"Next State: {next_state}"
    )

    total_reward += reward
    state = next_state

print(f"\nEpisode Finished!")
print(f"Total Reward: {total_reward}")
```

---

## The Environment

```text
S  .  .  .
.  X  .  .
.  .  .  T
```

* **S** = Starting position
* **T** = Treasure
* **X** = Wall
* **.** = Empty space

The goal is for the agent to find the treasure while collecting the highest possible reward.

---

## States

A state represents the agent's current location.

```python
state = (0, 0)
```

In this example, each state is represented as:

```text
(row, column)
```

Examples:

```python
(0, 0)  # Start
(1, 2)  # Middle of grid
(2, 3)  # Treasure
```

---

## Actions

The agent can choose one of four actions:

```python
actions = ["up", "down", "left", "right"]
```

These actions allow the agent to move through the environment.

---

## Rewards

The environment provides feedback through rewards.

| Event             | Reward |
| ----------------- | ------ |
| Reach treasure    | +10    |
| Valid move        | -1     |
| Hit wall          | -5     |
| Move outside grid | -5     |

The objective of reinforcement learning is to maximize the total reward collected during an episode.

---

## The Step Function

```python
next_state, reward, done = step(state, action)
```

The `step()` function represents the environment.

Given:

```python
state
action
```

it returns:

```python
next_state
reward
done
```

This is the interaction loop used in almost every reinforcement learning environment.

---

## Markov Principle

This example satisfies the Markov Principle.

The next state depends only on:

```python
current_state
current_action
```

For example:

```python
state = (1, 2)
action = "right"
```

The result will always be the same regardless of how the agent arrived at `(1, 2)`.

The environment does not need to know:

* Previous states
* Previous rewards
* Previous actions

This is the key idea behind Markov Decision Processes (MDPs).

---

## Episode

An episode begins at:

```python
start_state = (0, 0)
```

and ends when:

```python
treasure_state = (2, 3)
```

is reached.

The loop continues until:

```python
done == True
```

At that point, the total reward for the episode is displayed.

---

## Key Reinforcement Learning Concepts Demonstrated

This small example introduces the most important reinforcement learning concepts:

* **Agent** — the decision maker
* **Environment** — the grid world
* **State** — the agent's current position
* **Action** — up, down, left, right
* **Reward** — feedback from the environment
* **Episode** — one complete run from start to treasure
* **Markov Property** — future depends only on the current state

These concepts form the foundation for more advanced topics such as Monte Carlo Methods, Q-Learning, Deep Q-Networks (DQNs), and Policy Gradient methods.

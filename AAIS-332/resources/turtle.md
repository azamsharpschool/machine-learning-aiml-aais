
# 🐢 TurtleWorld — Code Walkthrough

## 1) Imports

```python
import gymnasium as gym
from gymnasium import spaces
import numpy as np
```

* **gymnasium**: the framework we use to define environments that agents can interact with (`reset`, `step`, etc.).
* **spaces**: describes the *shape* of observations and actions (e.g., “3 possible positions”, “2 possible actions”).
* **numpy**: not heavily used here, but handy for numbers/arrays when needed.

---

## 2) Define the Environment Class

```python
class TurtleWorld(gym.Env):
```

* You’re creating a **custom environment** by subclassing `gym.Env`.
* Every Gymnasium environment must implement at least: `__init__`, `reset`, `step`. `render` is optional but helpful.

---

## 3) `__init__`: Describe the world

```python
def __init__(self):
    super().__init__()
    # Positions: 0 = home, 1 = rock, 2 = pond
    self.observation_space = spaces.Discrete(3)
    # Actions: 0 = move left, 1 = move right
    self.action_space = spaces.Discrete(2)
    self.state = 0  # Start at home
    self.steps = 0
```

* **Observation space**: `spaces.Discrete(3)` means the state is a single integer in `{0, 1, 2}`:

  * `0` = 🏠 Home (start)
  * `1` = 🔥 Hot rock (bad)
  * `2` = 💧 Pond (goal)
* **Action space**: `spaces.Discrete(2)` means there are 2 possible actions:

  * `0` = move left
  * `1` = move right
* **State**: We keep the turtle’s current tile in `self.state`. Start at `0` (home).
* **Step counter**: `self.steps` tracks how many actions have happened (useful for ending an episode after a limit).

> Think of this as setting the game’s rules and initial setup.

---

## 4) `reset`: Start a new episode

```python
def reset(self):
    self.state = 0
    self.steps = 0
    return self.state, {}
```

* Called when you want to start fresh.
* Puts the turtle back at **home** and resets the step count.
* Returns a tuple `(observation, info)`:

  * `observation`: the current state (here, just the integer `0/1/2`)
  * `info`: extra details for debugging (empty `{}` here)

> In Gymnasium, `reset()` always returns `(obs, info)`.

---

## 5) `step`: Take one action and update the world

```python
def step(self, action):
    # Move turtle
    if action == 1 and self.state < 2:
        self.state += 1
    elif action == 0 and self.state > 0:
        self.state -= 1
```

* The turtle moves **right** if `action == 1` (unless it’s already at the far right).
* It moves **left** if `action == 0` (unless it’s already at the far left).
* The checks `self.state < 2` and `self.state > 0` prevent moving off the ends.

### Rewards and episode end

```python
    # Rewards
    if self.state == 2:
        reward = +10    # reached pond
        done = True
    elif self.state == 1:
        reward = -5     # hot rock
        done = False
    else:
        reward = -1     # still at home
        done = False
```

* **Pond (2)**: Big win → `+10` and **end the episode** (`done = True`).
* **Rock (1)**: Ouch → `-5`, keep going.
* **Home (0)**: Not the goal → `-1`, keep going.

### Step cap (safety stop)

```python
    self.steps += 1
    if self.steps >= 10:
        done = True
```

* Prevents episodes from running forever.
* After 10 moves, **we stop** (even if the turtle didn’t reach the pond).

### Return the step result

```python
    return self.state, reward, done, False, {}
```

* Gymnasium’s `step` returns **five** values:
  `(observation, reward, terminated, truncated, info)`

Here:

* `observation`: the new state (0, 1, or 2)
* `reward`: the number from the table above
* `terminated` (**your `done` flag**): True if the task is *successfully finished* (reached pond)
* `truncated`: True if the episode stopped due to a **time limit** or external reason (we return `False` and just fold time limit into `done`—simple for students)
* `info`: extra debug info (empty `{}` here)

> For teaching, using a single `done` boolean is fine; for strict Gymnasium style, you can separate `terminated` (goal reached) and `truncated` (time limit).

---

## 6) `render`: Show what the world looks like

```python
def render(self):
    tiles = ["🏠", "🔥", "💧"]
    world = ["⬜"] * 3
    world[self.state] = "🐢"
    print(" ".join(world), " | ", "".join(tiles))
```

* Builds a simple text visualization:

  * Left side: where the **turtle** is (`🐢` placed over the 3 empty squares)
  * Right side: the legend `[🏠🔥💧]`
* Example:

  ```
  ⬜ 🐢 ⬜  |  🏠🔥💧
  ```

---

## 7) Play the game with a random agent

```python
env = TurtleWorld()
state, _ = env.reset()

for step in range(100):
    action = env.action_space.sample()  # random move
    next_state, reward, done, _, _ = env.step(action)
    env.render()
    print(f"Step {step+1}: action={action}, reward={reward}\n")
    if done:
        break
```

* **`env.action_space.sample()`**: picks a random action (left or right).
  This is like a student guessing moves without thinking.
* After each move:

  * We see the new state (`next_state`)
  * The **reward** for that move
  * Whether the episode is **done** (goal reached or step limit)
  * We **render** the world so it’s easy to follow.
* We **stop** when `done` becomes `True`.

> This is a **baseline**: random behavior. In RL, we later replace this with a learning agent that **improves** over time.

---

## Mental Model (for students)

* The turtle is on a mini **number line**: `0 — 1 — 2`
* It **chooses** left/right.
* The **reward** tells it if that was good or bad.
* A smart agent will learn a **strategy**:

  * “From 0: go right twice to reach 2. Avoid staying at 1.”

---

## Optional: Small Improvements (still simple)

* **Separate termination vs time limit** (Gymnasium style):

  ```python
  terminated = (self.state == 2)
  truncated = (self.steps >= 10)
  done = terminated or truncated
  return self.state, reward, terminated, truncated, {}
  ```

* **Make rock harsher** to encourage faster learning:

  ```python
  reward = -8  # instead of -5
  ```

* **Give a tiny penalty for every move** to encourage shorter paths:

  ```python
  step_penalty = -0.2
  reward += step_penalty
  ```

---


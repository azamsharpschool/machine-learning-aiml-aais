
### Example: Rolling a Dice

Suppose a game works like this:

* Roll a dice.
* If you roll a **6**, you win **10 points**.
* Otherwise, you get **0 points**.

Monte Carlo says:

> Let's play many times and estimate the average reward.

```python
import random

rewards = []

for _ in range(1000):
    roll = random.randint(1, 6)

    if roll == 6:
        reward = 10
    else:
        reward = 0

    rewards.append(reward)

average_reward = sum(rewards) / len(rewards)

print("Estimated Value:", average_reward)
```

### What is happening?

We are not using a formula.

Instead, we:

1. Play many games.
2. Observe the rewards.
3. Average the results.

This is the core idea behind Monte Carlo methods.

---

### Another Example: Treasure Boxes

Imagine there are two treasure boxes.

```text
Box A
70% chance of $10
30% chance of $0

Box B
40% chance of $20
60% chance of $0
```

We don't know which box is better.

Let's simulate.

```python
import random

box_a_rewards = []
box_b_rewards = []

for _ in range(1000):

    if random.random() < 0.7:
        box_a_rewards.append(10)
    else:
        box_a_rewards.append(0)

    if random.random() < 0.4:
        box_b_rewards.append(20)
    else:
        box_b_rewards.append(0)

print("Box A Value:", sum(box_a_rewards) / len(box_a_rewards))
print("Box B Value:", sum(box_b_rewards) / len(box_b_rewards))
```

### Why this is Monte Carlo

We are estimating value through experience.

Instead of calculating:

```text
Expected Value = Probability × Reward
```

we let the computer play the game thousands of times and learn the average outcome.

---

### Reinforcement Learning Connection

In reinforcement learning:

* A state is like a treasure box.
* The agent visits the state many times.
* It records the rewards.
* It averages the results.

That average becomes the estimated value of the state.

So Monte Carlo methods are essentially:

> Learn by completing many episodes and averaging the rewards you observe.


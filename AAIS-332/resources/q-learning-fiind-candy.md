# Q-Learning Example: Teaching a Robot to Find Candy

In this example, we will learn the basic idea behind Q-Learning using a very simple scenario.

Imagine a robot is placed in a room. Somewhere in the room is a piece of candy. The robot has two choices:

```text
Left
Right
```

The candy is located on the right side of the room.

```text
Left        Robot        Right (Candy)
```

The robot does not know where the candy is. It must learn through trial and error.

## Full Code

```python
import random

q_table = {
    "left": 0,
    "right": 0
}

alpha = 0.1

for episode in range(100):

    action = random.choice(["left", "right"])

    if action == "right":
        reward = 10
    else:
        reward = -1

    q_table[action] = q_table[action] + alpha * (
        reward - q_table[action]
    )

print(q_table)
```

## What Is a Q-Value?

A Q-value represents how good an action is.

At the beginning, the robot has no experience.

```python
q_table = {
    "left": 0,
    "right": 0
}
```

This means the robot believes both actions are equally good.

```text
Go Left  = 0
Go Right = 0
```

Since it has never tried either action, it has no information.

## Learning Through Experience

The robot randomly chooses an action.

```python
action = random.choice(["left", "right"])
```

Sometimes it chooses:

```text
Left
```

Sometimes it chooses:

```text
Right
```

This process is called exploration.

The robot is exploring the environment to learn which actions produce better results.

## Receiving Rewards

If the robot goes right, it finds the candy.

```python
if action == "right":
    reward = 10
```

The robot receives a reward of:

```text
+10
```

If the robot goes left, it does not find the candy.

```python
else:
    reward = -1
```

The robot receives a reward of:

```text
-1
```

The reward acts as feedback from the environment.

## Updating the Q-Value

The most important line of code is:

```python
q_table[action] = q_table[action] + alpha * (
    reward - q_table[action]
)
```

This line updates the robot's knowledge.

You can think of it as:

```text
New Knowledge =
Old Knowledge +
Small Adjustment
```

The adjustment is based on the reward the robot just received.

If an action consistently receives good rewards, its Q-value increases.

If an action consistently receives bad rewards, its Q-value decreases.

## What Happens After Many Attempts?

The robot repeats this process 100 times.

Each time it tries an action, receives a reward, and updates its knowledge.

Eventually, the Q-table might look like:

```python
{
    "left": -1.0,
    "right": 10.0
}
```

The robot has learned:

```text
Going Right is much better than Going Left.
```

## Why Is This Called Q-Learning?

Q-Learning is a reinforcement learning algorithm that learns the value of actions.

The Q-table stores:

```text
How good is this action?
```

In our example:

```text
Q(Left)
Q(Right)
```

represent how valuable each action is.

Over time, the robot learns which action produces the highest reward.

## Key Concepts

### Agent

The robot is the agent.

The agent is responsible for making decisions.

### Action

The possible actions are:

```text
Left
Right
```

### Reward

The environment provides feedback.

```text
Right = +10
Left  = -1
```

### Learning

The robot improves its decisions by learning from rewards.

### Q-Value

A Q-value measures how good an action is based on past experience.

## Summary

This example demonstrates the core idea behind Q-Learning.

The robot:

1. Tries different actions.
2. Receives rewards.
3. Updates its knowledge.
4. Learns which action produces the highest reward.

Eventually, the robot learns that going right leads to candy and consistently chooses the action with the highest Q-value.

This is the foundation of Q-Learning and many modern reinforcement learning systems.

# Delivery Robot Environment Walkthrough

In this example, we will create a simple training environment for a delivery robot.

The goal of the robot is to deliver food from a restaurant to a customer. This example demonstrates how reinforcement learning environments are designed for specific real-world tasks.

## Full Code

```python
import random

states = ["Restaurant", "Street", "Customer"]
actions = ["drive", "wait"]

rewards = {
    "drive": -1,
    "wait": -2,
    "delivered": 10
}

def step(state, action):
    if state == "Restaurant":
        if action == "drive":
            return "Street", rewards["drive"], False
        return "Restaurant", rewards["wait"], False

    if state == "Street":
        if action == "drive":
            return "Customer", rewards["delivered"], True
        return "Street", rewards["wait"], False

    return "Customer", 0, True


state = "Restaurant"
done = False
total_reward = 0

while not done:
    action = random.choice(actions)

    next_state, reward, done = step(state, action)

    print(f"State: {state}, Action: {action}, Reward: {reward}, Next: {next_state}")

    total_reward += reward
    state = next_state

print("Total Reward:", total_reward)
```

## The Environment

The environment consists of three locations:

```text
Restaurant → Street → Customer
```

The robot begins at the restaurant and must reach the customer.

Each location is called a state.

```python
states = ["Restaurant", "Street", "Customer"]
```

In reinforcement learning, a state represents the current situation of the agent.

---

## Actions

The robot can perform two actions:

```python
actions = ["drive", "wait"]
```

### Drive

The robot moves toward the customer.

### Wait

The robot stays where it is.

In reinforcement learning, actions represent the decisions made by the agent.

---

## Rewards

The environment provides feedback using rewards.

```python
rewards = {
    "drive": -1,
    "wait": -2,
    "delivered": 10
}
```

### Driving

```python
"drive": -1
```

Driving costs time and energy, so the robot receives a small penalty.

### Waiting

```python
"wait": -2
```

Waiting is even worse because no progress is made.

### Delivery Completed

```python
"delivered": 10
```

Successfully delivering the package produces a large positive reward.

The goal of the agent is to maximize its total reward.

---

## The Step Function

The step function represents the environment.

```python
next_state, reward, done = step(state, action)
```

Given:

* Current state
* Selected action

the environment returns:

* Next state
* Reward
* Whether the task is complete

---

## Starting at the Restaurant

Suppose the robot is currently at:

```python
state = "Restaurant"
```

If it chooses:

```python
action = "drive"
```

the environment returns:

```python
"Street", -1, False
```

This means:

```text
Move to Street
Receive reward -1
Task is not finished
```

---

## Waiting at the Restaurant

If the robot chooses:

```python
action = "wait"
```

the environment returns:

```python
"Restaurant", -2, False
```

This means:

```text
Stay at Restaurant
Receive reward -2
Task is not finished
```

The robot learns that waiting is usually not a good strategy.

---

## Moving from Street to Customer

Once the robot reaches the street, it has another decision to make.

If it chooses:

```python
action = "drive"
```

the environment returns:

```python
"Customer", 10, True
```

This means:

```text
Reach the customer
Receive reward +10
Task is complete
```

The episode ends because the delivery was successful.

---

## Running the Simulation

The simulation begins at:

```python
state = "Restaurant"
```

The robot randomly chooses actions:

```python
action = random.choice(actions)
```

At this stage the robot is not intelligent.

It simply explores the environment and observes the rewards it receives.

---

## Example Output

A sample run might look like this:

```text
State: Restaurant, Action: wait, Reward: -2, Next: Restaurant

State: Restaurant, Action: drive, Reward: -1, Next: Street

State: Street, Action: drive, Reward: 10, Next: Customer

Total Reward: 7
```

In this example:

* The robot wasted time waiting.
* It then drove toward the customer.
* It completed the delivery.
* It accumulated a total reward of 7.

---

## Why This Example Is Important

This example demonstrates the key parts of a reinforcement learning environment:

### States

```text
Restaurant
Street
Customer
```

### Actions

```text
Drive
Wait
```

### Rewards

```text
Drive = -1
Wait = -2
Delivery = +10
```

### Goal

```text
Deliver food to the customer
```

---

## Connection to Real World Systems

Many real-world systems use similar environments.

Examples include:

* Food delivery robots
* Warehouse robots
* Autonomous vehicles
* Drone delivery systems

Although these real systems are much more complex, they are built using the same ideas shown in this simple example.

By designing states, actions, rewards, and goals, engineers can create environments that teach AI agents how to make better decisions.

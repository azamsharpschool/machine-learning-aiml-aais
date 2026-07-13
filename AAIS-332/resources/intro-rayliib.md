
``` py 
# Install Ray RLlib
!pip install -q "ray[rllib]"

# Import RLlib
from ray.rllib.algorithms.ppo import PPOConfig

# Configure the environment
config = (
    PPOConfig()
    .environment("CartPole-v1")
)

# Build the reinforcement learning agent
agent = config.build()

print("Training agent...\n")

# Train the agent
for i in range(5):
    result = agent.train()

    print(
        f"Iteration {i+1}: "
        f"Average Reward = {result['env_runners']['episode_return_mean']:.2f}"
    )

print("\nTraining Complete!")
```


### Step 1 - Install RLlib


```python
!pip install -q "ray[rllib]"
```

The first step installs the **Ray RLlib** library. RLlib provides implementations of popular reinforcement learning algorithms, so we don't have to build them from scratch.

---

### Step 2 - Import PPO

```python
from ray.rllib.algorithms.ppo import PPOConfig
```

This imports the configuration class for the **Proximal Policy Optimization (PPO)** algorithm, which is the reinforcement learning algorithm used to train our agent.

---

### Step 3 - Configure the Environment

```python
config = (
    PPOConfig()
    .environment("CartPole-v1")
)
```

A PPO configuration object is created, and the training environment is set to **CartPole-v1**.

In this environment, the agent controls a cart that can move left or right. The objective is to keep the pole balanced for as long as possible. Every successful time step earns a reward, while allowing the pole to fall ends the episode.

---

### Step 4 - Build the Agent

```python
agent = config.build()
```

Using the configuration, RLlib creates the reinforcement learning agent. This includes the PPO algorithm, the neural network that will learn the policy, and the connection to the CartPole environment.

At this point, the agent has not learned anything yet.

---

### Step 5 - Train the Agent

```python
for i in range(5):
    result = agent.train()
```

The training loop runs five iterations.

During each call to `train()`:

* The agent plays many episodes of CartPole.
* It observes the current state of the environment.
* It selects actions (move left or move right).
* It receives rewards based on how well it balances the pole.
* PPO updates the neural network to improve future decisions.

After training, RLlib returns statistics about the agent's performance.

---

### Step 6 - Display Progress

```python
print(
    f"Iteration {i+1}: "
    f"Average Reward = {result['env_runners']['episode_return_mean']:.2f}"
)
```

This prints the **average reward** earned during the training iteration.

For example:

```
Iteration 1: Average Reward = 22.15
Iteration 2: Average Reward = 41.83
Iteration 3: Average Reward = 78.40
Iteration 4: Average Reward = 132.61
Iteration 5: Average Reward = 187.94
```

As the average reward increases, it indicates that the agent is learning to balance the pole more successfully.

---

### Step 7 - Training Complete

```python
print("\nTraining Complete!")
```

After all five training iterations are finished, the program prints a message indicating that the training process has completed. At this point, the agent has learned a policy that performs significantly better than when it started.

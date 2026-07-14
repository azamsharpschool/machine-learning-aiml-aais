


# Walkthrough

In this example, we create our own reinforcement learning environment instead of using one of the built-in Gym environments. The goal is to train an AI thermostat that keeps a room at a comfortable temperature.

---

## Step 1 - Import the Required Libraries

```python
import gymnasium as gym
from gymnasium import spaces
```

The `gymnasium` library provides the base class used to create custom reinforcement learning environments. We also import `spaces`, which allows us to define the possible states and actions available to the agent.

---

## Step 2 - Create the Environment

```python
class ThermostatEnv(gym.Env):
```

A new environment named `ThermostatEnv` is created by inheriting from `gym.Env`.

Every custom Gym environment must define how the environment is initialized, reset, and updated when the agent performs an action.

---

## Step 3 - Initialize the Environment

```python
def __init__(self):
    super().__init__()

    self.observation_space = spaces.Discrete(3)
    self.action_space = spaces.Discrete(3)

    self.state = 0
```

The constructor defines the environment.

The observation space contains three possible temperature states:

* **0** = Cold
* **1** = Comfortable
* **2** = Hot

The action space contains three possible actions:

* **0** = Cool the room
* **1** = Heat the room
* **2** = Do nothing

The environment starts in the **Cold** state.

---

## Step 4 - Reset the Environment

```python
def reset(self, seed=None, options=None):
    super().reset(seed=seed)

    self.state = 0

    return self.state, {}
```

The `reset()` method prepares the environment for a new training episode.

Each time a new episode begins, the thermostat starts in the **Cold** state.

The method returns the initial state so the agent knows where it is starting.

---

## Step 5 - Update the Environment

```python
def step(self, action):
```

The `step()` method is the heart of the environment.

It receives an action from the agent, updates the room temperature, calculates the reward, and returns the new state.

---

## Step 6 - Process the Agent's Action

```python
if action == 1 and self.state < 2:
    self.state += 1

elif action == 0 and self.state > 0:
    self.state -= 1
```

If the agent chooses **Heat**, the temperature increases.

If the agent chooses **Cool**, the temperature decreases.

If the agent chooses **Do Nothing**, the temperature remains the same.

---

## Step 7 - Calculate the Reward

```python
if self.state == 1:
    reward = 10
else:
    reward = -5
```

The reward encourages the agent to keep the room comfortable.

* Comfortable → **+10**
* Cold → **−5**
* Hot → **−5**

Over time, the agent learns that reaching and maintaining the comfortable state produces the highest reward.

---

## Step 8 - Return the Results

```python
terminated = False
truncated = False

return self.state, reward, terminated, truncated, {}
```

The environment returns:

* the new state,
* the reward,
* whether the episode has ended,
* whether it was truncated,
* and an empty information dictionary.

For simplicity, this example never ends an episode.

---

## Step 9 - Register the Environment

```python
register_env(
    "Thermostat",
    lambda config: ThermostatEnv()
)
```

Before RLlib can use the custom environment, it must be registered.

The name **"Thermostat"** is associated with the `ThermostatEnv` class so RLlib knows which environment to create during training.

---

## Step 10 - Configure PPO

```python
config = (
    PPOConfig()
    .environment("Thermostat")
)
```

A PPO configuration is created and linked to the custom Thermostat environment.

Notice that this looks almost identical to the CartPole example. The only difference is the environment name.

---

## Step 11 - Build the Agent

```python
agent = config.build()
```

RLlib creates the reinforcement learning agent, including the PPO algorithm, neural network, and connection to the Thermostat environment.

Initially, the agent has no knowledge of the best actions to take.

---

## Step 12 - Train the Agent

```python
for i in range(10):
    result = agent.train()
```

Each training iteration allows the agent to interact with the environment many times.

During training, the agent:

* Observes the current temperature.
* Chooses an action.
* Receives a reward.
* Updates its policy to improve future decisions.

After each iteration, RLlib returns statistics describing the agent's performance.

---

## Step 13 - Display the Results

```python
print(result["env_runners"]["episode_return_mean"])
```

The average reward is displayed after each training iteration.

As training progresses, the average reward should increase, indicating that the agent has learned to keep the room at the comfortable temperature more consistently.

---

``` py 
# Install RLlib
!pip install -q "ray[rllib]"

# Import libraries
import gymnasium as gym
from gymnasium import spaces

from ray.tune.registry import register_env
from ray.rllib.algorithms.ppo import PPOConfig


# ----------------------------------------
# Create a Custom Environment
# ----------------------------------------

class ThermostatEnv(gym.Env):

    def __init__(self, config=None):
        super().__init__()

        # States:
        # 0 = Cold
        # 1 = Comfortable
        # 2 = Hot
        self.observation_space = spaces.Discrete(3)

        # Actions:
        # 0 = Cool
        # 1 = Heat
        # 2 = Do Nothing
        self.action_space = spaces.Discrete(3)

        self.state = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.state = 0

        return self.state, {}

    def step(self, action):

        # Heat the room
        if action == 1 and self.state < 2:
            self.state += 1

        # Cool the room
        elif action == 0 and self.state > 0:
            self.state -= 1

        # Do Nothing
        else:
            pass

        # Reward
        if self.state == 1:
            reward = 10
        else:
            reward = -5

        terminated = False
        truncated = False

        return self.state, reward, terminated, truncated, {}


# ----------------------------------------
# Register Environment
# ----------------------------------------

register_env(
    "Thermostat",
    lambda config: ThermostatEnv(config)
)

# ----------------------------------------
# Configure PPO
# ----------------------------------------

config = (
    PPOConfig()
    .environment("Thermostat")
)

# ----------------------------------------
# Build Agent
# ----------------------------------------

agent = config.build()

print("Training Thermostat Agent...\n")

# ----------------------------------------
# Train Agent
# ----------------------------------------

for i in range(10):

    result = agent.train()

    print(
        f"Iteration {i+1}: "
        f"Average Reward = {result['env_runners']['episode_return_mean']:.2f}"
    )

print("\nTraining Complete!")
```

## 🧠 What is Reinforcement Learning (RL)?

Reinforcement Learning is how we teach computers **through experience**.
Instead of giving them the correct answer (like in math), we give them a **goal** and **feedback (rewards)** for every action they take.

* The computer (called an **agent**) interacts with an **environment**.
* At each step:

  1. The agent **sees the state** of the environment.
  2. It **takes an action** (e.g., move left or right).
  3. It **receives a reward** (+1 point if it did well).
  4. It **learns** how to do better next time.

This is similar to how **humans learn** — by trial and error.

---

## 🎯 The CartPole Game

Imagine balancing a broom on your hand.
That’s what the CartPole environment is doing:

* There’s a **cart** that moves left and right on a track.
* A **pole** is attached to the cart by a joint.
* The goal is to **keep the pole upright** for as long as possible.

Every second the pole stays up, the agent gets a **reward of +1**.
When it falls — the episode ends.

---

## 🧩 Step-by-Step Code Explanation

### Step 1: Installing the Libraries

```python
!pip install "gymnasium[classic-control]" stable-baselines3 moviepy --quiet
```

* `gymnasium`: gives us environments like CartPole.
* `stable-baselines3`: provides pre-built RL algorithms (brains).
* `moviepy`: lets us play back the recorded video.

---

### Step 2: Importing Libraries

```python
import gymnasium as gym
from stable_baselines3 import PPO
from gymnasium.wrappers import RecordVideo
import os
from IPython.display import Video
```

We bring in everything we’ll use:

* `PPO` is a smart RL algorithm.
* `RecordVideo` helps us save what the agent does.
* `Video` lets Colab play the video inline.

---

### Step 3: Creating the Environment

```python
env = gym.make("CartPole-v1")
```

This line creates the CartPole game.
Behind the scenes, `gymnasium` gives us:

* The **state** (cart position, velocity, pole angle, etc.)
* The **actions** (move left or right)
* The **reward system** (+1 each step the pole stays up)

---

### Step 4: Choosing the Brain

```python
model = PPO("MlpPolicy", env, verbose=0)
```

* `PPO` (Proximal Policy Optimization) is a type of RL algorithm that learns stable policies.
* `"MlpPolicy"` means it uses a **neural network** (a simple brain) to learn patterns from data.

So the model starts knowing nothing — like a baby learning to balance for the first time.

---

### Step 5: Training the Model

```python
model.learn(total_timesteps=20_000)
```

This is where learning happens:

* The agent plays **20,000 steps** of the game.
* It tries random moves at first.
* Over time, it figures out which actions help it get higher rewards.

The more steps it practices, the better it gets.

---

### Step 6: Recording the Agent’s Play

```python
video_env = RecordVideo(
    gym.make("CartPole-v1", render_mode="rgb_array"),
    video_folder="videos",
    episode_trigger=lambda e: True
)
```

* We create a new environment that can **record frames** (`render_mode="rgb_array"`).
* `RecordVideo` saves the game frames to a folder.
* The `episode_trigger` tells it to record every episode.

Then we run one test episode:

```python
obs, _ = video_env.reset()
done = False
while not done:
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, _ = video_env.step(action)
    done = terminated or truncated
```

Here’s what happens:

* The model **looks at the game screen** (`obs`).
* It **predicts an action** (move left or right).
* It **updates the environment** with that move.
* It **repeats** until the pole falls or time runs out.

---

### Step 7: Showing the Video

```python
latest_video = sorted(os.listdir("videos"))[-1]
Video(os.path.join("videos", latest_video), embed=True)
```

This displays the video **right inside Colab** so you can *see* how well it did.

---

## 🏆 What You’ll Observe

After training:

* The cart will move smoothly left and right.
* The pole stays upright for 200+ steps.
* The agent has learned **a control strategy** — purely from rewards!

---

## 🧪 Experiments to Try

| Experiment                     | What it Teaches                                    |
| ------------------------------ | -------------------------------------------------- |
| Change `total_timesteps=5_000` | Shows what happens with less learning time.        |
| Change algorithm to `A2C`      | Try a different learning brain.                    |
| Add noise to state             | See how fragile or robust the learned behavior is. |
| Train longer (`50_000`)        | The agent performs almost perfectly.               |

---

## 📚 Key Learning Points

| Concept     | Meaning                                            |
| ----------- | -------------------------------------------------- |
| **State**   | What the agent sees (numbers describing the game). |
| **Action**  | The choice it makes (move left/right).             |
| **Reward**  | Feedback (+1 each step pole is balanced).          |
| **Episode** | One full game from start to fall.                  |
| **Policy**  | The strategy the agent learns to get high rewards. |

---

## 🧩 Real-World Connection

Reinforcement learning is used in:

* **Self-driving cars** (learn how to steer safely)
* **Robots** (learn to walk or grab objects)
* **Game AI** (learn to play games like chess or Go)
* **Healthcare** (optimize treatments or dosages)

The same ideas apply — the system *learns by experience*.

---

## 🪄 Summary

* We created an agent → made it play → rewarded good behavior.
* Over time, it learned how to keep the pole balanced.
* This is **the essence of reinforcement learning** — learning by doing!

---

Would you like me to create a **reward-vs-episode chart** you can add at the end of this notebook to visualize how the agent improves? It helps students *see* the learning curve.

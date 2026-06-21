
### Markov Principle 

```python
position = 0
goal = 4

for step in range(10):

  # Markov decision:
  # The agent only looks at the current state: position
  if position < goal:
    action = "right"
  else:
    action = "left"

  if action == "right":
    position += 1
  else:
    position -= 1

  position = max(0, min(position, goal))

  reward = 10 if position == goal else -1

  # draw the world
  world = ["_"] * 5
  world[goal] = "🧀"
  world[position] = "🐭"

  print(" ".join(world))
  print(f"Step: {step}, Action: {action}, Position: {position}, Reward: {reward}")
  print()

  if position == goal:
    print("🐭 Found the cheese!")
    break
```

The key change is this:

```python
if position < goal:
  action = "right"
else:
  action = "left"
```

That means the agent is deciding based only on the **current state**, not the past.

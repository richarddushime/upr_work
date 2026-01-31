from chicken_jump import ChickenJump

env = ChickenJump()

q_table = [[0, 0] for _ in range(20)]  # 20 states (0 - 19) and 2 actions [walk, fly].
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor

for episode in range(100):
    episode_reward = 0
    state = env.reset()
    while not env.terminated:
        # In the current state, is it better to walk (0) or fly (1)?
        action = 0 if q_table[state][0] > q_table[state][1] else 1

        # Execute the chosen action, get a reward.
        next_state, reward = env.action(action)
        episode_reward += reward
        
        # What is the best we can do in the new state?
        q_next = max(q_table[next_state][0], q_table[next_state][1])

        # Update the policy using the Bellman Equation.
        q_table[state][action] += alpha * (reward + gamma * q_next - q_table[state][action])
        
        state = next_state

    print(f'Episode {episode} finished with cummulative reward {episode_reward}.')

env.close()


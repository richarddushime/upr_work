import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset()
episode_over = False
total_reward = 0
while not episode_over:
    action = env.action_space.sample()  # Random action for now
    observation, reward, terminated, truncated, info = env.step(action)
    total_reward += reward
    episode_over = terminated or truncated
env.close()

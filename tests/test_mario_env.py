from scripts.mario_env import MarioKartEnv  

# Create environment  
env = MarioKartEnv()  

# Reset environment and get initial observation  
obs = env.reset()  
print("Initial Observation Shape:", obs.shape)  

# Take a random step  
action = env.action_space.sample()  
obs, reward, done, info = env.step(action)  
print(f"Step Taken: {action}, Reward: {reward}, Done: {done}")  

# Close environment  
env.close()  


import requests

name = "Your Name"
params = {
    "learning_rate": 0.0003,  # Step size for updating the agent (higher = faster learning, but less stable)
    "n_steps": 2048,           # Number of steps to run for each environment per update
    "batch_size": 64,          # Minibatch size for each gradient update
    "gamma": 0.99,             # Discount factor for future rewards (close to 1 = long-term focus)
    "ent_coef": 0.01,          # Entropy coefficient for exploration (higher = more exploration)
    "clip_range": 0.2          # PPO policy clip range (prevents too large policy updates)
}
server_url = "http://<admin-ip>:5000/submit"

response = requests.post(server_url, json={"name": name, "params": params}, timeout=120)
print(response.json())

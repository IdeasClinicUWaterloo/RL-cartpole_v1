# RL CartPole Leaderboard - User Guide

This guide is for users who want to submit their RL agent hyperparameters to the leaderboard.

---

## Setup

1. **Install requirements:**
   ```
   pip install -r requirements.txt
   ```
2. **Get a copy of `submit_params.py` from the admin.**
3. **Edit `submit_params.py`:**
   - Set your name in the `name` variable.
   - Set the server URL to the admin's address, e.g.:
     ```python
     server_url = "http://<admin-ip>:5000/submit"
     ```
   - Optionally, change the hyperparameters in the `params` dictionary. The following are supported (see [Stable-Baselines3 PPO docs](https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html#parameters)):
     - `learning_rate`: Step size for updating the agent (higher = faster learning, but less stable)
     - `n_steps`: Number of steps to run for each environment per update
     - `batch_size`: Minibatch size for each gradient update
     - `gamma`: Discount factor for future rewards (close to 1 = long-term focus)
     - `gae_lambda`: GAE parameter (controls bias-variance tradeoff)
     - `ent_coef`: Entropy coefficient for exploration (higher = more exploration)
     - `clip_range`: PPO policy clip range (prevents too large policy updates)
     - `vf_coef`: Value function loss coefficient
     - `max_grad_norm`: Gradient clipping
     - `n_epochs`: Number of epochs per update
     - `policy_kwargs`: Custom network architecture (e.g., `net_arch`, `activation_fn`)
4. **Run the script:**
   ```
   python submit_params.py
   ```
   (Or, if using the full path:)
   ```
   C:\University of waterloo\Dev RL game\.venv\Scripts\python.exe submit_params.py
   ```
5. **Check the leaderboard:**
   - Open `http://<admin-ip>:5000/leaderboard_html` in your browser to see your submission, score, and video.

---

## Example `submit_params.py`
```python
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
```

---

For questions or help, contact the server admin.

# RL CartPole Leaderboard - Admin Guide

This guide is for the server host (admin) who runs the leaderboard and manages submissions.

---

## Setup

1. **Install requirements:**
   ```
   pip install -r requirements.txt
   ```
2. **Start the server:**
   ```
   C:\University of waterloo\Dev RL game\.venv\Scripts\python.exe server.py
   ```
   (Or use the call operator in PowerShell:)
   ```
   & "C:\University of waterloo\Dev RL game\.venv\Scripts\python.exe" server.py
   ```
3. **Share your server's IP address and port (default: 5000) with users.**
4. **View the leaderboard:**
   - Open `http://<your-ip>:5000/leaderboard_html` in your browser.

---

## Features
- Receives hyperparameter submissions from users.
- Trains and evaluates RL agents automatically.
- Displays a live leaderboard with scores, hyperparameters, names, and video previews.
- Videos are saved and served for each submission.
- Leaderboard displays: learning rate, n_steps, batch size, gamma, ent_coef, clip_range, and more.

---

## Supported PPO Hyperparameters
You can allow users to tune any of the following PPO hyperparameters (see [Stable-Baselines3 PPO docs](https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html#parameters) for details):

- `learning_rate`: Step size for updating the agent
- `n_steps`: Number of steps to run for each environment per update
- `batch_size`: Minibatch size for each gradient update
- `gamma`: Discount factor for future rewards
- `gae_lambda`: GAE parameter
- `ent_coef`: Entropy coefficient for exploration
- `clip_range`: PPO policy clip range
- `vf_coef`: Value function loss coefficient
- `max_grad_norm`: Gradient clipping
- `n_epochs`: Number of epochs per update
- `policy_kwargs`: Custom network architecture (e.g., `net_arch`, `activation_fn`)

You can add or remove any of these from the user script and leaderboard as desired.

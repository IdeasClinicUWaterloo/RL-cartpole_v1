import gymnasium as gym
from stable_baselines3 import PPO

def train_and_evaluate(params, save_video=True, video_path="cartpole_run.mp4"):
    env = gym.make("CartPole-v1", render_mode="rgb_array" if save_video else None)
    model = PPO("MlpPolicy", env, **params)
    model.learn(total_timesteps=10000)
    # Evaluate
    episode_rewards = []
    frames = []
    for _ in range(10):
        obs, _ = env.reset()
        done, total_reward = False, 0
        while not done:
            if save_video:
                frames.append(env.render())
            action, _ = model.predict(obs)
            obs, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            total_reward += reward
        episode_rewards.append(total_reward)
    avg_reward = sum(episode_rewards) / len(episode_rewards)
    if save_video and frames:
        import imageio
        imageio.mimsave(video_path, frames, fps=30)
    return avg_reward, video_path if save_video else avg_reward

import os
from flask import Flask, request, jsonify, send_from_directory
from rl_agent import train_and_evaluate
import sys

app = Flask(__name__)
leaderboard = []

@app.route('/submit', methods=['POST'])
def submit():
    print(f"Received /submit request: {request.method} {request.json}", file=sys.stderr)
    params = request.json.get('params', {})
    name = request.json.get('name', 'Anonymous')
    score, video_path = train_and_evaluate(params, save_video=True, video_path=f"videos/{name}_cartpole.mp4")
    entry = {'name': name, 'params': params, 'score': score, 'video': f"{name}_cartpole.mp4"}
    leaderboard.append(entry)
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    return jsonify({'score': score, 'leaderboard': leaderboard, 'video': f"/video/{name}_cartpole.mp4"})

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    print("Received /leaderboard request", file=sys.stderr)
    return jsonify(leaderboard)

# HTML leaderboard endpoint
@app.route('/leaderboard_html', methods=['GET'])
def leaderboard_html():
    html = """
    <html>
    <head>
        <title>RL Leaderboard</title>
        <!-- Removed auto-refresh to avoid interrupting video playback -->
        <style>
            body { font-family: Arial, sans-serif; }
            table { border-collapse: collapse; width: 70%; margin: 40px auto; }
            th, td { border: 1px solid #ccc; padding: 8px 12px; text-align: center; }
            th { background: #f2f2f2; }
            h2 { text-align: center; }
        </style>
    </head>
    <body>
        <h2>RL Leaderboard</h2>
        <div style='text-align:center; margin-bottom:20px;'>
            <button onclick='window.location.reload();' style='padding:8px 16px; font-size:16px;'>Refresh</button>
        </div>
        <table>
            <tr>
                <th>Rank</th>
                <th>Name</th>
                <th>Score</th>
                <th>Learning Rate</th>
                <th>n_steps</th>
                <th>Batch Size</th>
                <th>Gamma</th>
                <th>Ent Coef</th>
                <th>Clip Range</th>
                <th>Video</th>
            </tr>
    """
    for idx, entry in enumerate(leaderboard, 1):
        params = entry['params']
        video_tag = f"<video width='160' controls><source src='/video/{entry['video']}' type='video/mp4'>Your browser does not support the video tag.</video>" if entry.get('video') else ''
        html += f"""
            <tr>
                <td>{idx}</td>
                <td>{entry.get('name', 'Anonymous')}</td>
                <td>{entry['score']:.2f}</td>
                <td>{params.get('learning_rate')}</td>
                <td>{params.get('n_steps')}</td>
                <td>{params.get('batch_size')}</td>
                <td>{params.get('gamma')}</td>
                <td>{params.get('ent_coef')}</td>
                <td>{params.get('clip_range')}</td>
                <td>{video_tag}</td>
            </tr>
        """
    html += """
        </table>
    </body>
    </html>
    """
    return html

# Serve video files
@app.route('/video/<path:filename>')
def serve_video(filename):
    video_dir = os.path.join(os.path.dirname(__file__), 'videos')
    return send_from_directory(video_dir, filename)

if __name__ == '__main__':
    # Ensure videos directory exists
    os.makedirs(os.path.join(os.path.dirname(__file__), 'videos'), exist_ok=True)
    app.run(host='0.0.0.0', port=5000)

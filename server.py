from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/split', methods=['POST'])
def split_video():
    data = request.get_json()
    video_id = data.get("video_id")

    if not video_id:
        return jsonify({"error": "Missing video_id"}), 400

    # 🧠 Tải video từ YouTube bằng yt-dlp
    os.system(f'yt-dlp -f best -o input.mp4 https://www.youtube.com/watch?v={video_id}')

    # 🎬 Chạy script chia scene
    os.system('python3 scene_split_v2.py')

    return jsonify({"message": f"✅ Đã tải và xử lý video_id: {video_id}!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

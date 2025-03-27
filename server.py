from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🎉 Server is running!", 200

@app.route('/split', methods=['POST'])
def split_videos():
    data = request.get_json()
    video_ids = data.get("video_ids")

    if not video_ids:
        return jsonify({"error": "Missing video_ids"}), 400

    # ✅ Gửi từng video_id vào xử lý scene
    for video_id in video_ids:
        os.system(f'python3 main.py "{video_id}"')

    return jsonify({"message": f"✅ Đã nhận {len(video_ids)} video_id và xử lý scene!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

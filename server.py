from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running!", 200

@app.route('/split', methods=['POST'])
def split_video():
    data = request.get_json()
    video_ids = data.get("video_ids")  # Lấy danh sách video_ids từ yêu cầu

    if not video_ids:
        return jsonify({"error": "Missing video_ids"}), 400

    # Chạy lệnh python3 để xử lý tất cả video trong danh sách video_ids
    for video_id in video_ids:
        os.system(f'python3 main.py {video_id}')  # Gọi lệnh xử lý video

    return jsonify({"message": f"Đã nhận và xử lý các video: {', '.join(video_ids)}!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🎉 Server is running!", 200

@app.route('/split', methods=['POST'])
def split_video():
    data = request.get_json()
    video_id = data.get("video_id")

    if not video_id:
        return jsonify({"error": "Missing video_id"}), 400

    # Gọi lệnh python để xử lý chia scene (chạy file main.py)
    os.system(f'python3 main.py "{video_id}"')

    return jsonify({"message": f"✅ Đã nhận video_id: {video_id} và xử lý chia scene!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

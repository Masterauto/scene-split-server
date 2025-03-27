from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '🎉 Server is running!', 200

@app.route('/split', methods=['POST'])
def split_video():
    data = request.get_json()
    
    video_ids = data.get("video_ids")
    if not video_ids or not isinstance(video_ids, list):
        return jsonify({"error": "Missing or invalid 'video_ids' (expecting list)"}), 400

    print(f"[INFO] Nhận {len(video_ids)} video_id để xử lý...")

    results = []

    for video_id in video_ids:
        print(f"[PROCESSING] 🎬 Đang xử lý video_id: {video_id}")

        try:
            exit_code = os.system(f'python3 main.py "{video_id}"')
            if exit_code == 0:
                results.append({
                    "video_id": video_id,
                    "status": "success"
                })
                print(f"[DONE] ✅ {video_id} xử lý thành công.")
            else:
                results.append({
                    "video_id": video_id,
                    "status": "failed",
                    "error": f"Exit code {exit_code}"
                })
                print(f"[ERROR] ❌ {video_id} lỗi với mã {exit_code}")
        except Exception as e:
            results.append({
                "video_id": video_id,
                "status": "error",
                "error": str(e)
            })
            print(f"[CRASHED] 💥 {video_id} bị lỗi nghiêm trọng: {e}")

    return jsonify({
        "message": "✅ Hoàn tất xử lý tất cả video",
        "results": results
    }), 200

@app.route('/download/<video_id>', methods=['GET'])
def download_video(video_id):
    video_path = f"{video_id}.mp4"
    if os.path.exists(video_path):
        return send_file(video_path, as_attachment=True)
    else:
        return jsonify({"error": f"Không tìm thấy file cho video_id: {video_id}"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

import sys
import time
import os

if __name__ == "__main__":
    video_id = sys.argv[1]
    print(f"[TEST] Đang xử lý video_id: {video_id}")

    # Giả lập xử lý video trong 5 giây
    time.sleep(5)

    # Đảm bảo thư mục output tồn tại
    os.makedirs("output", exist_ok=True)

    # Giả lập tạo file mp4 vào thư mục output/
    output_path = f"output/{video_id}.mp4"
    with open(output_path, "wb") as f:
        f.write(b"Fake MP4 content for testing\n")

    print(f"[DONE] ✅ Video {video_id} đã xử lý xong → output/{video_id}.mp4")

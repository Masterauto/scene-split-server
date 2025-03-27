import sys
import time

if __name__ == "__main__":
    video_id = sys.argv[1]
    print(f"[TEST] Đang xử lý video_id: {video_id}")

    # Giả lập xử lý video
    time.sleep(5)

    # Tạo file .mp4 giả lập để test server download
    with open(f"{video_id}.mp4", "w") as f:
        f.write("Fake video content for testing.\n")

    print(f"[DONE] ✅ Video {video_id} đã xử lý xong.")

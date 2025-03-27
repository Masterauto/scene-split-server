import sys
import time

if __name__ == "__main__":
    video_id = sys.argv[1]
    print(f"[TEST] Đang xử lý video_id: {video_id}")
    
    # Giả lập xử lý video trong 5 giây
    time.sleep(5)
    
    # Ghi file log để kiểm tra
    with open(f"{video_id}_done.txt", "w") as f:
        f.write("✅ Xử lý video thành công!\n")
    
    print(f"[DONE] ✅ Video {video_id} đã xử lý xong.")

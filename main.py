# main.py
import os
import sys
import time
from moviepy.editor import TextClip, CompositeVideoClip

# Nhận video_id từ terminal
video_id = sys.argv[1]
print(f"[TEST] Đang xử lý video_id: {video_id}")

# Tạo thư mục output nếu chưa có
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Tạo video đơn giản bằng moviepy
try:
    # Tạo text clip (giả lập nội dung video)
    txt_clip = TextClip(f"AI Video: {video_id}", fontsize=70, color='white', bg_color='black', size=(1280,720))
    txt_clip = txt_clip.set_duration(5)

    # Ghép thành video
    final_clip = CompositeVideoClip([txt_clip])
    output_path = os.path.join(output_dir, f"{video_id}.mp4")
    final_clip.write_videofile(output_path, fps=24)

    print(f"[DONE] ✅ Video {video_id} đã xử lý xong và lưu tại {output_path}")

except Exception as e:
    print(f"[ERROR] ❌ Không thể xử lý video {video_id}: {str(e)}")
    sys.exit(1)

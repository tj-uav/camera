from picamera2 import Picamera2, Preview
import os
import time
picam2 = Picamera2()
camera_config = picam2.create_still_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.DRM)
picam2.start()
time.sleep(1)
for i in range(1):
   picam2.capture_file(f"./pics/test{i}.jpeg")
   print("oh my")

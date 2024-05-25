import numpy as np
import time
from PIL import Image
import os

from time import sleep

from picamera2 import Picamera2, Preview

# docs at https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf

picam = Picamera2()

preview_config = picam.create_preview_configuration()
picam.configure(preview_config)

picam.start_preview(Preview.DRM)

capture_config = picam.create_still_configuration()

picam.configure(capture_config)

picam.start()
sleep(2)

with picam.controls as ctrl:
    ctrl.AnalogueGain = 1.0
    ctrl.ExposureTime = 400_000
sleep(2)

imgs = input("how many bozo: ")
sumv = None

batchname = int(time.time())
os.mkdir(f"./imgs/{batchname}")

for i in range(int(imgs)):
    print(f"pic {i}")
    img = Image.fromarray(np.uint8(np.longdouble(picam.capture_array())))
    img.save(f"./imgs/{batchname}/{i}.png")

#    if sumv is None:
#        sumv = np.longdouble(picam.capture_array())
#        img = Image.fromarray(np.uint8(sumv))
#        img.save("original.tif")
#    else:
#        sumv += np.longdouble(picam.capture_array())

#img = Image.fromarray(np.uint8(sumv/imgs))
#img.save("averaged.tif")
print("YIPPEE")

from picamera import PiCamera
from picamera import Color
import time

camera=PiCamera()

camera.start_preview()

camera.annotate_text=""
camera.capture('image.jpg')
time.sleep(0.1)
camera.annotate_text_size=100
camera.annotate_foreground=Color('white')
text="Image"
camera.annotate_text=text
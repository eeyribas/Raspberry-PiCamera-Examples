import cv2
import picamera
import picamera.array

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution=(1280, 1080)

        while True:
            camera.capture(stream, 'bgr', use_video_port=True)
            cv2.imshow('Camera Images', stream.array)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            stream.seek(0)
            stream.truncate()
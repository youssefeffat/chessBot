import cv2

class CameraModule:
    def __init__(self, camera_id=0):
        self.camera_id = camera_id
        self.capture = cv2.VideoCapture(self.camera_id)

    def capture_image(self):
        ret, frame = self.capture.read()
        if not ret:
            raise Exception("Failed to capture image from camera.")
        return frame

    def release(self):
        self.capture.release()
import cv2
import time

# This is to open Web-cam
# 0 -> Default/Inbuilt Webcam
video = cv2.VideoCapture(0)

# The below code captures the first frame and prints a numPy array
check, frame = video.read() # check is boolean variable that checks if video can be captured
# print(check)
# print(frame)

# This will open WebCam for 3 Seconds
time.sleep(3)

cv2.imshow("Capturing", frame)  # Print first frame
cv2.waitKey(0)

# This will close WebCam
video.release()

cv2.destroyWindow() # It destroys all windows open


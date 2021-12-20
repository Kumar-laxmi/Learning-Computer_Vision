import cv2
import time

video = cv2.VideoCapture(0)    # 0 for Default Camera(Inbuilt Camera)
a = 1

while True:
    a = a + 1      # Increments Number of Frames
    check, frame = video.read()
    print(frame)    # This prints NumPy Matrix of frames

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # This converts every frame to grey-scale

    cv2.imshow("Capturing..", gray)  # This opens a new window with video
    key = cv2.waitKey(1)  # This generates a new frame after every 1 milli-secondqq

    if key == ord('q'):  # This will cause window to destroy once 'q' is pressed
        break

print(a)   # This will print number of frames ellapsed
video.release()   # This will close video
cv2.destroyWindow()    # This will destroy Window openend
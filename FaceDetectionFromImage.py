import cv2

# Read inbuild cascade XML File
face_cascade = cv2.CascadeClassifier("/Users/kumarlaxmikant/PycharmProjects/pythonProject/venv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml")

# Capture Color Image
img = cv2.imread("/Users/kumarlaxmikant/Downloads/myself.jpeg", 1)

# Convert image to Gray Scale
greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect Faces
faces = face_cascade.detectMultiScale(greyImg, scaleFactor= 1.05, minNeighbors= 5)

print(type(faces))
print(faces)

# To draw rectangular box around faces
for x,y,z,h in faces:
    img = cv2.rectangle(img, (x,y), (x+z,y+h), (0,255,0), 3)

# This is to resize image
# resized = cv2.resize(img, (int(img.shape[1]),int(img.shape[0])))

cv2.imshow("Gray", img)
cv2.waitKey(0)

cv2.destroyWindow() # It destroys all windows open
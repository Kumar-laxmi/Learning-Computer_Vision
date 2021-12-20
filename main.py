import cv2

face_cascade = cv2.CascadeClassifier("/Users/kumarlaxmikant/PycharmProjects/pythonProject/venv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml")
img = cv2.imread("/Users/kumarlaxmikant/Downloads/myself.jpeg", 1)

greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(greyImg, scaleFactor= 1.05, minNeighbors= 5)

print(type(faces))
print(faces)

for x,y,z,h in faces:
    img = cv2.rectangle(img, (x,y), (x+z,y+h), (0,255,0), 3)

resized = cv2.resize(img, (int(img.shape[1]),int(img.shape[0])))

cv2.imshow("Gray", img)
cv2.waitKey(0)

cv2.destroyWindow()

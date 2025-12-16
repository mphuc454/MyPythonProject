import cv2

path = r"D:\ThuMucCuaTui\Programmer\PythonApp\img\AirportImg.jpg"
img = cv2.imread(path)
cv2.imshow('Image Original', img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
cv2.imshow('HS Image', img)
cv2.waitKey(0)

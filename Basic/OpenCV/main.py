import cv2 as cv
img = cv.imread("path/to/image")

cv.imshow("Display window", img)
k = cv.waitKey(0)
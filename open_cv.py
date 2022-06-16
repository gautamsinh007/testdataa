import cv2 as cv
import os

img = cv.imread('/Users/yudiz/Desktop/open_cv/a.jpeg')

img = cv.resize(img ,(600, 400))
cv.imshow('lion',img)

cv.waitKey(0)


data = os.listdir('images')
path = r"""/Users/yudiz/Desktop/open_cv/images"""

for i  in 

print(data)



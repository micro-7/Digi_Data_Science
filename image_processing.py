import cv2
import numpy as np

#read image
naruto = r'C:\Users\mihir\Downloads\Boeing-Dreamliner-d4291b6.jpg'
img = cv2.imread(naruto)
if img is None:
    print('Could not open or find the image:', naruto)
    exit(0)
print('type', type(img))
print('shape', img.shape)

#resize image by width and height
img_200= cv2.resize(img,(200,150))
#resize image by scale
img_25pct= cv2.resize(img, (0,0), fx=0.25, fy=0.25)

#filters- grayscale,edge detection, bgrtorgb
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_rgb= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_edge= cv2.Canny(img, 100,200)

#DISPLAY IMAGE

cv2.imshow('image gray',img_gray)
cv2.imshow('image rgb', img_rgb)
cv2.imshow('image', img)
cv2.imshow('image edge', img_edge)
cv2.waitKey(0)
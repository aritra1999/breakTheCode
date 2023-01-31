import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
  
img = cv2.imread('download.png') 
img = cv2.medianBlur(img,5)
  
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

cv2.imshow('image', img) 
cv2.waitKey(0)  
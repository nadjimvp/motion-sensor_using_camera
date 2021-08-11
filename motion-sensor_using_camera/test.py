#sorry for the gramemr in advance 
import cv2
import time
from pyautogui import *
import pyautogui
from PIL import Image
import numpy as np
from skimage import color
#i'll use this fonction in order to evaluate the diffrence between two images 
#comparing pixel par pixel 
def imagesDifference( imageA, imageB ):
    diff=0.00
    A = color.rgb2gray(imageA)
    B = color.rgb2gray(imageB)
    if (len(A) != len(B)): return -1
    diff = []
    for i in range(0, len(A)):
        diff += [abs(A[i][0] - B[i][0]), abs(A[i][1] - B[i][1]), abs(A[i][2] - B[i][2])]
    return (np.sum(diff))

camera = cv2.VideoCapture(0)
n=0
while True:
    name="image"
    #i'll take two images with a time intervale of 1 second 
    return_value,image = camera.read()
    time.sleep(1)
    return_value,image2 = camera.read()
    #gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('image',gray)
    cv2.imwrite('test.jpg',image)
    cv2.imwrite('test2.jpg',image2)
    cmp=imagesDifference( image, image2 )
    #print(cmp)
    sensetivity=40
    #the lower the sensetivity the more sesetive to movment the code will get 
    if cmp>sensetivity:
       n=n+1
       namemvt=name+str(n)+'.jpg'
       sleep(0.1)
       cv2.imwrite(namemvt,image)
camera.release()
cv2.destroyAllWindows()
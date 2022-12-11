import numpy as np
import cv2
import os

weights=[0]*256
weights=np.array(weights)
weights=np.reshape(weights,(16,-1))

for circle in os.listdir("images/circle"):
    f=os.path.join("images/circle",circle)
    img=cv2.imread(f,cv2.IMREAD_GRAYSCALE)
    img//=255
    img=np.array(img)
    weights+=img
for rect in os.listdir("images/rect"):
    f=os.path.join("images/rect",rect)
    img=cv2.imread(f,cv2.IMREAD_GRAYSCALE)
    img//=255
    img=np.array(img)
    weights-=img

img=cv2.imread("images/rectangle6.png",cv2.IMREAD_GRAYSCALE)
img//=255
img=np.array(img)
img=np.ravel(img)
if np.dot(img,weights.ravel())>0:
    print("Circle")
else:
    print("Rectangle")
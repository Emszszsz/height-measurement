import numpy as np
import cv2
import time
from PIL import Image

cap = cv2.VideoCapture(0)
sigma = 0.1
low_threshold = 100
high_threshold = 150
i=0

while(i<400):
    ret, frame = cap.read()
    cv2.imshow('capture', frame)
    i=i+1
    if (cv2.waitKey(1) & 0xFF == ord('q')) or i == 99:
        im = cv2.imwrite('C:/Users/emili/OneDrive/Desktop/size-of-objects/size-of-objects/images/frame.jpg', frame)
        break
cap.release()
cv2.destroyAllWindows()

image = Image.open('C:/Users/emili/OneDrive/Desktop/size-of-objects/size-of-objects/images/frame.jpg')
image.crop((0, 0, 100, 100))
image.load()
image.save('C:/Users/emili/OneDrive/Desktop/size-of-objects/size-of-objects/images/frame.jpg', "JPEG")

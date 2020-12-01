import cv2
import numpy as np

def transdilate():
    image = cv2.imread("Data/imgs/schtroumpf.jpg")
    kernel = np.ones((15, 15), np.uint8)
    dilate = cv2.dilate(image, kernel, iterations=1)
    cv2.imwrite("Data/output/schtroumpf-dilate.jpg", dilate)
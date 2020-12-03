import os
import cv2
import numpy as np


def transdilate(src, x, out):
    try:
        tmp = src[-4]
        for i in [-3, -2, -1]:
            tmp = tmp + src[i]
        if tmp == '.jpg' or tmp == '.png':
            image = cv2.imread(src)
            kernel = np.ones((x, x), np.uint8)
            dilate = cv2.dilate(image, kernel, iterations=1)
            cv2.imwrite(out, dilate)
        else:
            print(f'Not an image. EXTENSION={tmp} IN {src}')

    except cv2.error as e:
        print(f'ERROR={e}')
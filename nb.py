"""The module allowing to tranform a colored image into a black and white one"""
import cv2

def transnb(src, out):
    """
    Appplies a black and white filter to an image
    :param src: The image to be turned grey
    :param out: The directory where the transformed images are stored
    """
    try:
        tmp = src[-4]
        for i in [-3, -2, -1]:
            tmp = tmp + src[i]
        if tmp == '.jpg' or tmp == '.png':
            image = cv2.imread(src)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # cv2.imshow('Original image', image)
            # cv2.imshow('Gray image', gray)
            cv2.imwrite(out, gray)
            return
        else:
            print(f'Not an image. EXTENSION={tmp} IN {src}')
    except cv2.error as e:
        print(f'ERROR={e}')
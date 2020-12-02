import cv2

def transnb(src, out):
    try:
        tmp = src[-4]
        for i in [-3, -2, -1]:
            tmp = tmp + src[i]
        if tmp == '.jpg' or tmp == '.png':
            print('IMG B&W')
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
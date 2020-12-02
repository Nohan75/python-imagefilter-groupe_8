import cv2

def transblur(x):
    try:
        src = 'Data/imgs/schtroumpf.jpg'
        tmp = src[-4]
        for i in [-3, -2, -1]:
            tmp = tmp + src[i]
        if tmp == '.jpg' or tmp == '.png':
            print('IMG BLUR')
            image = cv2.imread(src, cv2.IMREAD_UNCHANGED)
            if x < 0 or x % 2 == 0:
                print('Enter an odd and positive value')
                return
            else:
                blur = cv2.GaussianBlur(image,(x,x),0)
            # cv2.imshow("Blured Image", blur)
            cv2.imwrite("Data/output/schtroumpf_blured.jpg", blur)
            return
        else:
            print(f'Not an image. EXTENSION={tmp} IN {src}')
    except cv2.error as e:
        print(f'ERROR={e}')
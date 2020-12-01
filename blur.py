import cv2

def transblur():
    image = cv2.imread("Data/imgs/schtroumpf.jpg")
    src = cv2.imread('Data/imgs/schtroumpf.jpg', cv2.IMREAD_UNCHANGED)
    blur = cv2.GaussianBlur(src,(5,5),0)
    cv2.imshow("Blured Image", blur)
    cv2.imwrite("Data/output/schtroumpf_blured.jpg", blur)
    return
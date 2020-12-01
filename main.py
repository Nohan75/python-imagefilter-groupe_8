import cv2

image = cv2.imread("Data/imgs/schtroumpf.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image', image)
cv2.imshow('Gray image', gray)

cv2.imwrite("Data/output/schtroumpf_grey.jpg", gray)

src = cv2.imread('Data/imgs/schtroumpf.jpg', cv2.IMREAD_UNCHANGED)

blur = cv2.GaussianBlur(src,(5,5),0)
cv2.imshow("Blured Image", blur)
cv2.imwrite("Data/output/schtroumpf_blured.jpg", blur)

cv2.destroyAllWindows()


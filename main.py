import cv2

image = cv2.imread("Data/imgs/schtroumpf.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image', image)
cv2.imshow('Gray image', gray)

cv2.imwrite("Data/output/schtroumpf_grey.jpg", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


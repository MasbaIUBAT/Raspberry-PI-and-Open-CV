import cv2

img = cv2.imread('img 4.jpg')
rows, cols, channels = img.shape
roi = img[0:rows, 0:cols]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bool, mask = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)
trans = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('binary', mask)
cv2.imshow('transperent', trans)


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('transfower.png',trans)

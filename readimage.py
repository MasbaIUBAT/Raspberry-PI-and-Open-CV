import cv2

img = cv2.imread('tower.jpg')

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
frame = img [55:170, 80:200]
img[500:615, 400:520] = frame

cv2.imshow('image', img)
'''cv2.imshow('gray', gray)
cv2.imshow('rgb', rgb)'''

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('gray.png', gray)


import cv2
import numpy

img = cv2.imread('tower.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (20,10), (100,200), (255,0,0) ,3)
#image, start point, end point, color, thikness
cv2.rectangle(img, (15,25), (200,150), (0,255,0), -1)
#image, start point, end point, color, thikness
cv2.circle(img, (400,400), 40, (0,0,255), -1)
#image, center, radius, color, thikness
dots = numpy.array([[20,30], [80,90], [200,180], [300,400]], numpy.int32)
cv2.polylines(img, [dots], True, (255,255,255), 3)
#image, dots, if want to complete, color, thikness
convexhull = cv2.convexHull (numpy.array([[300, 605], [56,67], [400,100], [180,251], [522,451]]))
cv2.drawContours(img, [convexhull], -1, (200,100,255), 5)
#image, array of dots, wanted points to be drawn, color, thikness
cv2.putText(img, "I AM GROOT", (150, 120),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (20, 200, 255), 2)
cv2.imshow('drawing', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



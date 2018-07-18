import cv2
import numpy

def nothing(x):
	pass
	
cv2.namedWindow('Trackbar')

stream = cv2.VideoCapture(0)
stream.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

cv2.createTrackbar('LHue','Trackbar', 150, 255, nothing)
cv2.createTrackbar('LSat','Trackbar', 150, 255, nothing)
cv2.createTrackbar('LValue','Trackbar', 50, 255, nothing)
cv2.createTrackbar('UHue','Trackbar', 179, 179, nothing)
cv2.createTrackbar('USat','Trackbar', 255, 255, nothing)
cv2.createTrackbar('UValue','Trackbar', 200, 255, nothing)

while True:

	_,frame = stream.read()
	
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	LHue = cv2.getTrackbarPos('LHue', 'Trackbar')
	LSat = cv2.getTrackbarPos('LSat', 'Trackbar')
	LValue = cv2.getTrackbarPos('LValue', 'Trackbar')
	UHue = cv2.getTrackbarPos('UHue', 'Trackbar')
	USat = cv2.getTrackbarPos('USat', 'Trackbar')
	UValue = cv2.getTrackbarPos('UValue', 'Trackbar')
	
	lbound = numpy.array([LHue,LSat,LValue])
	ubound = numpy.array([UHue,USat,UValue])
	
	mask = cv2.inRange(hsv, lbound, ubound)
	res = cv2.bitwise_and(frame, frame, mask = mask)
	
	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	
	if cv2.waitKey(5) & 0xFF == 27:
		break

cv2.destroyAllWindows()
stream.release()
	
import cv2
import numpy

def is_circ(ob):
	peri = cv2.arcLength(ob, True)
	approx = cv2.approxPolyDP(ob, 0.04 * peri, True)
	if len(approx) < 3 or len(approx) > 5:
		return True
	else:
		return False

stream = cv2.VideoCapture(0)
stream.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
while True:
	_, frame = stream.read()
	#gauss = cv2.GaussianBlur(frame, (11, 11), 0)
	median = cv2.medianBlur(frame, 11)
	#bilateral = cv2.bilateralFilter(frame, 11, 75, 75)
	hsv = cv2.cvtColor(median, cv2.COLOR_BGR2HSV)
	lred = numpy.array([150,123,40])
	ured = numpy.array([179,255,102])
	
	mask = cv2.inRange(hsv, lred, ured)
	res = cv2.bitwise_and(frame, frame, mask = mask)
	
	#dummy = numpy.ones((5,5), numpy.uint8) 
	#erode = cv2.erode(mask, None, iterations =2)
	#dilate = cv2.dilate(mask, None, iterations = 2)
	
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, None)
	#closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, dummy)

	cnts = cv2.findContours(opening.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[1]
	center = None

	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		if is_circ(c):	
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 

			if radius > 10:

				cv2.circle(frame, (int(x), int(y)), int(radius),
							(0, 255, 255), 2)
				cv2.circle(frame, center, 5, (0, 0, 255), -1)
	cv2.imshow('frame',frame)
	#cv2.imshow('mask',mask)
	#cv2.imshow('res',res)
	#cv2.imshow('erode',erode)
	#cv2.imshow('dilate',dilate)
	#cv2.imshow('opening',opening)
	#cv2.imshow('closing',closing)
	
	if cv2.waitKey(5) & 0xFF == 27:
		break

cv2.destroyAllWindows()
stream.release()
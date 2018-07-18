import cv2
import time

input = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('video' + time.strftime("%Y%m%d-%H%m%s")+'.avi',
						codec, 20.0, (640, 480))

while 1:
	bool, frame = input.read()
	video.write(frame)
	cv2.imshow('video', frame)
	
	if cv2.waitKey(5) & 0xFF == 27:
		break

input.release()
video.release()
cv2.destroyAllWindows()


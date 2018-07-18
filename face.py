import io
import picamera
import cv2
import numpy
import time

#Create a memory stream so photos doesn't need to be saved in a file
stream = io.BytesIO()

#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters (e.g.:rotate the image)
with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.capture(stream, format='jpeg')

#Convert the picture into a numpy array
buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

#Now creates an OpenCV image
image = cv2.imdecode(buff, 1)

#image = cv2.imread('ironman.jpg', cv2.IMREAD_COLOR)
#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Convert to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Look for faces in the image using the loaded cascade file
faces = face_cascade.detectMultiScale(gray, 1.3, 2)

print ("Found "+str(len(faces))+" face(s)")

#Draw a rectangle around every found face
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
    cv2.putText(image, "I AM IRONMAN", (x-10, y-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (20, 200, 255), 2)

#Save the result image
cv2.imwrite('result '+time.strftime("%Y%m%d-%H%m%s")+'.jpg',image)

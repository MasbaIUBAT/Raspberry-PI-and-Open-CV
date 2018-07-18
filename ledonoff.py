import RPi.GPIO as GPIO       				#import GPIO library
import time				#import time library
import sys
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)				#use board pin numbers


GPIO.setup(11, GPIO.OUT)				#setup pin 11 as output
#GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
	for x in range (0,10):			#repeat for x=0 to 9
		GPIO.output(11, True)			#set pin 11 high
		time.sleep(2)				#wait 2 seconds
		GPIO.output(11, False)			#set pin 11 low
		time.sleep(2)				#wait 2 seconds
except (KeyboardInterrupt,SystemExit):
	GPIO.cleanup()
	sys.exit()
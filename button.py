import RPi.GPIO as GPIO       				#import GPIO library
import time						#import time library
import sys
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)				#use board pin numbers

GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)
try:
	while True:
		if(GPIO.input(12) == False):
			print("Button pressed")
			time.sleep(0.2)
except (KeyboardInterrupt, SystemExit):
	GPIO.cleanup()
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # set GPIO in Broadcom mode

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set GPIO 18 as input and trigger False when pushed
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW) # set GPIO 17 as output and start with the output LOW

try:
    while True:
        state = GPIO.input(18)
        if state == False: # on push
            if GPIO.input(17):   # checks if the pin is HIGH
                GPIO.output(17,GPIO.LOW)
                print('Off')
            else:
                GPIO.output(17,GPIO.HIGH)
                print('On')
            time.sleep(0.5) # wait half second for changing states
except (KeyboardInterrupt, SystemExit):
    GPIO.cleanup()
    raise
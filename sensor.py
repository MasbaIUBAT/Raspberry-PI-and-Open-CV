#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
data_log = open('/var/www/html/report.csv','r') 
lines = data_log.readlines()
data_log.close()
 
sensor_qty = 1     # how many sensor lines to read in from log
 
html_string = '<html>\n<body>\n<style>\ntable { \n  border-spacing: 10px;\n'
html_string += '  border-collapse: separate;\n}\n</style>\n'
html_string += '\n<table>\n<tr align="center">\n<th>Location</th>'
html_string += '<th>Temp</th><th>Date</th><th>Time</th></tr>\n'
 
for x in range(-sensor_qty, 0, 1):
    line = lines[x].split(',')

    ipsrc = line[0]
    temp,noise,co2,pulse,movement = float(line[1]))
 
    html_string += '<tr><td align="right">'
    html_string += line[0]
    html_string += '</td><td align="right">'
    html_string += line[1]
    html_string += '&deg;C </td>'
    html_string += '<td align="right">'
    html_string += line[2]
    html_string += '<td align="right"> '
    html_string += line[3]
    html_string += '</td></tr>\n'
 
html_string += '</table>\n\n</body>\n</html>'
 
html_file = open('/var/www/html/temps.html','a') 
html_file.write(html_string)
html_file.close()
print(temp,pulse)
if temp>33:
    GPIO.output(11, True)
    time.sleep(10)
    GPIO.output(11, False)

GPIO.cleanup()

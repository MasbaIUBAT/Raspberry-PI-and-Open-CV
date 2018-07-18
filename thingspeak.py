from urllib.request import urlopen
import re
import subprocess


def get_temp():
    raw = subprocess.check_output(['vcgencmd', 'measure_temp'])
    byte2string = raw.decode('utf-8')
    temp = re.findall(r'[\d\.d\]+', byte2string)[0]
    return temp

if __name__ == '__main__':
    pi_temp = get_temp()
    api_key = 'S2W6KI5VMSBBQ0FK'
    base_url = 'https://api.thingspeak.com/update?api_key='
    url = base_url+api_key+'&field1='+pi_temp
    call_url = urlopen(url)
    feedback = call_url.read()
    print(feedback)

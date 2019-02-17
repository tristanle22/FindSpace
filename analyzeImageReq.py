import requests
import subprocess
import os
import json
import threading
import time
import mraa
from subprocess import Popen, PIPE
import GPIOLibrary

try:
    Pin23 = GP.getPin23()
    Pin23.out()

    Pin24 = GP.getPin24()
    Pin24.out()	

    for i in range(0,20):
        pinValue = Pin29.getValue()
	
        if pinValue == 1:
            Pin27.high()
        else:
            Pin27.low()
        time.sleep(1)

finally:
    GP.cleanup()

url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/0a95ed60-d8e4-4e5e-998a-787d8021e776/image?iterationId=dbb6c4cd-454f-4907-9dd3-9c14fbd02d92"
headers = {"prediction-Key": 'f24c0306b1ac4e0784ac5566960105de', "Content-Type": "application/octet-stream"}
print(mraa.getVersion())

def capture():
    #subprocess.run('ffmpeg -i /dev/video0 -frames 1 ./output.jpg')
    #os.system('ffmpeg -i /dev/video0 -frames 1 ./output.jpg')
    p = os.popen('ffmpeg -i /dev/video0 -frames 1 ./output.jpg', "w")
    p.write("y\n")
    image = open("output.jpg", "rb")
    resp = requests.post(url, headers=headers, data=image)
    output = resp.text
    return getParkingStatusFromJson(output)


def getParkingStatusFromJson(jsonData):
    data = json.loads(jsonData)
    for i in data['predictions']:
        print(i['probability'])
        if i['probability'] >= 0.20:
            return True
    return False


def controlLed(isEmpty):
    led = [mraa.Gpio(24), mraa.Gpio(25)]
    for x in led:
        x.dir(mraa.DIR_OUT)
        x.write(0)
        if (isEmpty):
            led.write(1)
        else:
            led.write(0)

def runCapture(n):
    controlLed(capture())
    for i in range(0, n-1):
        time.sleep(15)
        controlLed(capture())


runCapture(5)

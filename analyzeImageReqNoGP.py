import requests
import subprocess
import os
import json
import threading
import time

url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/0a95ed60-d8e4-4e5e-998a-787d8021e776/image?iterationId=dbb6c4cd-454f-4907-9dd3-9c14fbd02d92"
headers = {"prediction-Key": 'f24c0306b1ac4e0784ac5566960105de', "Content-Type": "application/octet-stream"}


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
            return "Empty Spot Available"
    return "No Spots :("


def runCapture(n):
    print(capture())
    for i in range(0, n-1):
        time.sleep(15)
        print(capture())


runCapture(5)

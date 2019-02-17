import requests
import subprocess
import os
import json
import threading
import time
from subprocess import Popen, PIPE
url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/0a95ed60-d8e4-4e5e-998a-787d8021e776/image?iterationId=dbb6c4cd-454f-4907-9dd3-9c14fbd02d92"
headers = {"prediction-Key": '88724618479e49e4939ac9548e804782', "Content-Type": "application/octet-stream"}

signal = False
def capture():
    #subprocess.run('ffmpeg -i /dev/video0 -frames 1 ./output.jpg')
    #os.system('ffmpeg -i /dev/video0 -frames 1 ./output.jpg')
    #p = os.popen('ffmpeg -i /dev/video0 -frames 1 ./output.jpg', "w")
    #p.write("y\n")
    p = Popen(["ffmpeg", "-i", "/dev/video0", "-frame", "./output.jpg"], shell=True, stdin=PIPE)
    p.stdin.write("y/n")
    image = open("output.jpg", "rb")
    resp = requests.post(url, headers=headers, data=image)
    output = resp.text
    setSignalStatus(parseJson(output))
    print(signal)

def parseJson(jsonData):
    data = json.loads(jsonData)
    for i in data['predictions']:
        print(i['probability'])
        if i['probability'] >= 0.20:
            return True
    return False

def setSignalStatus(state):
    signal = state

def runCapture():
    for i in range(0, 3):
        capture()
        time.sleep(15)

runCapture()


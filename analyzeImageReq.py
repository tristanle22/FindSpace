import requests
import subprocess
import os
import base64
url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/0a95ed60-d8e4-4e5e-998a-787d8021e776/image?iterationId=dbb6c4cd-454f-4907-9dd3-9c14fbd02d92"
headers = {"prediction-Key": '88724618479e49e4939ac9548e804782', "Content-Type": "application/octet-stream"}


def capture():
    #subprocess.run('ffmpeg -i /dev/video0 -frames 1 ./output.jpg')
    os.system('ffmpeg -i /dev/video0 -frames 1 ./output.jpg')
    with open("../Documents/output.jpg", "rb") as img:
        req = requests.post(url, files={"../Documents/output.jpg": img}, headers=headers)
    output = req.text
    print(output)


capture()

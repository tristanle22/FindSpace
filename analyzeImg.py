import urllib
import subprocess

url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/" \
      "0a95ed60-d8e4-4e5e-998a-787d8021e776/image?iterationId=8115342a-7571-4f99-bd30-35a2a93521a4"
headers = {"prediction-Key": '88724618479e49e4939ac9548e804782', "Content-Type": "application/octet-stream"}



def capture():
    subprocess.run('ffmpeg -i /dev/video0 -frames 1 ./output.jpg')
    img = open('output.jpg', 'rb')
    files = {'file': img}
    req = urllib.Request(url, files, headers)
    response = urllib.urlopen(req)
    output = response.read()
    print(output)

capture()
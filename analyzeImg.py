
import urllib.parse
import urllib.request
import subprocess
import base64

url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/" \
      "0a95ed60-d8e4-4e5e-998a-787d8021e776/image?iterationId=8115342a-7571-4f99-bd30-35a2a93521a4"
headers = {"prediction-Key": '88724618479e49e4939ac9548e804782', "Content-Type": "application/octet-stream"}


def capture():
    subprocess.run('ffmpeg -i /dev/video0 -frames 1 ./output.jpg')
    with open("../Documents/output.jpg", "rb") as img:
        encodedImg = base64.b64decode(img.read());
    data = urllib.parse.urlencode({"image": encodedImg})
    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req)
    output = response.read()
    print(output)


capture()
"""
Traceback (most recent call last):
  File "analyzeImg.py", line 23, in <module>
    capture()
  File "analyzeImg.py", line 18, in capture
    response = urllib.request.urlopen(req)
  File "/usr/lib/python3.4/urllib/request.py", line 153, in urlopen
    return opener.open(url, data, timeout)
  File "/usr/lib/python3.4/urllib/request.py", line 453, in open
    req = meth(req)
  File "/usr/lib/python3.4/urllib/request.py", line 1104, in do_request_
    raise TypeError(msg)
TypeError: POST data should be bytes or an iterable of bytes. It cannot be of type str.
"""

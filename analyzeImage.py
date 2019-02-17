import urllib
import pygame
import pygame.camera

url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/" \
      "0a95ed60-d8e4-4e5e-998a-787d8021e776/image?iterationId=8115342a-7571-4f99-bd30-35a2a93521a4"
headers = {"prediction-Key": '88724618479e49e4939ac9548e804782', "Content-Type": "application/octet-stream"}


def capture():
    cam = startCamera()
    img = cam.get_image()
    files = {'file': img}
    req = urllib.request.Request(url, files, headers)
    response = urllib.request.urlopen(req)
    output = response.read()
    print(output)


def startCamera():
    pygame.init()
    pygame.camera.init()
    camlist = pygame.camera.list_cameras()
    if camlist:
        cam = pygame.camera.Camera(camlist[0], (640, 480))
    cam.start()
    return cam


capture()




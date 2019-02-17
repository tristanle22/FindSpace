import urllib
import threading
import pygame
import time
import logging


"""class detectParkingSpot():
    url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/" \
          "0a95ed60-d8e4-4e5e-998a-787d8021e776/image?iterationId=8115342a-7571-4f99-bd30-35a2a93521a4"
    headers = {"prediction-Key": '88724618479e49e4939ac9548e804782', "Content-Type": "application/octet-stream"}

    def main(self):
        cam = self.startCamera()
        img = cam.get_image()
        files = {'file': open(img, 'rb')}
        req = urllib.Request(self.url, files, self.headers)
        response = urllib.urlopen(req)
        output = response.read()

        print('output')

    def startCamera(self):
        pygame.init()
        pygame.camera.init()
        cam = pygame.camera.Camera('/dev/video0')
        cam.start()
        return cam"""


url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/" \
    "0a95ed60-d8e4-4e5e-998a-787d8021e776/image?iterationId=8115342a-7571-4f99-bd30-35a2a93521a4"
headers = {"prediction-Key": '88724618479e49e4939ac9548e804782', "Content-Type": "application/octet-stream"}

def main():
    cam = startCamera()
    img = cam.get_image()
    files = {'file': open(img, 'rb')}
    req = urllib.Request(url, files, headers)
    response = urllib.urlopen(req)
    output = response.read()

    print('output')

def startCamera():
    pygame.init()
    pygame.camera.init()
    cam = pygame.camera.Camera('/dev/video0')
    cam.start()
    return cam

if __name__ == "__name__":
    main()





import requests
import cv2
import numpy as np
import imutils

url = "http://192.168.**.***:8080/shot.jpg" #Add your router's IP

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content))
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width = 1920, height = 1080)
    cv2.imshow("Android_cam", img)

    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()

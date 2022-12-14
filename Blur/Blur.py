import cv2
 
cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('C:\\Users\\Mudar\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\data\\haarcascade_frontalface_default.xml')
 
while True:
    success,img = cap.read()
    faces = faceCascade.detectMultiScale(img,1.2,4)
    for (x, y, w, h) in faces:

        # To make a face blurred
        ROI = img[y:y+h, x:x+w]
        blur = cv2.GaussianBlur(ROI, (91,91),0)
        # Insert ROI back into image
        img[y:y+h, x:x+w] = blur
 
        # To make a bounding box #*(Not Necessary)
        # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
    if faces==():
        cv2.putText(img,'No Face Found!',(20,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    cv2.imshow('Face Blur',img)
    rval, frame = cap.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
# Turn camera off        
cap.release()
# Close camera window
cv2.destroyAllWindows("Face blur")
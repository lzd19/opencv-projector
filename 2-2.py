import cv2
cap=cv2.VideoCapture(0)
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')
smile=cv2.CascadeClassifier('haarcascade_smile.xml')
while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
        eyes = eye.detectMultiScale(gray,1.16,35,cv2.CASCADE_SCALE_IMAGE,(25,25))
        for (x,y,w,h) in eyes:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
            smiles = smile.detectMultiScale(gray,1.16,35,cv2.CASCADE_SCALE_IMAGE,(25,25))
            for (x,y,w,h) in smiles:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
    #cv2.namedWindow('camera',0)
    cv2.imshow('camera',img)
    if cv2.waitKey(100) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyWindow()

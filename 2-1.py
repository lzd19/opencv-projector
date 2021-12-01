import cv2
import os
path='./CatDog/'
recornations='./recornations/'
for file in os.listdir(path):
    src=path+file
    img=cv2.imread(src)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    catface=cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
    recornation=catface.detectMultiScale(gray)
    for (x,y,w,h) in recornation:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(img, 'cat', (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 0), 2)
        if x!=0:
            cv2.imwrite(recornations+file,img)
    print(recornation)
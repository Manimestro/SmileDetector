import cv2
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
trained_smile_data=cv2.CascadeClassifier('haarcascade_smile.xml')
cam=cv2.VideoCapture(0)
img=cv2.imread('pexels-italo-melo-2379004.jpg')
while True:
    is_OK,img=cam.read()
    grayscaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)
    smile_coordinates=trained_smile_data.detectMultiScale(grayscaled_img, scaleFactor=1.7 , minNeighbors=20 )
    if not is_OK:
        break
    for x,y,w,h in face_coordinates:
        print(x,y,w,h)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        for a,b,c,d in smile_coordinates:
            print(a,b,c,d)
            print("------------")
            if (a>x and (a-x)<w) and (b>y and (b-y)<h) and (c<w and d<h):
                print("hi")
                cv2.rectangle(img,(a,b),(a+c,b+d),(0,255,0),2)
    cv2.imshow("manikanta",img)
    keys=cv2.waitKey(1) 
    if keys==81 or keys==113:
        break
cam.release()
print("Code Completed")
# python3 Smile.py 
import cv2
capture =cv2.VideoCapture(0)
while True:
    ret,frame=capture.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret==False:
        continue
    cv2.imshow("Video Frame",gray_frame)
    cv2.imshow("GRay Frame",frame)
    #wait for user input-q,then you will stop the loop
    key_pressed=cv2.waitKey(1)& 0xFF#converting 32 bit into 8 bit no

    if key_pressed==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

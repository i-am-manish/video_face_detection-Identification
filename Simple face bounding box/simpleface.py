import cv2
import sys
faceCascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#img = cv2.imread(image)
video_capture = cv2.VideoCapture(0)
#You can also provide a filename here, and Python will read in the video file. 
#However, you need to have ffmpeg installed for that since OpenCV itself cannot decode compressed video. 
#Ffmpeg acts as the front end for OpenCV, and, ideally, it should be compiled directly into OpenCV. 
#This is not easy to do, especially on Windows.

while True:

    ret,frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags=cv2.CV_HAAR_SCALE_IMAGE
)


    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release() 
cv2.destroyAllWindows()

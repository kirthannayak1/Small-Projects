import cv2
 #detect face points
face_cap= cv2.CascadeClassifier("C:/Users/HP/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml")  

video_cap=cv2.VideoCapture(0)  #enable camera
while True:
    ret, video_data=video_cap.read()    #read run time image
    col=cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)         #Convert to Greyscale 
    #face structure-create a frame for face
    faces=face_cap.detectMultiScale( col,
                                    scaleFactor=1.1,
                                    minNeighbors=5,
                                    minSize=(30, 30),
                                    flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(255,255,255),2)   #attributes of frame(x,y,width,height)
         # Display the number of faces detected
        text = f"Faces detected: {len(faces)}"
        cv2.putText(video_data, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Live Video",video_data)   #show the images
    if cv2.waitKey(10) == ord("x"):          #stop capturing when you press x
        break
video_cap.release()
cv2.destroyAllWindows()



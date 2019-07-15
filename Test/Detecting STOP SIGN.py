#import the neccessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera 
import time
import cv2


#Initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size = (640, 480))

#initialize the stop sign cascade
stop_cascade = cv2.CascadeClassifier("./cascades/stop_sign.xml")

#allow the camera to warmup
time.sleep(0.1)

#capture frames from the camera 
for frame in camera.capture_continuous(rawCapture, format = "bgr", use_video_port = True):
	
	#grab the raw numpy array representing the image, then initialize the timestamp
	#and occupied/ unoccupied text
	frame = frame.array
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	stop_signs = stop_cascade.detectMultiScale(gray,1.3,5)
	
	for(x,y,w,h) in stop_signs:
		img = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
		cv2.putText(img,"STOP SIGN W: " + str(w) + " H: " + str(h), (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 2)
	
	#show the frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) && 0xFF
	
	#clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	
	#if the 'q' key was pressed, break from the loop
	if(key == ord("q")):
		break

cv2.destroyAllWindows()

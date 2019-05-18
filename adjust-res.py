import cv2
import numpy as np
cap = cv2.VideoCapture(0)

def make_480():
	cap.set(3,680)
	cap.set(4,480)

def make_720():
	cap.set(3,1280)
	cap.set(4,720)

def change_res(width, height):
	cap.set(3, width)
	cap.set(4, height)

def rescale_frame(frame, percent=75):
	scale_percent =75
	width = int(frame.shape[1]*scale_percent/100)
	height = int(frame.shape[0]*scale_percent/100)
	dim = (width,height)
	return cv2.resize(frame,dim, interpolation = cv2.INTER_AREA)
while (True):
	#capture frame by frame

	ret, frame = cap.read()
	frame = rescale_frame(frame, percent=80)
	# display the frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

# when everthing is done
cap.release()
cv2.destroyAllWindows()



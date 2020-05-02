# import libraries
from vidgear.gears import CamGear
import cv2

# https://stackoverflow.com/questions/58527145/opencv-hls-youtube-stream-stops-after-a-couple-frames


stream = CamGear(source='https://youtu.be/9Auq9mYxFEE', y_tube =True,  time_delay=5, logging=True).stream() # YouTube Video URL as input
print(stream)
cv2.VideoCapture
# infinite loop
while True:
	
	frame = stream.read()
	# read frames

	# check if frame is None
	if frame is None:
		#if True break the infinite loop
		break
	
	# do something with frame here
	
	cv2.imshow("Output Frame", frame)
	# Show output window

	key = cv2.waitKey(1) & 0xFF
	# check for 'q' key-press
	if key == ord("q"):
		#if 'q' key-pressed break out
		break

cv2.destroyAllWindows()
# close output window

stream.stop()
# safely close video stream.
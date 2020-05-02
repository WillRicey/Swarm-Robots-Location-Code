# import libraries
import pafy
import cv2

# https://stackoverflow.com/questions/58527145/opencv-hls-youtube-stream-stops-after-a-couple-frames


url = "https://www.twitch.tv/thenuel2"
video = pafy.new(url)
best = video.getbest(preftype="mp4")

capture = cv2.VideoCapture()
capture.open(best.url)

# Looping forever
while capture.isOpened():
	success, frame = capture.read()
	if not success:
		break

  	# show frame
	cv2.imshow('Livestream', frame)
  
  	# quit on ESC button
	if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed
		break
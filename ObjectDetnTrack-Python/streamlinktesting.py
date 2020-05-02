import streamlink
import cv2

url = 'https://twitch.tv/thenuel2'

streams = streamlink.streams(url)
print(streams)
#cap = cv2.VideoCapture(streams["360p"].url)
cap = cv2.VideoCapture(streams["720p"].url)

# Looping forever
while cap.isOpened():
	success, frame = cap.read()
	if not success:
		break

  	# show frame
	cv2.imshow('Livestream', frame)
  
  	# quit on ESC button
	if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed
		break

cap.release()
cv2.destroyAllWindows()
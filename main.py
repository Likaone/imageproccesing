import cv2
import numpy as np

video = cv2.VideoCapture(0)
#background_video = cv2.VideoCapture("street.mp4")

while True:
	check, original_frame = video.read()
	
	if check:
		# check, background = background_video.read()

		background = cv2.imread('img.jpg')
		background = cv2.resize(background, (1280,720))

		image_copy = np.copy(original_frame)
		cv2.imshow("copy image", image_copy)

		lower_green = np.array([0, 50, 0])
		upper_green = np.array([175, 230, 50])

		mask = cv2.inRange(image_copy, lower_green, upper_green)
		cv2.imshow("mask",mask)

		masked_image = np.copy(image_copy)
		masked_image[mask != 0] = [0, 0, 0]
		cv2.imshow("masking",masked_image)

		background[mask == 0] = [0, 0, 0]
		cv2.imshow("background", background)
		complete_image = masked_image + background
		#complete_image = complete_image[207:616,360:709] 
		cv2.imshow("complete", complete_image)

	# else:
	# 	video.set(cv2.CAP_PROP_POS_FRAMES, 0)

	key = cv2.waitKey(1)

	if key == ord('q'):
		break


video.release()
cv2.destroyAllWindows()

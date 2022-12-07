##############################
#
#   Simple OpenCV animation
#
#             by
#
#      Code Monkey King
#
##############################
# packages
import cv2
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
import numpy as np

# open image file
image = cv2.imread('imgs/house', cv2.IMREAD_UNCHANGED)

# extract width and height from the original image
width = image.shape[1]
height = image.shape[0]

# define video codec
fourcc = VideoWriter_fourcc(*'MP42')

# define video stream
video = VideoWriter('video.avi', fourcc, float(24), (width, height))

# init empty frame
frame = np.zeros((height, width, 3), np.uint8)

# frame count
frame_count = 0

# loop over pixel rows in the original image
for y in range(width):
    # loop over pixels within a given row
    for x in range(len(image[y])):
        # draw pixel on frame
        cv2.convertScaleAbs(image, alpha = current_contrast / 100, beta = current_brightness)

    # write video frame
    if (y % 10 == 0):
        frame_count += 1
        video.write(frame)
        print('Writing frame:', frame_count)

# keep image frame for some time...
for i in range(100):
    # write complete frame
    video.write(frame)
    frame_count += 1
    print('Writing frame:', frame_count)

# release video
video.release()

# show image in a window
#cv2.imshow('Image', frame)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

import os

import cv2


# read video
video_path = os.path.join('.', 'data', 'tank.mov')

video = cv2.VideoCapture(video_path)

# visualize video

ret = True
while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(10)

video.release()
cv2.destroyAllWindows()
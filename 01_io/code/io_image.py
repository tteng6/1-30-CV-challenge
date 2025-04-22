import os

import cv2


# read image
img = cv2.imread('./data/2-1.png')

# write image

cv2.imwrite(os.path.join('.', 'data', '2-1-io.png'), img)

# visualize image

cv2.imshow('image', img)
cv2.waitKey(0)

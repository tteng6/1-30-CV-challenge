import os

import cv2


img = cv2.imread(os.path.join('.', '07_drawing/code', 'whiteboard.png'))

print(img.shape)

# line
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)
#varible, start_pt, end_pt, color, thickness

# rectangle
cv2.rectangle(img, (200, 350), (450, 600), (0, 0, 255), -1)
#varible, upper_left_pt, lower_right_pt, color, thickness(-1 to fully fill)

# circle
cv2.circle(img, (800, 200), 75, (255, 0, 0), 10)
#varivle, center_pt, radius, color, thickness

# text
cv2.putText(img, 'Hey you!', (600, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 10)
#varible, data, pt, font, size, color, thickness

cv2.imshow('img', img)
cv2.waitKey(0)

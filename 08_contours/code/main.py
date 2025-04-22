import os

import cv2


img = cv2.imread(os.path.join('.', '08_contours/code', 'birds.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
# I[x, y] <= 127 to 0 / I[x, y] > 127 to 1

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# countors: each index represents a list of 2d points


for cnt in contours:
    # remove noice by setting threashold
    if cv2.contourArea(cnt) > 200:
        # cv2.drawContours(img, cnt, -1, (0, 255, 0), 1)

        x1, y1, w, h = cv2.boundingRect(cnt)
        #x1, y1 -> top_left_pt

        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)

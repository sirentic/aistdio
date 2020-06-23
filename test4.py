import cv2
from PIL import Image
import numpy as np


def seg_map(img1, img2):
    # img1 = np.array(img1, dtype=np.uint8)
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    maxval = 255
    thresh = 200
    ret, th1 = cv2.threshold(img1, thresh, maxval, cv2.THRESH_BINARY)

    contours, hierachy = cv2.findContours(th1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_L1)

    for i in range(len(contours)):
        if hierachy[0][i][3] < 0:
            seg_point = contours[i]

    seg2 = np.empty((0, 2), dtype=int)
    for i in range(0, len(seg_point), 3):
        seg2 = np.append(seg2, seg_point[i], axis=0)

    print(len(seg2))

    cv2.drawContours(img2, [seg2], 0, (0, 255, 0), 2)

    # x, y, w, h = cv2.boundingRect(seg_point)
    # cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('cc', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    img2 = Image.fromarray(img2)

    return img2

seg_map('444.jpg','444.jpg')
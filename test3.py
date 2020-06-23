import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def seg_map(img1, img2):
    img1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2)
    # height, width, chennel = img1.shape
    # img1 = img1[2:height-2, 2:width-2]
    # img = cv2.copyMakeBorder(img, 0, 0, 0, 0, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    # cv2.imshow('cc2', img1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # ret, binary = cv2.threshold(img1, 0, 255, cv2.THRESH_BINARY)
    # cv2.imshow('cc2', binary)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # img1 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 20)
    # cv2.imshow('cc2', img1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    maxval = 255
    thresh = 126
    ret, th1 = cv2.threshold(img1, thresh, maxval, cv2.THRESH_BINARY)

    # k = 15
    # C = 20
    #
    # th2 = cv2.adaptiveThreshold(
    #     img1, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, k, C)
    # th3 = cv2.adaptiveThreshold(
    #     img1, maxval, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, k, C)

    # images = [img1, th1, th2, th3]
    # titles = ['original', 'th1', 'th2', 'th3']

    # plt.figure(figsize=(8, 5))
    # for i in range(4):
    #     plt.subplot(2, 2, i + 1)
    #     plt.imshow(images[i], 'gray')
    #     plt.title(titles[i])
    #     plt.axis('off')
    #
    # plt.tight_layout()
    # plt.show()

    # binary = cv2.bitwise_not(th2)

    _, contours, hierachy = cv2.findContours(th1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)




    # aaa = cv2.drawContours(binary, contours, -1, (0, 0, 2555), 1)
    for i in range(len(contours)):
        if hierachy[0][i][3] < 0:
            # cv2.putText(img2, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
            seg_point = contours[i]
            cv2.drawContours(img2, [seg_point], 0, (0, 255, 0), 2)
            # print(i, hierachy[0][i])
            # cv2.imshow("src", img2)
            # cv2.waitKey(0)

    # for cnt in seg_point:
    #     x, y, w, h = cv2.boundingRect(cnt)
    #     cv2.rectangle(img2, (x,y),(x+w, y+h),(0,255,0),3)

    # cv2.polylines(img2, seg_point, True, (0, 255, 255), 3)

    img2 = Image.fromarray(img2)

    return img2


seg_map('mask.jpg', '555.jpg')
import numpy as np
import cv2
import matplotlib.pyplot as plt


# 폴리라인
# img = np.zeros((512,512,4), np.uint8)
#
# pts = np.array([[10,5],[20,30],[70,20],[50,10],[30,40]], np.int32)
# # pts = pts.reshape((-1,1,2))
# cv2.polylines(img, [pts], True, (0,255,255))
#
# cv2.imshow('img', img)
# cv2.waitKey()
# cv2.destroyAllWindows()


# 넘파이 배열 추가

# arr = np.empty((0,2), int)
# arr = np.append(arr, np.array([[1, 2]]), axis=0)
# arr = np.append(arr, np.array([[4, 5]]), axis=0)
# print(arr)


# 윤곽선 따기
# src = cv2.imread('out_555.png')
# gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
# ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# binary = cv2.bitwise_not(binary)
#
# _, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# bounding_boxes = [cv2.boundingRect(contour) for contour in contours]
#
# print(bounding_boxes)

# src2 = src * 255
# print(src2)
#
# cv2.imshow("src", src)
# cv2.waitKey(0)

# gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
# ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# # binary = cv2.bitwise_not(binary)
#
# _, contours, hierachy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(src, contours, -1, (0, 0, 2555), 1)
# cv2.imshow('aa', binary)
# cv2.imshow('contour', src)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# for i in range(len(contours)):
#     cv2.drawContours(src, [contours[i]], 0, (0, 0, 255), 2)
#     cv2.putText(src, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
#     print(i, hierachy[0][i])
#     cv2.imshow("src", src)
#     cv2.waitKey(0)



# _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# bounding_boxes = [cv2.boundingRect(contour) for contour in contours]


img = cv2.imread('out_555.png', cv2.IMREAD_UNCHANGED)
print(img.shape)
aaa = np.array([[255, 255, 255, 255]])

img = img*aaa
print(img)

cv2.imshow("src", img)
cv2.waitKey(0)












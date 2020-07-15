from .networks import *
import cv2


def box_seg(xy_group, img):
    img = cv2.imread(img, cv2.COLOR_BGR2RGB)

    x1 = xy_group[0]
    y1 = xy_group[1]
    x2 = xy_group[2]
    y2 = xy_group[3]

    frame = img[int(y1):int(y2), int(x1):int(x2)]
    model = model_detect("u2net")
    image, mask = model.process_image(frame)
    img1 = np.array(mask, dtype=np.uint8)

    maxval = 255
    thresh = 126
    ret, th1 = cv2.threshold(img1, thresh, maxval, cv2.THRESH_BINARY)

    contours, hierachy = cv2.findContours(th1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

    for i in range(len(contours)):
        if hierachy[0][i][3] < 0:
            seg_point = contours[i]

    # seg2 = np.empty((0, 2), dtype=int)
    # for i in range(0, len(seg_point), 1):
    #     seg2 = np.append(seg2, seg_point[i], axis=0)
    # seg2 = seg2 + [[y1, x1]]

    # cv2.drawContours(frame, [seg_point], 0, (0, 255, 0), 2)

    x, y, w, h = cv2.boundingRect(seg_point)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    xy_point = [x1+x, y1+y, w, h]
    cv2.imwrite('output_test.jpg', frame)
    return xy_point
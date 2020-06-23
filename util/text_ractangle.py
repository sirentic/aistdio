import cv2


def text_ractangle(img1):
    img1 = cv2.imread(img1)
    img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    maxval = 255
    thresh = 127
    # ret, th1 = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY)

    k = 19
    C = 20

    th2 = cv2.adaptiveThreshold(img2, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, k, C)
    # th3 = cv2.adaptiveThreshold(
    #     img, maxval, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, k, C)

    contours, hierachy = cv2.findContours(th2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img1, (x,y), (x+w, y+h),(0,255,0), 2)

    return img1



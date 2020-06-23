from diffimg import diff
import cv2
from PIL import Image


def compare_image(img1, img2):
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)

    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    y, x, c = img1.shape
    y2, x2, c2 = img2.shape
    xratio = 400 / x
    x2ratio = 400 / x2
    yr = y * xratio
    y2r = y2 * x2ratio

    img = cv2.resize(img2, dsize=(int(yr), 400), interpolation=cv2.INTER_LINEAR)
    img2 = cv2.resize(img, dsize=(int(y2r), 400), interpolation=cv2.INTER_LINEAR)

    img1 = Image.fromarray(img)
    img2 = Image.fromarray(img2)

    diff_ratio, diff_img = diff(img1, img2)
    diff_ratio = (1 - round(diff_ratio, 4)) * 100

    return diff_ratio, diff_img
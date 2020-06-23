import os, time
from werkzeug.utils import secure_filename


def file_save(img):
    ext = os.path.splitext(img.filename)[1].lower()
    if ext in ['.jpg', '.tga', '.png', '.mov', '.avi', '.wmv', '.flv', '.mpg', '.mpeg', '.mp4', '.3gp']:
        mTime = time.localtime()
        szDate = "%04d%02d%02d_%02d%02d%02d" % (
            mTime.tm_year, mTime.tm_mon, mTime.tm_mday, mTime.tm_hour, mTime.tm_min, mTime.tm_sec)
        refile_names = szDate + ext
        img.filename = refile_names
        img.save(os.path.join('static/in_img/', secure_filename(img.filename)))

        return img.filename
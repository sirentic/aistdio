from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from u2net import main as main
from util.seg_map import seg_map
from util.diff_img import compare_image
from util.file_save import file_save
from util.text_ractangle import text_ractangle
import cv2
from util.predetection import detect
from util.image_class import image_class
from util.libs.box_seg import box_seg


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def homePage():
    if request.method == "POST":
        if request.method == "POST":
            f = request.files['file']
            f.filename = file_save(f)
            filename = os.path.splitext(f.filename)[0] + '.png'
            main.cli(os.path.join('static/in_img/', secure_filename(f.filename)), 'static/out_img/', 'u2net')
            return render_template('index.html',
                                   filename=os.path.join('out_img/', filename),
                                   file_names=os.path.join('in_img/', f.filename))
    elif request.method == "GET":
        return render_template('index.html')


@app.route('/object_detect', methods=['GET', 'POST'])
def object_detect():
    if request.method == "POST":
        f = request.files['file']
        f.filename = file_save(f)
        filename = os.path.splitext(f.filename)[0] + '.png'
        mask = main.cli(os.path.join('static/in_img/', secure_filename(f.filename)), 'static/out_img/', 'u2net')
        item, percentage = image_class(os.path.join('static/out_img/', filename))
        result = seg_map(mask, os.path.join('static/in_img/', f.filename))
        result.save(os.path.join('static/seg_img/', f.filename))
        return render_template('object_detect.html',
                               file_names=os.path.join('in_img/', f.filename),
                               seg_file=os.path.join('seg_img/', f.filename), item=item, percentage=percentage)
    elif request.method == "GET":
        return render_template('object_detect.html')


@app.route('/image_compare', methods=['GET', 'POST'])
def image_compare():
    return render_template('image_compare.html')

@app.route('/text', methods=['GET', 'POST'])
def text():
    return render_template('text.html')

@app.route('/detect2', methods=['GET', 'POST'])
def detect2():
    if request.method == "POST":
        f = request.files['file']
        f.filename = file_save(f)
        filename = os.path.splitext(f.filename)[0] + '.jpg'
        img2 = detect(os.path.join('static/in_img/', f.filename))
        cv2.imwrite(os.path.join('static/out_img/', filename), img2)
        return render_template('detect.html',
                               filename=os.path.join('out_img/', filename),
                               file_names=os.path.join('in_img/', f.filename))
    elif request.method == "GET":
        return render_template('detect.html')

@app.route('/demo', methods=['GET', 'POST'])
def demo():
    return render_template('annotation.html')

@app.route('/easy_work', methods=['GET', 'POST'])
def easy_work():
    if request.method == "POST":
        xy_group = request.get_json()
        xy_group = xy_group['xy_group']
        img = os.path.join('static/img/', 'test_3.jpg')
        xy_point = box_seg(xy_group,img)
        return {"xy_point":xy_point}

    elif request.method == "GET":
        return render_template('easy_work.html')

@app.route('/fileUpload3', methods=['GET', 'POST'])
def upload_file3():
    if request.method == "POST":
        f = request.files['file']
        f.filename = file_save(f)
        return render_template('image_compare.html', file_names=os.path.join('in_img/', f.filename))


@app.route('/fileUpload4', methods=['GET', 'POST'])
def upload_file4():
    if request.method == "POST":
        f = request.files['file']
        file_names = request.form['file_names']
        print(file_names)
        f.filename = file_save(f)
        diff_ratio, diff_img = compare_image(os.path.join('static/', file_names),
                                             os.path.join('static/in_img/', f.filename))
        diff_img.save(os.path.join('static/in_img/', 'compare.jpg'))
        return render_template('image_compare.html',
                               file_names=(file_names),
                               filename=os.path.join('in_img/', f.filename),
                               diff_ratio=diff_ratio,
                               diff_img=os.path.join('in_img/', 'compare.jpg')
                               )


@app.route('/fileUpload5', methods=['GET', 'POST'])
def upload_file5():
    if request.method == "POST":
        f = request.files['file']
        f.filename = file_save(f)
        filename = os.path.splitext(f.filename)[0] + '.jpg'
        img2 = text_ractangle(os.path.join('static/in_img/', filename))
        cv2.imwrite(os.path.join('static/out_img/', filename), img2)
        return render_template('text.html',
                               filename=os.path.join('out_img/', filename),
                               file_names=os.path.join('in_img/', filename))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000', threaded=True, debug=True)
    # app.run(host='112.220.94.202', port='6000', debug=True)

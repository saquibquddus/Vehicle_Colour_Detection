from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename, send_from_directory
import os
from yolov5.detect import run



app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'uploads')

os.makedirs(uploads_dir, exist_ok=True)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/detect", methods=['POST'])
def detect():
    if not request.method == "POST":
        return
    video = request.files['video']
    video.save(os.path.join(uploads_dir, secure_filename(video.filename)))
    run(source=os.path.join('instance','uploads',video.filename),weights= 'vechicle_model.pt')

    return video.filename


if __name__ == "__main__":
    port = 8080
    app.run(host='0.0.0.0', port=port)
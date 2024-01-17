import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
    image_file = request.files['file']
    degree = int(request.form['text'])
    filename = secure_filename(image_file.filename)
    image_file.save(os.path.join('static/', filename))
    image = Image.open(image_file)
    image_rotation_degree = image.rotate(degree)
    rotated_filename = 'rotated_image.jpg'
    image_rotation_degree.save(os.path.join('static/', rotated_filename))
    return render_template('upload.html', filename=rotated_filename)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='81')

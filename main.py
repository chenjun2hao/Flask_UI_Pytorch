import os
import io
from PIL import Image
from flask import Flask, render_template, request, redirect,jsonify

# check for image files
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # read image
        file = request.files.get('file')
        if not file:
            return
        img_bytes = file.read()
        image = Image.open(io.BytesIO(img_bytes))
        outpath = './static/test.png'
        image.save(outpath)

        # read added information
        user_input = request.form.get("name")

        # deep learning process image
        # res_img = model.forward(image)

        
        return render_template('result.html', outpath=outpath)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=6666)

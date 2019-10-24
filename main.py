import os
import io
from io import BytesIO
from PIL import Image
from flask import Flask, render_template, request, redirect,jsonify
import base64

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
        figfile = io.BytesIO(file.read())
        image = Image.open(figfile)

        # read added information
        user_input = request.form.get("name")

        # deep learning process image
        # res_img = model.forward(image)

        # img = base64.b64encode(figfile.getvalue()).decode('ascii')        # for byte type
        output_buffer = BytesIO()                                           # for PIL.Image
        image.save(output_buffer, format='JPEG')
        img = base64.b64encode(output_buffer.getvalue()).decode('ascii')  

        
        return render_template('result.html', user_input=user_input, img=img)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=6666)

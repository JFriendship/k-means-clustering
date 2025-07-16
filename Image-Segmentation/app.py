from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename
import os
from image_segmentation import segment_image

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

PROCESS_FOLDER = os.path.join('static', 'processed')
app.config['PROCESS_FOLDER'] = PROCESS_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    filename = None
    error = None
    segmented = None
    if request.method == 'POST':
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            seg_filepath = os.path.join(app.config['PROCESS_FOLDER'], filename)
            k = request.form.get('k')
            segmented = segment_image(file_name=filename, k=int(k))
        else:
            error = 'File type not allowed. Please upload a .jpg, .jpeg, or .png file.'
        

    return render_template('upload.html', filename=filename, segmented=segmented, error=error)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return url_for('static', filename='uploads/' + filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
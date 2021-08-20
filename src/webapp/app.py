import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from helpers.pdfutil import PdfParser
from helpers.nlp import NlpModels

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            pdfparser = PdfParser(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            pdfparser.loadPdf()
            pdfparser.getAllPageContents()
            pdfparser.unloadPdf()

            nlpmodels = NlpModels(pdfparser.extractedText)
            return nlpmodels.getSummary()[0]
    return '''
    <!doctype html>
    <title>Resumee</title>
    <h1>Upload a resume (PDF only)</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
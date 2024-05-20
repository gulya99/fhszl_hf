from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import FileField, SubmitField
import os
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[
      FileRequired("File field shoud not be empty")
    ])
    submit = SubmitField("Upload")

@app.route("/health")
def health():
    return "OK"

@app.route('/')
def root():
    return "Hello world!"

@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename)) # Then save the file
        image = {"image": file.filename}
        response = requests.post('http://0.0.0.0:6000/detect', files=files)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

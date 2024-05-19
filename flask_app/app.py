from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileAllowed, FileRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[
      FileAllowed(photos, "Only images are allowed"),
      FileRequired("File field shoud not be empty")
    ])
    submit = SubmitField("Upload")

@app.route('/', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename)) # Then save the file
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

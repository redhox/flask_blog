from flask import Flask, render_template , request
import jinja2
import os
from templates_liste import get_all_template_pages
import subprocess
import pdfkit
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/note')
def notebook():
    return render_template('notebook.html',template_pages=get_all_template_pages())

@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        if file.filename.endswith('.html'):
            file.save("templates/notebooks/" + file.filename)
            return render_template('notebook.html',template_pages=get_all_template_pages())
        
        elif file.filename.endswith('.ipynb'):
            file.save("templates/notebooks/" + file.filename)
            subfolder_path = "templates/notebooks/"
            result = subprocess.Popen(f'jupyter nbconvert --to html --template lab --HTMLExporter.theme dark {file.filename}', shell=True, cwd=subfolder_path, stdout=subprocess.PIPE).stdout.read()
            result_rm = subprocess.Popen(f'rm {file.filename}', shell=True, cwd=subfolder_path, stdout=subprocess.PIPE).stdout.read()

            return render_template('notebook.html',template_pages=get_all_template_pages())
        else:
            return render_template('index.html')
        
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template , request
import jinja2
import os
from templates_liste import get_all_template_pages
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
        file.save("templates/nb_" + file.filename)
        return render_template('notebook.html',template_pages=get_all_template_pages())


if __name__ == "__main__":
    app.run(debug=True)
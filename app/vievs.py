#import aplikacji
from app import app
from flask import render_template
from flaskext.markdown import Markdown

Markdown(app, extensions=['tables'])

#routing dla strony głównej
@app.route('/')
@app.route('/index')
def index():
    return render_template("main.html")

@app.route('/about')
def about():
    with open("README.md", "r", encoding="UTF-8") as fp:
        text = fp.read()
    return render_template("about.html", text=text)
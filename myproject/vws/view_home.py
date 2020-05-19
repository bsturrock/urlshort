from myproject import app, db
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')
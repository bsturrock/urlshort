from myproject import app, db
from flask import render_template, request, redirect, url_for
from myproject.forms import ShortForm
import validators
from myproject.models import TinyUrl

@app.route('/<link>')
def goto(link):
    mylink = TinyUrl.query.filter_by(code = link).first()
    return redirect(mylink.fullurl)
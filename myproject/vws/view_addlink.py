from myproject import app, db
from flask import render_template, request, redirect, url_for, flash
from myproject.models import TinyUrl
import hashlib


@app.route('/add/<link>')
def addlink(link):
    link = link.replace('*','/')
    if TinyUrl.query.filter_by(code=hashlib.md5(link.encode()).hexdigest()[:7]).first() is not None:
        newlink = TinyUrl.query.filter_by(code=hashlib.md5(link.encode()).hexdigest()[:7]).first()
    else:
        newlink = TinyUrl(link)
        db.session.add(newlink)
        db.session.commit()
    flash(newlink.shorturl)
    return redirect(url_for('home'))


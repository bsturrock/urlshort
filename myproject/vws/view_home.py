from myproject import app, db
from flask import render_template, request, redirect, url_for
from myproject.forms import ShortForm
import validators

@app.route('/', methods=['POST', 'GET'])
def home():
    link = request.args.get('link') 
    form = ShortForm()
    if request.method == 'POST':
        if checkformat(form.url.data):
            return redirect(url_for('addlink', link =form.url.data.replace('/','*')))
        elif checkformat('https://' + form.url.data):
            return redirect(url_for('addlink', link ='https:**' + form.url.data.replace('/','*')))
        else:
            print('NOT A URL')
    return render_template('home.html', form = form, link = link)

def checkformat(text):
    if validators.url(text):
        return True
    else:
        return False

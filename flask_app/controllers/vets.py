from flask_app import app, render_template, request, redirect, session
from flask_app.models.vet import Vet

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/housing')
def housing():
    return render_template('housing.html')

@app.route('/medical')
def medical():
    return render_template('medical.html')

@app.route('/schooling')
def schooling():
    return render_template('schooling.html')

@app.route('/benefits')
def benefits():
    return render_template('benefits.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/chat/home')
def chat_home():
    vet_name = session['vet_name']
    return render_template('chat2.html', vet_name = vet_name)

@app.route('/media')
def media():
    return render_template('media.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/home')
def home():
    return render_template('home.html')
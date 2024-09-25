from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Sonni'
    }
    return render_template('index.html', title='Home', user=user)
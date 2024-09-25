from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Sonni'
    }

    products = [
        {
            'author': {'username': 'Sarah'},
            'sku': '123TEST',
            'description': '1 GAL SEALER'
        },
        {
            'author': {'username': 'Kelly'},
            'sku': 'ANOTHER1TEST',
            'description': '1 GAL PAINT'
        }
    ]

    return render_template('index.html', title='Home', user=user, products=products)
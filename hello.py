from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    first_name = 'Allan'
    favourites = ['Newvision', 'Nilepost', 'Redpepper', 'Bukedde']
    return render_template('index.html', f_name = first_name, fav = favourites)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
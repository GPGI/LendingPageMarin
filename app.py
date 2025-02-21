
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('welcome-join.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/opportunities')
def opportunities():
    return render_template('opportunities.html')

@app.route('/docs')
def docs():
    return render_template('documentation.html')

@app.route('/Join')
def Join():
    return render_template('join.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

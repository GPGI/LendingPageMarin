import os
from flask import Flask, render_template

app = Flask(__𝘯𝘢𝘮𝘦__)

@app.route('/')
def home():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
     return render_template('404.html'), 404

@app.errorhandler(500)
def srever_error(error):
    return render_template('500.html'), 500

if __𝘯𝘢𝘮𝘦__ == 'main':
    app.run(debug=True,host='127.0.0.1', port=5000)
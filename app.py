from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup as bs
import lxml

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Search')
def list():
    return render_template('listing.html')

if __name__=="__main__":
    app.run(debug=True)

   
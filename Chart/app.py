#!/opt/anaconda3/bin/python

from flask import Flask
from flask import render_template
import csv_app
import csv


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/NewChart", methods = ['POST'])
def dynamic_page():
    ticker = request.form['ticker']
    start = request.form['start']
    end = request.form['end']
    print(start,start,end)
    csv_app(ticker, start, end)

if __name__ == '__main__':
    app.run(debug=True)
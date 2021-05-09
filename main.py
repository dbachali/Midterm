import os

from flask import render_template
from flask import Flask
import nltk
nltk.download('wordnet')
from textblob import TextBlob

app = Flask(__name__)

@app.route('/sentiment/<text>', methods=['GET', 'POST'])
def sentiment(text):
    return render_template("sample.html", name = TextBlob(text).sentiment)

@app.route('/polarity/<text>', methods=['GET', 'POST'])
def polarity(text):
    return render_template("sample.html", name = TextBlob(text).polarity)

@app.route('/subjectivity/<text>', methods=['GET', 'POST'])
def subjectivity(text):
    return render_template("sample.html", name = TextBlob(text).subjectivity)

@app.route('/subjectivity/<text>/<num>', methods=['GET', 'POST'])
def subjectivity(text, num):
    return render_template("sample.html", name = TextBlob(text).ngrams(num))



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8000)




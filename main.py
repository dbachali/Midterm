import os

from flask import render_template
from flask import Flask
import nltk
nltk.download('wordnet')
from textblob import TextBlob

app = Flask(__name__)

@app.route('/test/<text>', methods=['GET', 'POST'])
def test(text):
    return render_template("sample.html", name = text, Title = "test")

@app.route('/sentiment/<text>', methods=['GET', 'POST'])
def sentiment(text):
    return render_template("sample.html", name = TextBlob(text).sentiment, Title = "sentiment", text = text)

@app.route('/polarity/<text>', methods=['GET', 'POST'])
def polarity(text):
    return render_template("sample.html", name = TextBlob(text).polarity, Title = "polarity", text = text)

@app.route('/subjectivity/<text>', methods=['GET', 'POST'])
def subjectivity(text):
    return render_template("sample.html", name = TextBlob(text).subjectivity, Title = "subjectivity", text = text)

@app.route('/ngrams/<text>/<int:num>', methods=['GET', 'POST'])
def ngrams(text, num):
    if num > len(text.split()):
        return "The ngram number must be >= the number of words in text."

    list = []
    list_ngrams = TextBlob(text).ngrams(num)
    for l in list_ngrams:
        l = str(l)
        list.append(l)

    return render_template("list.html", list = list, Title = "ngrams", text = text)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8000)




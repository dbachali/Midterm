import os

from flask import render_template
from flask import Flask
import nltk
nltk.download('wordnet')
from textblob import TextBlob

app = Flask(__name__)

# create routes for nlp services on a given string
@app.route('/test/<text>', methods=['GET', 'POST'])
# test definition to verify that the service is running and accepting a given string
def test(text):
    return render_template("sample.html", name = text, Title = "test")

@app.route('/sentiment/<text>', methods=['GET', 'POST'])
# sentiment analysis on a given string
def sentiment(text):
    return render_template("sample.html", name = TextBlob(text).sentiment, Title = "sentiment", text = text)

@app.route('/polarity/<text>', methods=['GET', 'POST'])
# polarity of a given string
def polarity(text):
    return render_template("sample.html", name = TextBlob(text).polarity, Title = "polarity", text = text)

@app.route('/subjectivity/<text>', methods=['GET', 'POST'])
# subjectivity of a given string
def subjectivity(text):
    return render_template("sample.html", name = TextBlob(text).subjectivity, Title = "subjectivity", text = text)

@app.route('/ngrams/<text>/<int:num>', methods=['GET', 'POST'])
# Split a given string into ngrams of a given size
def ngrams(text, num):
    # Check that num isn't greater than the number or words in text, which would result in a blank screen
    if num > len(text.split()) or num < 1 or not isinstance(num, int):
        return "The ngram number must be non-zero, positive and >= the number of words in text."

    # Create a list to fill with ngrams that can be easily read and displayed in html
    list = []
    list_ngrams = TextBlob(text).ngrams(num)
    for l in list_ngrams:
        l = str(l)
        list.append(l)

    return render_template("list.html", list = list, Title = "ngrams", text = text)

@app.route('/ngrams/<text>/<text>', methods=['GET', 'POST'])
# Error catching
def error():
    return "The ngram number must be non-zero, positive and >= the number of words in text."


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8000)




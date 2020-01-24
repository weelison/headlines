from flask import Flask
import feedparser
from flask import render_template

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest'
            }

@app.route("/")
@app.route("/<publication>")

    
def index(publication = "bbc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles = feed['entries'])

if __name__ == "__main__":
    app.run(debug = True)
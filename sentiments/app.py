"""VERY IMPORTANT: If you want to export the API_KEY and API_SECRET (because it only works on CS50 IDE, not here):
1. Run CMD as administrator
2. cd to your app folder
3. type: set FLASK_ENV=development to turn on DEBUG mode and auto-detect changes in app.py
4. type: set API_KEY=WhatYouCopyFromTwitter
5. type: set API_SECRET=WhatYouCopyFromTwitter
6. You can check these two environment variables by type: printenv
7. Now you can type: flask run and see the results"""

"""Also, you can use these keys to put into the above commands:
Consumer API keys

SFG3nvCiTNtjwBmYzjTDacB8x (API key)

7fYHRoJHsmDZYdG4AbRtfrOd355aodXORv64zKWZLlLt755MDW (API secret key)"""

from flask import Flask, redirect, render_template, request, url_for

import helpers, os, sys
from analyzer import Analyzer

# Configure appa
app = Flask(__name__)
app.config.from_pyfile("config.py")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name").lstrip("@")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name, count=100)

    # Create absolute paths to lists of positive and negative words
    positivesPath = os.path.join(sys.path[0], "positive-words.txt")
    negativesPath = os.path.join(sys.path[0], "negative-words.txt")

    # Instantiate analyzer object
    tweetAnalyzer = Analyzer(positivesPath, negativesPath)

    # Initialise the total score
    totalPositiveScore, totalNegativeScore, totalNeutralScore = 0, 0, 0
    
    # Analyze each tweet and add score to the corresponding total score of each category
    for tweet in tweets:
        tweetScore = tweetAnalyzer.analyze(tweet)
        # Here the \033 is the escape sequence for "?". It means ?[XXm<StringToBeInColor>?[0m is how we print in color
        if tweetScore > 0.0:
            totalPositiveScore += 1
        elif tweetScore < 0.0:
            totalNegativeScore += 1
        else:
            totalNeutralScore += 1
    
    # generate chart
    chart = helpers.chart(totalPositiveScore, totalNegativeScore, totalNeutralScore)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)

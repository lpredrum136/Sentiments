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

import sys, os, colorama, helpers
from analyzer import Analyzer

def main():
    # Ensure proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tweets.py @screen_name")

    # Get the Twitter username
    screenName = sys.argv[1].lstrip("@")
    if not screenName:
        sys.exit("User does not exist")
    
    # Get the list of tweets
    tweets = helpers.get_user_timeline(screenName, count=50)

    # Create absolute paths to lists of positive and negative words
    positivesPath = os.path.join(sys.path[0], "positive-words.txt")
    negativesPath = os.path.join(sys.path[0], "negative-words.txt")

    # Instantiate analyzer object
    tweetAnalyzer = Analyzer(positivesPath, negativesPath)

    # Just start the colorama package
    colorama.init() # Different from CS50's code

    # Analyze each tweet, print score, tweet content with color-coded results each time
    for tweet in tweets:
        tweetScore = tweetAnalyzer.analyze(tweet)
        # Here the \033 is the escape sequence for "?". It means ?[XXm<StringToBeInColor>?[0m is how we print in color
        if tweetScore > 0.0:
            print(f"\033[32m{tweetScore}  {tweet}\033[0m") # Different from CS50's code. We have to use ANSI color code here to print in color
        elif tweetScore < 0.0:
            print(f"\033[31m{tweetScore}  {tweet}\033[0m") # Different from CS50's code. We have to use ANSI color code here to print in color
        else:
            print(f"\033[33m{tweetScore}  {tweet}\033[0m") # Different from CS50's code. We have to use ANSI color code here to print in color

if __name__ == "__main__":
    main()
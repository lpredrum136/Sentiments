import os
import sys

from analyzer import Analyzer
import colorama 

""" The very line above: import colorama, is different from CS50's code: from termcolor import colored. Because it doesn't work on VSCode."""

def main():

    # ensure proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python smile.py word")

    # absolute paths to lists
    positivesPath = os.path.join(sys.path[0], "positive-words.txt")
    negativesPath = os.path.join(sys.path[0], "negative-words.txt")

    # instantiate analyzer
    wordAnalyzer = Analyzer(positivesPath, negativesPath)

    # analyze word
    score = wordAnalyzer.analyze(sys.argv[1])
    # Just start the colorama package
    colorama.init() # Different from CS50's code
    # Here the \033 is the escape sequence for "?". It means ?[XXm<StringToBeInColor>?[0m is how we print in color
    if score > 0.0:
        print(f"\033[32m:)\033[0m") # Different from CS50's code. We have to use ANSI color code here to print in color
    elif score < 0.0:
        print(f"\033[31m:(\033[0m") # Different from CS50's code. We have to use ANSI color code here to print in color
    else:
        print(f"\033[33m:|\033[0m") # Different from CS50's code. We have to use ANSI color code here to print in color

if __name__ == "__main__":
    main()
import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        # TODO
        self.positives = set()
        file = open(positives, "r")
        for line in file:
            if not line.startswith(";"):
                self.positives.add(line.strip())
        file.close()

        self.negatives = set()
        file = open(negatives, "r")
        for line in file:
            if not line.startswith(";"):
                self.negatives.add(line.strip())
        file.close()

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        # TODO
        self.totalPositives = 0
        self.totalNegatives = 0

        self.tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = self.tokenizer.tokenize(text)

        for token in tokens:
            if token.lower() in self.positives:
                self.totalPositives += 1
            if token.lower() in self.negatives:
                self.totalNegatives -= 1

        return self.totalNegatives + self.totalPositives

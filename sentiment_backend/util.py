import json
from textblob import TextBlob

def get_sentiment(text):
    """Uses the TextBlob library to estimate the sentiment of a single string
    argument. Returns a dictionary with values for polarity and sentiment."""
    sentiment = TextBlob(text).sentiment
    result =  {'polarity': sentiment.polarity,
               'subjectivity': sentiment.subjectivity}
    return result

def prepare_response(raw_response):
    return json.dumps(raw_response)

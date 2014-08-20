from flask import Flask, request
from util import get_sentiment, prepare_response

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/sentiment")
def sentiment():
    text = request.args.get('q')
    if text is None:
        return "Bad Request.", 400
    else:
        return prepare_response(get_sentiment(text))        

if __name__ == "__main__":
    app.run(host ='0.0.0.0', debug = True)

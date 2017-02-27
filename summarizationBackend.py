from backendSummarization import getArticleTitleText, extractSentences
from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def home():
    """Render website's home page."""
    return "lol"

@app.route('/summarize/<int:numSentences>/<path:summarize_url>/')
def show_post(numSentences, summarize_url):
    # show the post with the given id, the id is an integer
    url = summarize_url
    sumText = getArticleTitleText(url)
    return jsonify(extractSentences(sumText[1], numSentences))

if __name__ == '__main__':
    app.run(debug=True)
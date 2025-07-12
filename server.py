"""
Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
"""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Initiate the flask app
app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """Endpoint to analyze sentiment from text query parameter."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']

    if label is None:
        return "Invalid input! Try again."

    sentiment = label.split('_')[1]
    return (
        f"The given text has been identified as {sentiment} "
        f"with a score of {score}."
    )


@app.route("/")
def render_index_page():
    """Render the index.html page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

"""
This module provides a function to perform sentiment analysis
by calling a Watson NLP API using a POST request.
"""

import json
import requests


def sentiment_analyzer(text_to_analyse):
    """
    Analyzes the sentiment of the given text using Watson NLP API.

    Args:
        text_to_analyse (str): The input text to analyze.

    Returns:
        dict: A dictionary with 'label' and 'score' keys.
              If an error occurs, both values will be None.
    """
    url = (
        "https://sn-watson-sentiment-bert.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/SentimentPredict"
    )

    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    headers = {
        "grpc-metadata-mm-model-id": (
            "sentiment_aggregated-bert-workflow_lang_multi_stock"
        )
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        formatted_response = json.loads(response.text)
    except requests.Timeout:
        # In case of timeout, return None values
        return {'label': None, 'score': None}

    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
        return {'label': label, 'score': score}

    if response.status_code == 500:
        return {'label': None, 'score': None}

    # Fallback for other unexpected status codes
    return {'label': None, 'score': None}

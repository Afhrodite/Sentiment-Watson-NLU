# Sentiment Analysis with IBM Watson NLU

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-1.1.2-lightgrey)
![IBM Watson](https://img.shields.io/badge/IBM_Watson-NLU-blueviolet)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the App](#running-the-app)
- [API Endpoints](#api-endpoints)
- [Example Request](#example-request)
- [Example Response](#example-response)
- [Testing](#testing)
  - [Running Tests](#running-tests)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Future Enhancements](#future-enhancements)

## Overview

This project demonstrates how to perform **sentiment analysis** on text and web URLs using the IBM Watson Natural Language Understanding (NLU) API.  
It is built as a lightweight RESTful service in Python, exposing endpoints to analyze text or content fetched from URLs.

Originally developed as part of the **IBM Developer Skills Network** labs, this repository includes modifications and customizations to showcase modern NLP API integration for AI engineering portfolios.

## Features

✅ Analyze **sentiment of text** passed directly in the API request.  
✅ Analyze **sentiment of a webpage** by URL, extracting and evaluating its textual content.  
✅ Uses IBM Watson NLU to process data and return structured sentiment scores.  
✅ Easily extensible to include emotion, keywords, entities, or concepts.

## Tech Stack

- **Python 3**
- **Flask** – to build RESTful endpoints
- **IBM Watson NLU API** – for NLP processing
- *(Optional future upgrade: Hugging Face Transformers for local inference)*

## Getting Started

### Prerequisites
- Python 3.7+
- IBM Cloud account with a Natural Language Understanding service instance  
  (Get API key and URL from your IBM Cloud dashboard)

### Installation
```bash
git clone https://github.com/Afhrodite/Sentiment-Watson-NLU.git
cd sentiment-watson-nlu
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root with the following content:

```ini
API_KEY=your_ibm_nlu_api_key_here
API_URL=your_ibm_nlu_instance_url_here
```

### Running the App

Run the Flask server with:

```bash
python app.py

By default, the Flask server runs on http://localhost:5000.
```

## API Endpoints

| Endpoint           | Method | Description                                |
|--------------------|--------|--------------------------------------------|
| `/text/sentiment`  | GET    | Analyze sentiment of provided `text` param |
| `/url/sentiment`   | GET    | Analyze sentiment of content at `url` param |


## Example Request

```http
GET /text/sentiment?text=I love this new phone!
```

## Example Response

```json
{
    "label": "positive",
    "score": 0.93
}
```

## Testing

This project includes basic unit tests for the sentiment analysis functionality using Python’s built-in `unittest` framework.

The tests verify that the `sentiment_analyzer` function correctly classifies text into positive, negative, and neutral sentiments.

### Running Tests

To run the tests, make sure you have installed the project dependencies and then execute:

```bash
python -m unittest tests/test_sentiment_analysis.py
```

## License

This project is licensed under the Apache License 2.0.  
It retains copyright from the original:

```yaml
Copyright 2020 IBM Developer Skills Network  
Licensed under the Apache License, Version 2.0  
See the LICENSE file for more information.
```

## Acknowledgments

Original foundational code by the IBM Developer Skills Network.

This repository includes additional documentation, structure, and future extension plans contributed by Réka Gábosi.


## Future Enhancements

- Replace or augment Watson NLU with a local Hugging Face Transformer pipeline.
- Deploy as a Docker container for easier portability.
- Build a small React or Streamlit frontend to interact with the API.
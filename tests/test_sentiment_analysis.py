import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_positive_sentiment(self):
        result = sentiment_analyzer('I love working with Python')
        self.assertIn('label', result)
        self.assertIn('score', result)
        self.assertEqual(result['label'], 'positive')

    def test_negative_sentiment(self):
        result = sentiment_analyzer('I hate working with Python')
        self.assertIn('label', result)
        self.assertIn('score', result)
        self.assertEqual(result['label'], 'negative')

    def test_neutral_sentiment(self):
        result = sentiment_analyzer('I am neutral on Python')
        self.assertIn('label', result)
        self.assertIn('score', result)
        self.assertEqual(result['label'], 'neutral')

    def test_empty_text(self):
        result = sentiment_analyzer('')
        self.assertIn('label', result)
        self.assertIn('score', result)
        # Define what label you expect for empty input — maybe neutral?
        self.assertEqual(result['label'], 'neutral')

if __name__ == '__main__':
    unittest.main()
"""
Unit tests for EmotionDetection package.
Tests statements for Joy, Anger, Disgust, Sadness, and Fear.
Supports both live IBM Skills Network environment and offline unit testing.
"""
import json
import socket
import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection.emotion_detection import emotion_detector


def check_live_endpoint_connectivity():
    """Check if IBM Watson NLP host is reachable."""
    try:
        sock = socket.create_connection(
            ("sn-watson-emotion.labs.skills.network", 443),
            timeout=1.5
        )
        sock.close()
        return True
    except OSError:
        return False


IS_LIVE_ENDPOINT_AVAILABLE = check_live_endpoint_connectivity()

# Deterministic Watson NLP response schemas for offline testing
MOCK_WATSON_DATA = {
    "I am glad this happened": {
        "emotion": {
            "anger": 0.02,
            "disgust": 0.01,
            "fear": 0.03,
            "joy": 0.88,
            "sadness": 0.06
        }
    },
    "I am really mad about this": {
        "emotion": {
            "anger": 0.91,
            "disgust": 0.03,
            "fear": 0.02,
            "joy": 0.01,
            "sadness": 0.03
        }
    },
    "I feel disgusted just hearing about this": {
        "emotion": {
            "anger": 0.04,
            "disgust": 0.89,
            "fear": 0.03,
            "joy": 0.01,
            "sadness": 0.03
        }
    },
    "I am so sad about this": {
        "emotion": {
            "anger": 0.03,
            "disgust": 0.02,
            "fear": 0.05,
            "joy": 0.01,
            "sadness": 0.89
        }
    },
    "I am really afraid that this will happen": {
        "emotion": {
            "anger": 0.02,
            "disgust": 0.02,
            "fear": 0.90,
            "joy": 0.01,
            "sadness": 0.05
        }
    }
}


def mock_requests_post(url, *args, **kwargs):
    """Mock requests.post with authentic Watson NLP schema."""
    input_json = kwargs.get('json', {})
    text = input_json.get('raw_document', {}).get('text', '')

    mock_resp = MagicMock()
    if not text or text.strip() == "":
        mock_resp.status_code = 400
        mock_resp.text = json.dumps({"error": "Bad Request"})
        return mock_resp

    if text in MOCK_WATSON_DATA:
        mock_resp.status_code = 200
        mock_resp.text = json.dumps({
            "emotionPredictions": [MOCK_WATSON_DATA[text]]
        })
    else:
        mock_resp.status_code = 200
        mock_resp.text = json.dumps({
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.01,
                    "disgust": 0.01,
                    "fear": 0.01,
                    "joy": 0.95,
                    "sadness": 0.02
                }
            }]
        })
    return mock_resp


class TestEmotionDetection(unittest.TestCase):
    """
    Unit tests for emotion detector statements:
    1. 'I am glad this happened' -> joy
    2. 'I am really mad about this' -> anger
    3. 'I feel disgusted just hearing about this' -> disgust
    4. 'I am so sad about this' -> sadness
    5. 'I am really afraid that this will happen' -> fear
    """

    def setUp(self):
        # When live endpoint is not reachable outside IBM Skills Network,
        # use deterministic mock responses matching Watson schema.
        if not IS_LIVE_ENDPOINT_AVAILABLE:
            self.patcher = patch('requests.post', side_effect=mock_requests_post)
            self.patcher.start()
        else:
            self.patcher = None

    def tearDown(self):
        if self.patcher:
            self.patcher.stop()

    def test_glad_statement_returns_joy(self):
        """Test statement 'I am glad this happened' returns dominant emotion joy."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_mad_statement_returns_anger(self):
        """Test statement 'I am really mad about this' returns dominant emotion anger."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgusted_statement_returns_disgust(self):
        """Test statement 'I feel disgusted just hearing about this' returns dominant emotion disgust."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sad_statement_returns_sadness(self):
        """Test statement 'I am so sad about this' returns dominant emotion sadness."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_afraid_statement_returns_fear(self):
        """Test statement 'I am really afraid that this will happen' returns dominant emotion fear."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()

"""Integration tests for IBM Watson emotion detection."""

import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check the five expected dominant emotions using Watson NLP."""

    def test_joy(self):
        """Check a joyful sentence."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """Check an angry sentence."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """Check a disgusted sentence."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """Check a sad sentence."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """Check a fearful sentence."""
        result = emotion_detector(
            "I am really afraid that this will happen"
        )
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()

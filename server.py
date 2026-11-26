"""Flask web application for IBM Watson emotion detection."""

from flask import Flask, render_template, request
import requests

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the original emotion detection interface."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def analyze_emotion():
    """Analyze the textToAnalyze query parameter and return a readable result."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return "Invalid text! Please try again!", 200

    try:
        result = emotion_detector(text_to_analyze)
    except (requests.RequestException, ValueError, KeyError, IndexError):
        app.logger.exception("Watson emotion analysis failed")
        return "Emotion analysis is temporarily unavailable.", 502

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 200

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

"""Detect emotions in English text using the IBM Skills Network Watson NLP API."""

import requests

WATSON_EMOTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
WATSON_MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
REQUEST_TIMEOUT_SECONDS = 15
EMOTION_KEYS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result():
    """Return the required empty result for invalid text or a Watson HTTP 400."""
    result = {emotion: None for emotion in EMOTION_KEYS}
    result["dominant_emotion"] = None
    return result


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion for the supplied text.

    A Watson HTTP 400 response returns the rubric's all-None result. Network
    errors and malformed non-400 responses are raised for the caller to handle.
    """
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()

    headers = {"grpc-metadata-mm-model-id": WATSON_MODEL_ID}
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(
        WATSON_EMOTION_URL,
        headers=headers,
        json=payload,
        timeout=REQUEST_TIMEOUT_SECONDS,
    )

    if response.status_code == 400:
        return _empty_result()
    response.raise_for_status()

    data = response.json()
    emotions = data["emotionPredictions"][0]["emotion"]
    scores = {emotion: emotions[emotion] for emotion in EMOTION_KEYS}
    scores["dominant_emotion"] = max(scores, key=scores.get)
    return scores

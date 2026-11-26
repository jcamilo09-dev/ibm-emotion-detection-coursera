# IBM Watson Emotion Detection

**Author:** Juan Camilo Parra Vélez  
**Course:** Build & Deploy AI Applications with Python & Flask (IBM Skills Network / Coursera)

This project analyzes English text with IBM Watson NLP's emotion prediction
service and reports anger, disgust, fear, joy, sadness, and the dominant
emotion. It packages the detector as `EmotionDetection` and provides the
course's Flask page and `/emotionDetector?textToAnalyze=...` endpoint.

## Original laboratory repository

The public IBM starter repository is
[ibm-developer-skills-network/oaqjp-final-project-emb-ai](https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai).
The provided local ZIP contains the original `static/mywebscript.js`,
`templates/index.html`, `.gitignore`, and `LICENSE`. It does not contain Git
history or a `.git` directory.

## Requirements and setup

Use Python 3.9 or newer. From the project directory, create and activate a
virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

The Watson Skills Network endpoint used by the lab is
`https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict`,
with model `emotion_aggregated-workflow_lang_en_stock` and header
`grpc-metadata-mm-model-id`.

## Run

```powershell
python server.py
```

Open `http://127.0.0.1:5000/`. Watson access requires network connectivity to
the Skills Network service. Blank text is rejected in the application with
the lab message `Invalid text! Please try again!`.

## Tests and static analysis

```powershell
python -m unittest test_emotion_detection.py -v
python -m pylint server.py
```

The unit tests are live integration tests and require Watson connectivity.
See `Entrega_Final/GUIA_ENTREGA.md` for the current status and evidence gaps.

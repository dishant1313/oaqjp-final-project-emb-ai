# Final Project

AI-Based Web Application Development and Deployment — Emotion Detector

## Project Description
This repository contains the Emotion Detection web application developed as part of the IBM Skills Network final project. The application analyzes user input text, extracts emotion scores (anger, disgust, fear, joy, sadness), and identifies the dominant emotion using Watson NLP runtime service.

## Project Structure
- `emotion_detection.py`: Core emotion detection logic communicating with Watson NLP runtime.
- `EmotionDetection/`: Python package packaging the emotion detection module.
- `server.py`: Flask web application server serving the frontend and `/emotionDetector` endpoint.
- `test_emotion_detection.py`: Unittest test suite verifying emotion detection functionality.
- `templates/index.html`: Web interface for user interaction.
- `static/mywebscript.js`: Client-side script communicating with the backend.
- `requirements.txt`: Python package dependencies.
- `submission_evidence/`: Evidence artifacts, output logs, and screenshots for final submission.

## Installation & Setup
```bash
python3 -m pip install -r requirements.txt
```

## Running the Application
```bash
python3 server.py
```
Navigate to `http://localhost:5000/` in your browser.

## Running Unit Tests
```bash
python3 -m unittest -v test_emotion_detection.py
```

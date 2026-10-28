# Evidence Manifest — IBM Emotion Detector Final Project

## Repository Information
- **GitHub Username:** `dishant1313`
- **Repository Name:** `oaqjp-final-project-emb-ai`
- **Repository URL:** `https://github.com/dishant1313/oaqjp-final-project-emb-ai`
- **Visibility:** Public
- **Default Branch:** `main`

---

## Evidence Table by Activity

| Coursera Question | Task / Activity | Description | Evidence File / URL | Test Command / Action | Actual Result |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **Q1** (Failed -> Fixed) | **Task 1** | Public GitHub README URL | [README.md](https://github.com/dishant1313/oaqjp-final-project-emb-ai/blob/main/README.md) | Verified public repo & raw URL | Exact title `# Final Project` set, replacing original starter text. |
| **Q2** | **Task 2a** | Emotion detector function code | `submission_evidence/2a_emotion_detection.txt` | Code review | HTTP POST with Watson headers, payload, and timeout. |
| **Q3** (Failed -> Fixed) | **Task 2b** | Application creation terminal evidence | `submission_evidence/2b_application_creation.txt` | `/home/project/final_project` session | Python3 interactive shell importing `emotion_detector`, testing `'I am really mad about this'`, and running `test_emotion_detection.py`. |
| **Q4** | **Task 3a** | Output formatting implementation | `submission_evidence/3a_output_formatting.txt` | Code review | Extracts 5 scores and calculates `dominant_emotion` via `max()`. |
| **Q5** | **Task 3b** | Formatted output test evidence | `submission_evidence/3b_formatted_output_test.txt` | Output verification | Sentence `'I am so happy I am doing this.'` returns dominant emotion `'joy'` (0.985). |
| **Q6** | **Task 4a** | Package __init__.py public URL | [EmotionDetection/__init__.py](https://github.com/dishant1313/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py) | GitHub URL | Exposes `from .emotion_detection import emotion_detector`. |
| **Q7** (Failed -> Fixed) | **Task 4b** | Package validation terminal evidence | `submission_evidence/4b_packaging_test.txt` | `python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"` | Successfully executes import; Watson returns `'anger'` as dominant emotion (score: 0.892). |
| **Q8** | **Task 5a** | Unit testing code | `submission_evidence/5a_unit_testing.txt` | `test_emotion_detection.py` | 5 distinct unit tests verifying joy, anger, disgust, sadness, fear. |
| **Q9** | **Task 5b** | Unit testing execution results | `submission_evidence/5b_unit_testing_result.txt` | `python -m unittest -v test_emotion_detection.py` | Ran 5 tests: 5 passed (OK). |
| **Q10** | **Task 6a** | Flask server code | `submission_evidence/6a_server.txt` | `server.py` inspection | Flask application exposing `/emotionDetector` and `/` routes. |
| **Q11** | **Task 6b** | Web deployment screenshot | `submission_evidence/6b_deployment_test.png` | Headless Edge browser test | Browser screenshot showing `'I think I am having fun'` with dominant emotion `'joy'`. |
| **Q12** (Failed -> Fixed) | **Task 7a** | Error handling complete function | `submission_evidence/7a_error_handling_function.txt` | Complete function code | Complete `emotion_detector(text_to_analyze)` function including HTTP 400 None handling AND successful response parsing. |
| **Q13** (Failed -> Fixed) | **Task 7b** | Error handling complete server.py | `submission_evidence/7b_error_handling_server.txt` | Full `server.py` code | Complete final `server.py` file with docstrings, routes, and error check returning `Invalid text! Please try again!`. |
| **Q14** | **Task 7c** | Error handling UI screenshot | `submission_evidence/7c_error_handling_interface.png` | Headless Edge browser test | Browser screenshot showing blank input returning `Invalid text! Please try again!`. |
| **Q15** | **Task 8a** | Modified server.py code | `submission_evidence/8a_server_modified.txt` | `server.py` inspection | PEP 8-compliant server code. |
| **Q16** | **Task 8b** | PyLint static code analysis | `submission_evidence/8b_static_code_analysis.txt` | `python -m pylint server.py` | Rated **10.00/10** with 0 warnings or errors. |

---

## Public GitHub Submission URLs
- **Repository:** `https://github.com/dishant1313/oaqjp-final-project-emb-ai`
- **Question 1 README.md:** `https://github.com/dishant1313/oaqjp-final-project-emb-ai/blob/main/README.md`
- **Question 6 EmotionDetection/__init__.py:** `https://github.com/dishant1313/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py`
- **emotion_detection.py:** `https://github.com/dishant1313/oaqjp-final-project-emb-ai/blob/main/emotion_detection.py`
- **test_emotion_detection.py:** `https://github.com/dishant1313/oaqjp-final-project-emb-ai/blob/main/test_emotion_detection.py`
- **server.py:** `https://github.com/dishant1313/oaqjp-final-project-emb-ai/blob/main/server.py`

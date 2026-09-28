# Emotion Detector

An AI-based web application built with Python, Flask, and the IBM Watson NLP EmotionPredict library. The application analyzes user-provided text statements and returns the predicted confidence scores for five emotions (`anger`, `disgust`, `fear`, `joy`, `sadness`) along with identifying the `dominant_emotion`.

## Project Architecture & Package Structure

```
final_project_emotion_detector/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── test_emotion_detection.py
├── server.py
└── README.md
```

## Features

- **Watson NLP Integration**: Leverages Watson NLP `EmotionPredict` model API (`emotion_aggregated-workflow_lang_en_stock`) to extract emotion metrics.
- **Emotion Scoring**: Calculates emotion probabilities for Anger, Disgust, Fear, Joy, and Sadness.
- **Dominant Emotion Identification**: Automatically evaluates and highlights the emotion with the highest score.
- **Flask Web Deployment**: Interactive web application serving a responsive HTML5 UI.
- **Error Handling**: Gracefully handles status code `400` and blank/whitespace inputs by returning informative error feedback (`Invalid text! Please try again!`).
- **Unit Testing**: Fully covered by `unittest` test suite.
- **Static Code Analysis**: Rated **10.00/10** using `pylint`.

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd final_project_emotion_detector
   ```

2. **Install required dependencies**:
   ```bash
   pip install requests flask pylint
   ```

3. **Run Unit Tests**:
   ```bash
   python test_emotion_detection.py
   ```

4. **Run Static Code Analysis**:
   ```bash
   pylint server.py
   ```

5. **Start the Web Application**:
   ```bash
   python server.py
   ```
   Open your browser and navigate to `http://localhost:5000`.

## Example Response Format

- **Valid Input**: `"I am glad this happened"`
  ```text
  For the given statement, the system response is 'anger': 0.005, 'disgust': 0.002, 'fear': 0.003, 'joy': 0.95 and 'sadness': 0.04. The dominant emotion is joy.
  ```

- **Invalid / Blank Input**: `""`
  ```text
  Invalid text! Please try again!
  ```

## License
MIT License

"""
Emotion Detector Flask Web Application
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the main application index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the emotion of the provided text input and returns the formatted response.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.get('dominant_emotion')

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

''' Executing the application of Emotion Detection over the Flask channel 
    and deployed on localhost:5002.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives text and runs emotion detection function
    over it using emotion_dection(). The output shows the different emotion 
    scores for the text provided.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyze)
    if len(text_to_analyze) == 0:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is {dominant_emotion}."



@app.route("/")
def render_index_page():
    ''' Rendering of the main application page over the Flask channel '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

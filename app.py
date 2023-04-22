from flask import Flask, render_template, request
import requests
import replicate_ai_models

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    images = request.files.getlist('images')
    for image in images:
        filename = image.filename
        # Will call our script to train the Model here.
    return render_template('train_model.html')

@app.route('/getBadge/<value>')
def api(value):
    response = getBadgeAPI(value)
    return f"<img src=\"{response}\"><img>"

@app.route('/getEnhancedImg')
def enhancedImg():
    response = replicate_ai_models.enhanceImage()
    return f"<img src=\"{response}\"><img>"

@app.route('/getAnimeImg')
def AnimeImg():
    response = replicate_ai_models.enhanceImage()
    return f"<img src=\"{response}\"><img>"

def getBadgeAPI(value):
    if value == 'value1':
        prompt = "painting of [v] person posing in front of Eiffel tower in black suit"
    elif value == 'value2':
        prompt = "beautiful painting of [v] person standing in front of eiffel tower" 
        print(prompt)
    return replicate_ai_models.createBadge(prompt)
if __name__ == '__main__':
    app.run()

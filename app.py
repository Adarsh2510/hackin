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
        prompt = """
        Add the image of [v] person with the following specifications:
        The Eiffel Tower should be visible in the background, positioned as if the [v] is standing in front of it
        The lighting should be consistent with the Eiffel Tower's surroundings
        [v] should be scaled appropriately so that he appear to be standing in front of the Eiffel Tower
        The image should be high resolution and suitable for use in a marketing campaign or print advertisement.
        """
    elif value == 'value2':
        prompt = "promt2" 
    return replicate_ai_models.createBadge(prompt)
if __name__ == '__main__':
    app.run()

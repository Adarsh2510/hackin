from flask import Flask, render_template, request
import requests
import replicate_ai_models
from prompt import example_prompt
import random
from PIL import Image
import subprocess
import requests
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():

    subprocess.run(['zip', '-r', 'data.zip', 'data'])

    api_token =  os.getenv('API_TOKEN')
    upload_url = 'https://dreambooth-api-experimental.replicate.com/v1/upload'

    with open('data.zip', 'rb') as file:
        headers = {'Authorization': f'Token {api_token}'}
        data = {'file': file}

        response = requests.post(upload_url, headers=headers, files=data)
        response_json = json.loads(response.text)

        upload_url = response_json['upload_url']
        upload_token = response_json['upload_token']

        with open('data.zip', 'rb') as file:
            headers = {'Content-Type': 'application/zip', 'Authorization': f'Token {upload_token}'}
            data = file

            response = requests.put(upload_url, headers=headers, data=data)

            response_json = json.loads(response.text)
            serving_url = response_json['serving_url']

            print(f'Serving URL: {serving_url}')

    input_data = {
        "instance_prompt": "a photo of a [v] person",
        "class_prompt": "a photo of a person",
        "instance_data": serving_url,
        "max_train_steps": 2000
    }

    data = {
        'input': input_data,
        'model': os.getenv('MODEL_NAME'),
        'trainer_version': 'cd3f925f7ab21afaef7d45224790eedbb837eeac40d22e8fefe015489ab644aa',
        'webhook_completed': 'https://example.com/dreambooth-webhook'
    }

    # Send the POST request to the trainings endpoint
    response = requests.post('https://dreambooth-api-experimental.replicate.com/v1/trainings', headers=headers, data=json.dumps(data))

    # Check the response status code and print the response content
    if response.status_code == 200:
        print(response.json())
    else:
        print(f'Error: {response.status_code} - {response.content}')

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
    prompt = random.choice(example_prompt)
    print(prompt)
    return replicate_ai_models.createBadge(prompt)

if __name__ == '__main__':
    app.run()

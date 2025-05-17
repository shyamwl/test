import os
from flask import Flask, render_template, request
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

# Configurable environment variables
PROJECT_ID = os.environ.get("PROJECT_ID")
LOCATION = os.environ.get("LOCATION", "us-central1")
MODEL_NAME = os.environ.get("MODEL_NAME", "gemini-2.5-pro")

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 100  # allow uploads up to 100MB

# Initialize Vertex AI when the app starts
vertexai.init(project=PROJECT_ID, location=LOCATION)
model = GenerativeModel(MODEL_NAME)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    uploaded_file = request.files.get('video')
    prompt = request.form.get('prompt', '')
    if not uploaded_file or not prompt:
        return render_template('index.html', output='Both video and prompt are required.')

    video_bytes = uploaded_file.read()
    video_part = Part.from_data(video_bytes, mime_type=uploaded_file.mimetype)

    try:
        response = model.generate_content([video_part, prompt])
        output_text = response.text
    except Exception as e:
        output_text = f'Error: {e}'

    return render_template('index.html', output=output_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

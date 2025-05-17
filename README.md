# Gemini Video Prompt App

This is a simple Flask application that demonstrates how to send a video file and prompt to the Google Vertex AI platform using the Gemini 2.5 Pro model.

## Requirements

- Python 3.9+
- Google Cloud credentials with access to Vertex AI

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running

Set environment variables for your Google Cloud project:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
export PROJECT_ID=your-project-id
export LOCATION=us-central1  # or other region
export MODEL_NAME=gemini-2.5-pro  # update if needed
```

Start the application:

```bash
python app.py
```

Open `http://localhost:8080` in your browser to upload a video and enter a prompt. After clicking **Run Prompt**, the application sends the video and prompt to Vertex AI and displays the returned text.

## Notes

- This example assumes the Gemini 2.5 Pro model accepts direct video bytes. Depending on the API, you may need to upload the video to Google Cloud Storage and pass the URI instead.
- Uploaded videos are not saved on disk.


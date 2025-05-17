# Gemini Video Application

This example demonstrates uploading a video file to Google Cloud Storage and
using the Vertex AI Gemini 2.5 Pro model to analyze the video with a prompt.

## Setup

1. Create a Google Cloud Storage bucket and set the environment variable
   `GCS_BUCKET_NAME` to that bucket name.
2. Ensure the service account running the app has permissions to generate
   signed URLs and access Vertex AI.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

Open `http://localhost:5000` in your browser to upload a video and enter a
prompt. The app uploads the video via a signed URL, invokes the Gemini model,
and displays the response.

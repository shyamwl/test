import os
import datetime
from flask import Flask, request, render_template, jsonify
from google.cloud import storage
from google import genai
from google.genai.types import HttpOptions, Part

app = Flask(__name__)

BUCKET_NAME = os.environ.get("GCS_BUCKET_NAME")


def generate_upload_signed_url_v4(bucket_name, blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    url = blob.generate_signed_url(
        version="v4",
        expiration=datetime.timedelta(minutes=15),
        method="PUT",
        content_type="application/octet-stream",
    )
    return url


def run_gemini(video_uri, prompt):
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=[
            Part.from_uri(file_uri=video_uri, mime_type="video/mp4"),
            prompt,
        ],
    )
    return response.text


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate-url", methods=["POST"])
def generate_url():
    data = request.get_json()
    file_name = data["file_name"]
    signed_url = generate_upload_signed_url_v4(BUCKET_NAME, file_name)
    return jsonify({"signed_url": signed_url})


@app.route("/run", methods=["POST"])
def run():
    data = request.get_json()
    video_uri = f"gs://{BUCKET_NAME}/{data['file_name']}"
    prompt = data["prompt"]
    answer = run_gemini(video_uri, prompt)
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True)

import os
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline

# HUGGING_FACE_API = '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'
# FACE_API = os.environ.get(key=HUGGING_FACE_API)
load_dotenv(find_dotenv())
# image to text
def image2text(url):
    pipe = pipeline("image-to-text", model="s3-tresio/blip-image-captioning-base")


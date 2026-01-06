# app/images.py
from imagekitio import ImageKit
import os
from dotenv import load_dotenv

load_dotenv()

imagekit = ImageKit()  # no args in v5.x

def upload_to_imagekit(file_path: str, file_name: str):
    with open(file_path, "rb") as f:
        response = imagekit.upload_file(
            file=f,
            file_name=file_name,
            options={
                "public_key": os.getenv("IMAGEKIT_PUBLIC_KEY"),
                "private_key": os.getenv("IMAGEKIT_PRIVATE_KEY"),
                "url_endpoint": os.getenv("IMAGEKIT_URL_ENDPOINT"),
                "use_unique_file_name": True,
                "tags": ["backend-upload"]
            }
        )
    return response

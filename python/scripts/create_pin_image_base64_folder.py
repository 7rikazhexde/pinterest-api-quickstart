#!/usr/bin/env python
import base64
import requests
import os

class PinterestPinCreator:
    def __init__(self, access_token):
        self.api_url = "https://api-sandbox.pinterest.com/v5/pins"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

    def create_pin(self, image_path, title, description, board_id):
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
        image_base64 = base64.b64encode(image_data).decode("utf-8")
        data = {
            "title": str(title),
            "description": str(description),
            "board_id": str(board_id),
            "media_source": {
                "source_type": "image_base64",
                "content_type": "image/jpeg",
                "data": image_base64
            }
        }
        response = requests.post(self.api_url, headers=self.headers, json=data)
        return response

if __name__ == "__main__":  # pragma: no cover
    access_token = "YOUR_ACCCESS_TOKEN(SANDBOX)"
    pinterest_pin_creator = PinterestPinCreator(access_token)

    image_path = "IMAGE_FILE_FOLDER_PATH"
    board_id = "BOARD_ID"

    for filename in sorted(os.listdir(image_path)):
        if filename == ".DS_Store":
            continue
        file_path = os.path.join(image_path, filename)
        if os.path.isfile(file_path):
            title = os.path.splitext(filename)[0]
            description = ""
            response = pinterest_pin_creator.create_pin(file_path, title, description, board_id)
            print(f"File: {filename}")
            print("Status Code:", response.status_code)
            print("Response Body:", response.text)
            print("---")
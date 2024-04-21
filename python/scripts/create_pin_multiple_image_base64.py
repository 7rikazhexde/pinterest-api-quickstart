#!/usr/bin/env python
import base64
import os
import requests

class PinterestPinCreator:
    def __init__(self, access_token):
        self.api_url = "https://api-sandbox.pinterest.com/v5/pins"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

    def create_pin_with_multiple_images(self, image_paths, board_id):
        image_data_list = []
        for image_path in image_paths:
            with open(image_path, "rb") as image_file:
                image_data = image_file.read()
                image_base64 = base64.b64encode(image_data).decode("utf-8")
                image_data_list.append({
                    "title": os.path.basename(image_path),
                    "description": "",
                    "content_type": "image/jpeg",
                    "data": image_base64
                })

        data = {
            "board_id": str(board_id),
            "media_source": {
                "source_type": "multiple_image_base64",
                "items": image_data_list
            },
            "index": 0
        }

        response = requests.post(self.api_url, headers=self.headers, json=data)
        return response

if __name__ == "__main__":  # pragma: no cover
    access_token = "YOUR_ACCCESS_TOKEN(SANDBOX)"
    pinterest_pin_creator = PinterestPinCreator(access_token)

    image_paths = [
        "FOLDER_PATH/IMAGE_FILE_NAME1", 
        "FOLDER_PATH/IMAGE_FILE_NAME2", 
        "FOLDER_PATH/IMAGE_FILE_NAME3"
    ]
    board_id = "BOARD_ID"

    response = pinterest_pin_creator.create_pin_with_multiple_images(image_paths, board_id)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    
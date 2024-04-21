#!/usr/bin/env python
import base64
import requests

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

    #image_path = input("Enter the path to the local image file: ")
    image_path = "FOLDER_PATH/IMAGE_FILE_NAME"
    title = input("Enter the title for the pin: ")
    description = input("Enter the description for the pin: ")
    board_id = "BOARD_ID"

    response = pinterest_pin_creator.create_pin(image_path, title, description, board_id)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
#!/usr/bin/env python
import requests

class PinterestPinCreator:
    def __init__(self, access_token):
        self.api_url = "https://api-sandbox.pinterest.com/v5/pins"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

    def create_pin(self, image_url, title, description, board_id):
        data = {
            "title": str(title),
            "description": str(description),
            "board_id": str(board_id),
            "media_source": {
                "source_type": "image_url",
                "url": str(image_url)
            }
        }

        response = requests.post(self.api_url, headers=self.headers, json=data)
        return response

if __name__ == "__main__":  # pragma: no cover
    access_token = "YOUR_ACCCESS_TOKEN(SANDBOX)"
    pinterest_pin_creator = PinterestPinCreator(access_token)

    image_url = input("Enter the url for the pin: ")
    title = input("Enter the title for the pin: ")
    description = input("Enter the description for the pin: ")
    board_id = "BOARD_ID"

    response = pinterest_pin_creator.create_pin(image_url, title, description, board_id)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
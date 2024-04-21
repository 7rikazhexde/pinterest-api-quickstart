#!/usr/bin/env python
import os
import re
import requests

def download_pinterest_image(pin_id, output_dir):
    api_url = f"https://api-sandbox.pinterest.com/v5/pins/{pin_id}"
    access_token = "YOUR_ACCCESS_TOKEN(SANDBOX)"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(api_url, headers=headers)
    data = response.json()

    pattern = re.compile(r"(\d+)x(\d+)?")

    resolutions = []
    for key in data["media"]["images"].keys():
        match = pattern.match(key)
        if match:
            width = int(match.group(1))
            height = int(match.group(2)) if match.group(2) else width
            resolutions.append((width, height, key))
    resolutions.sort(reverse=True)

    if resolutions:
        image_url = data["media"]["images"][resolutions[0][2]]["url"]
    else:
        image_url = None

    if image_url:
        response = requests.get(image_url)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(os.path.join(output_dir, f"{pin_id}.jpg"), "wb") as f:
            f.write(response.content)

        print(f"Image downloaded: {pin_id}.jpg")
    else:
        print(f"No suitable image found for Pin: {pin_id}")

if __name__ == "__main__":  # pragma: no cover
    pin_id = "PIN_ID"
    output_dir = "pinterest_images"
    download_pinterest_image(pin_id, output_dir)
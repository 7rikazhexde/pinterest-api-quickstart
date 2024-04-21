#!/usr/bin/env python
import requests

username = "USER_NAME"
access_token = "YOUR_ACCCESS_TOKEN(NO_SANDBOX)"

url = f"https://api.pinterest.com/v5/boards/?owner={username}"
headers = {"Authorization": f"Bearer {access_token}"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    for board in data["items"]:
        print(f"Board ID: {board['id']}, Board Name: {board['name']}")
else:
    print("Failed to retrieve boards.")
    print(f"Status code: {response.status_code}")
    print(f"Error message: {response.text}")
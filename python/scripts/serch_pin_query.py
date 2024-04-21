#!/usr/bin/env python
import requests

access_token = "YOUR_ACCCESS_TOKEN(NO_SANDBOX)"
query = "nature"

# Can be a value from 1 to 250. The default is 25.
page_size = 50

url = f"https://api.pinterest.com/v5/search/pins/?query={query}&page_size={page_size}"
headers = {"Authorization": f"Bearer {access_token}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(len(data["items"]))
    if "items" in data:
        for pin in data["items"]:
            print(f"Pin ID: {pin['id']}")
            print(f"Title: {pin['title']}")
            print(f"Description: {pin['description']}")
            print(f"URL: {pin['link']}")
            print("---")
    else:
        print("No search results found.")
else:
    print("Failed to search pins.")
    print(f"Status code: {response.status_code}")
    print(f"Error message: {response.text}")
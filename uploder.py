import requests
import os

FLIC_TOKEN = "<YOUR_TOKEN>"

def get_upload_url():
    headers = {
        "Flic-Token": FLIC_TOKEN,
        "Content-Type": "application/json"
    }
    response = requests.get("https://api.socialverseapp.com/posts/generate-upload-url", headers=headers)
    return response.json()

def upload_video(upload_url, file_path):
    with open(file_path, 'rb') as file:
        response = requests.put(upload_url, data=file)
    return response.status_code == 200

def create_post(hash, title, category_id=1):
    headers = {
        "Flic-Token": FLIC_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        "title": title,
        "hash": hash,
        "is_available_in_public_feed": False,
        "category_id": category_id
    }
    response = requests.post("https://api.socialverseapp.com/posts", headers=headers, json=payload)
    return response.json()

# This is an Test script for testing (in case postman is not supported or not working.)

import requests

base_url = "http://127.0.0.1:5000"  # Replace with the appropriate base URL of your Flask app

# Test the GET request to get the first article
response = requests.get(f"{base_url}/get_article")
print(response.json())  # Print the response JSON

# Test the POST request to mark the article as liked
response = requests.post(f"{base_url}/like_article")
print(response.json())  # Print the response JSON

# Test the POST request to mark the article as not liked
response = requests.post(f"{base_url}/not_like_article")
print(response.json())  # Print the response JSON

# Test the GET request again to see the updated article
response = requests.get(f"{base_url}/get_article")
print(response.json())  # Print the response JSON

# Made By Junaid (https://abujuni.dev).
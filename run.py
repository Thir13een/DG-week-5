import requests

# URL for the prediction API
url = 'http://127.0.0.1:5000/predict'


data = {
    'input': [6.2, 3.4, 5.4, 2.3]
}

response = requests.post(url, json=data)

print(response.json())
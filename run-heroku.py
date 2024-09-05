import requests

# URL for the prediction API on heroku
url = 'https://run-iris-794bce0fc4df.herokuapp.com/predict'

data = {
    'input': [6.2, 3.4, 5.4, 2.3]
}

response = requests.post(url, json=data)

print(response.json())

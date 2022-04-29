import requests
from app import app


api_key = app.config['API_KEY']
secret_key = app.config['SECRET_KEY']
url = app.config['BASE_URL']


def get_news():
    """API Call"""
    base_url = url.format(api_key)
    response = requests.get(base_url).json()
    print(response['articles'])
    return response['articles']
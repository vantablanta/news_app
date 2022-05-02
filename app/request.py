import requests
from app import app
from app.models import Source, News

api_key = app.config['API_KEY']
secret_key = app.config['SECRET_KEY']
base_url = app.config['BASE_URL']
sources_url = app.config['SOURCES_URL']
kenya_url = app.config['KENYA_URL']



def get_news():
    """NEWS API Call"""
    url = base_url.format(api_key)
    response = requests.get(url).json()
    return response['articles']

def get_sources():
    """SOURCES API Call"""
    url = sources_url.format(api_key)
    response = requests.get(url).json()
    return response['sources']

def get_kenya_news():
    """SOURCES API Call"""
    url = kenya_url.format(api_key)
    response = requests.get(url).json()
    response['articles']
    return response['articles']
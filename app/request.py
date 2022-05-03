import requests
from app.models import Source, News

api_key  = '451494679ce7417b92b2e90fe43214f0'
base_url ='https://newsapi.org/v2/top-headlines?q=news&apiKey={}'
sources_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
kenya_url = 'https://newsapi.org/v2/everything?q=kenya&apiKey={}'

def configure_request(app):
    global api_key,base_url, sources_url, kenya_url
    # api_key = app.config['API_KEY']
    # base_url = app.config['BASE_URL']
    # sources_url = app.config['SOURCES_URL']
    # kenya_url = app.config['KENYA_URL']

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
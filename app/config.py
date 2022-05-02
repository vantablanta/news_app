class Config:
    """Parent Config Class """
    BASE_URL = 'https://newsapi.org/v2/top-headlines?q=news&apiKey={}'
    SOURCES_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    KENYA_URL = 'https://newsapi.org/v2/everything?q=kenya&apiKey={}'

class ProdConfig(Config):
    """Production Config Class"""


class DevConfig(Config):
    """Developement Config"""
    DEBUG = True
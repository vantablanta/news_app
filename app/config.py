class Config:
    """Parent Config Class """
    BASE_URL = 'https://newsapi.org/v2/everything?sources=bbc-news&apiKey={}'

class ProdConfig(Config):
    """Production Config Class"""


class DevConfig(Config):
    """Developement Config"""
    DEBUG = True
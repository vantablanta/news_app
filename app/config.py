class Config:
    """Parent Config Class """
    BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    

class ProdConfig(Config):
    """Production Config Class"""


class DevConfig(Config):
    """Developement Config"""
    DEBUG = True
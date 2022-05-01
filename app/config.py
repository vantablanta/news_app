class Config:
    """Parent Config Class """
    BASE_URL = 'https://newsapi.org/v2/top-headlines?q=news&apiKey={}&pageSize=10'
    SOURCES_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    

class ProdConfig(Config):
    """Production Config Class"""


class DevConfig(Config):
    """Developement Config"""
    DEBUG = True
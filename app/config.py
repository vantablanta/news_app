from distutils.debug import DEBUG


class Config:
    """Parent Config Class """

class ProdConfig(Config):
    """Production Config Class"""

class DevConfig(Config):
    """Developement Config"""
    DEBUG = True
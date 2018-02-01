import os

class Config:
    
    '''
    general configuration parent class
    '''
    BASE_NEWS_API_URL='https://newsapi.org/v2/sources?language=en&country={}&category={}&apiKey={}'
    SOURCE_NEWS_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}' 
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')   
class ProdConfig(Config):
    '''
    production configuration child class
    Arg:
        config :The parent configuration class with General configurations settings
    '''
    pass

class DevConfig(Config): 
    '''
    development configuration child class
    Arg:
        config :The parent configuration class with General configurations settings
    '''

    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}


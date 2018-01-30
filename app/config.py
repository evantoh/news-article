class Config:
    '''
    general configuration parent class
    '''
    NEWS_API_KEY = '9b098e83fdcf425695945d23ddf98e4d' 
    BASE_NEWS_API_URL = 'https://newsapi.org/v2/top-headlines?country={}&category={}&apiKey={}'

    
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


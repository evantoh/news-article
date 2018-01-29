class Config:
    '''
    general configuration parent class
    '''
    SOURCE_NEWS_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_BASE_URL='https://newsapi.org/v2/top-headlines?country=&category={}&apiKey={}'
    
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


from  app import app
import urllib.request,json
from .models import news

#getting api key
api_key = app.config['NEWS_API_KEY']
print(api_key)
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(country,category,api_key):
    '''
    function that gets the json response to our url request
    '''
    get_news_url = base_url.format(country,category,api_key)

with urllib.request.urlopen(get_news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)

    news_results = None

    if get_news_response['results']:
        news_results_list = get_news_response['results']

        news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
        '''
        function that proceses the news results and transform them to
         a list of objects
        Args:
        news_list:a list of dictionaries that contain news details
        Returns:
        new_results: a list of movie objects
        '''
        news_results = []
        for news_item in news_list:

        






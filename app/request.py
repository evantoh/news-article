from  app import app
import urllib.request,json
from .models import source
Source = source.Source

#getting api key
api_key = app.config['NEWS_API_KEY']

source_url = app.config['NEWS_API_BASE_URL']

def get_sources(category):
    '''
    function that gets the json response to our url request
    '''
    get_sources_url = source_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        #

        if get_source_response['articles']:
            source_results_list = get_source_response['articles']

            source_results = process_source_results(source_results_list)

    return source_results

def process_source_results(source_list):
        '''
        function that proceses the news results and transform them to
         a list of objects
        Args:
        news_list:a list of dictionaries that contain news details
        Returns:
        new_results: a list of movie objects
        '''
        source_results = []
        for source_item in source_list:
           
            # author = source_item('author')
            title=source_item.get('title')
            urlToImage=source_item.get('urlToImage')
            description=source_item.get('description')
            url=source_item.get('url')
            publishedAt=source_item.get('publishedAt')
            
            
            

            if url:
             
                source_object =Source(title,description,url,urlToImage,publishedAt)
                source_results.append(source_object)

        return source_results 
    
  





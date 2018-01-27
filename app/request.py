from  app import app
import urllib.request,json
from .models import source
Source = source.Source

#getting api key
api_key = app.config['NEWS_API_KEY']

source_url = app.config["SOURCE_API_BASE_URL"]

def get_sources():
    '''
    function that gets the json response to our url request
    '''
    get_sources_url = source_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
                source_results_list = get_source_response['sources']

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
            id =source_item.get('id')
            name = source_item.get('name')
            description = source_item.get('description')
            source = source_item.get('source')
            category= source_item.get('category')
          
            
            

            
            source_object =Source(id,name,description,source,category)
            source_results.append(source_object)

        return source_results 
    
  





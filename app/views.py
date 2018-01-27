from flask  import render_template
from app import app
from .request import get_sources
 
 #view
@app.route('/')
def index():
    # popular_sources = get_sources('id','api_key')
    # print(popular_sources)
    title = 'Hello-Welcome to news site'
    return render_template('index.html',message = title)

@app.route('/news/<int:news_id>')
def news(news_id):
     '''
    View news page function that returns the news details page and its data
    '''
     return render_template('news.html',id = news_id)
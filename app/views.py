from flask  import render_template
from app import app
from .request import get_news
 
 #view
@app.route('/')
def index():
    popular_news = get_news('country','category')
    print(popular_news)
    title = 'Hello-Welcome to news site'
    return render_template('index.html',message = title,popular =popular_news)

@app.route('/news/<int:news_id>')
def news(news_id):
     '''
    View news page function that returns the news details page and its data
    '''
     return render_template('news.html',id = news_id)
from flask import render_template
from app import app
from .request import get_sources, get_articles



@app.route('/')
def index():
    general_list = get_sources('us', 'general')
    business_list = get_sources('us', 'business')
    technology_list = get_sources('us', 'technology')
    sports_list = get_sources('us', 'sports')
    health_list = get_sources('us', 'health')
    science_list = get_sources('us', 'science')
    entertainment_list = get_sources('us', 'entertainment')
    test_args = 'Welcome to top headline!'
    return render_template('index.html',test_param=test_args,general=general_list,business=business_list,technology=technology_list,sports=sports_list,
health=health_list,science=science_list,entertainment=entertainment_list)


@app.route('/news/<id>')
def news(id):
    
    news_args = get_articles(id)
    highlight_args = 'hulllah you made it here !!'
    # name = f'{results_list}'
    return render_template('news.html', highlight_param=highlight_args,news=news_args)

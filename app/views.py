from flask  import render_template
from app import app
from .request import get_sources
 
 #view
@app.route('/')
def index():
    sports = get_sources('us','sports')
  
    title='Home - welcome to top headlines'
    return render_template('index.html', sports = sports)

@app.route('/articles/<highlight>')
def articles(highlight):
    test_highlight ='they are ok'
    
    return render_template('source.html', highlights =test_highlight)

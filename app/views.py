from flask  import render_template
from app import app
from .request import get_sources
 
 #view
@app.route('/')
def index():
    general_sources = get_sources('general')
    technology = get_sources('technology')
    sports = get_sources('sports')
    business = get_sources('business')
    health = get_sources('health')
    print(general_sources)


    message='Hello World'
    title='Home - welcome to the best news webiste online'
    return render_template('index.html',health = health,title=title, technology=technology, sports=sports, business=business, general=general_sources)

@app.route('/source/<id>')
def news(id):
   new_id = id
   title = f'{new_id}'
    
   return render_template('source.html',title =title,new_id = new_id )
from flask  import render_template
from app import app
 
 #view
@app.route('/')
def index():
    return render_template('index.html')

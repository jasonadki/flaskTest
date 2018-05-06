from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jason'}
    posts = [
    	{
    		'author' : {'username': 'Josh'},
    		'body' : 'Hey I"m Josh'
    	},
    	{
    		'author' : {'username': 'Chris'},
    		'body' : 'Hi I"m Christian'
    	},
    	{
    		'author' : {'username': 'Josh'},
    		'body' : 'Hey Chris whats up'
    	}
    ]
    return render_template('index.html', title = 'Home', user = user, posts	= posts)
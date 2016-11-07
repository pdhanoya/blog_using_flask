from flask import render_template, flash, redirect, url_for, request
from myproject import app
from .forms import LoginForm

@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is
# accepting: POST requests in this case
@app.route('/', methods=['POST'])
def hello():
    name=request.form['yourname']

    return render_template('form_submit.html', name=name)


'''
@app.route('/index')
def index():
	user = {'nickname':'Param'}
	posts = [ {
	'author' : {'nickname' :'John'},
	'body' : 'Beautiful day in  Portland!'
	},
	{
		'author' : {'nickname': 'Susan'},
		'body' : 'The Avengers movie was so cool'
	}
	]
	return render_template('index.html', title = 'Home', user = user)


@app.route('/text/<text>')
def show_text(text):
	return text

@app.route('/helloWorld')
def helloWorld():
	return "Hello World"
'''

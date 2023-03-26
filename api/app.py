"""
Skyscraper is a web scraping API built with Flask and deployed using Docker. It uses Beautiful Soup,
Pandas, and other powerful string manipulation libraries to scrape data from websites and provide the
results in various formats including JSON, YAML, and CSV. The project also includes OAuth2 authentication,
a database connection, and dynamic rendering of pages using Jinja templates and Bootstrap.

Import Files
------------

Initialize Flask App
--------------------

Single Page App with api endpoints
----------------------------------

"""
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# Initialize Flask App
app = Flask(__name__)

# set up templates and static folders for Flask app with jinja
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['DEBUG'] = True
app.template_folder = 'templates'


# Single Page App with api endpoints
@app.route('/')
def index():
    return render_template('index.html')

# Run Flask App
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

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
from config import conf
import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, make_response, abort, send_from_directory, send_file, Response, session, Request

# from flask.templating

# from flask_cors import CORS TODO - add CORS

# Initialize Flask App
app = Flask(__name__)

# set up templates and static folders for Flask app with jinja
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config["DEBUG"] = True
app.config["ENV"] = "development"
app.template_folder = os.environ.get("template_folder")
app.static_folder = os.environ.get("static_folder")

# middleware


@app.before_request
def before_request():
    pass


# error handlers
@app.errorhandler(404)  # page not found
def page_not_found(e):
    pass
    """TODO - add 404 page"""
    # return render_template('404.html'), 404


@app.errorhandler(500)  # internal server error
def internal_server_error(e):
    pass
    """TODO - add 500 page"""
    # return render_template('500.html'), 500


# Single Page App with api endpoints
@app.route("/")
def index():
    """TODO connect to database"""
    """TODO create form class to hold form fields """
    """TODO generate models for data from scraping
            module, and models for saving search
            criteria with better results and scrub
            it for creating tensorflow model"""
    return render_template("index.html", title="Skyscraper")  # q: wahts wrong with this?
#


# Run Flask App
if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

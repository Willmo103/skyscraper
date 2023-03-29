"""
This module defines the configuration settings for the web scraping API.
Since environment variables are being used, this file contains only basic
configuration for local development purposes. The production environment
variables are set via the Docker Compose file.
"""
import os
import dotenv


class Conf():
    def __init__(self):
        if os.environ.get('FLASK_ENV') == 'development':
            self.__dev_from_env()
        self._db_host = os.environ.get('DB_HOST')
        self._db_user = os.environ.get('DB_USER')
        self._db_pass = os.environ.get('DB_PASS')
        self._db_name = os.environ.get('DB_NAME')
        self._db_port = os.environ.get('DB_PORT')
        self._database_url = os.environ.get('DATABASE_URL')
        self._static_folder = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'static')
        self._template_folder = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'templates')
        os.environ.update({"static_folder": self._static_folder})
        os.environ.update({"template_folder": self._template_folder})

    @classmethod
    def __dev_from_env(cls):
        """ auxiliary constructor sets environment variables from .env file"""
        dotenv.load_dotenv()
        return cls()

    @property
    def db_url(self) -> str:
        """ returns the database url for postgres """
        return f'postgresql://{self._db_user}:{self._db_pass}@{self._db_host}:{self._db_port}/{self._db_name}'

    @property
    def static_folder(self) -> str:
        """ returns the static folder path """
        return self._static_folder

    @property
    def template_folder(self) -> str:
        """ returns the template folder path """
        return self._template_folder

    def __repr__(self):
        return None


conf = Conf()

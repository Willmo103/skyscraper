"""Tests for the Config class live here."""

import os, pytest
from config import Conf

def test_constructor_raises_error_when_no_env_vars():
    """Test that the constructor raises an error when no environment variables are set."""
    with pytest.raises(Exception):
        Conf()

def test_constructor_sets_db_host():
    """Test that the constructor sets the db_host attribute."""
    os.environ['DB_HOST'] = 'localhost'
    assert Conf().db_host == 'localhost'


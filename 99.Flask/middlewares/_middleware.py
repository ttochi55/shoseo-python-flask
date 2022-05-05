# Miscellaneous operating system interfaces
import os

# Basic date and time types
from datetime import date, datetime, timedelta

# Higher-order functions and operations on callable objects
from functools import wraps, update_wrapper

# The Python micro framework for building web applications.
from flask import make_response, request, abort

# Import custom bin and module files.
from modules.os import get_app_dir

# Set the absolute directory path.
appdir = get_app_dir()

# Remove Cache
# https://frhyme.github.io/python-lib/flask_matplotlib/
def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return update_wrapper(no_cache, view)

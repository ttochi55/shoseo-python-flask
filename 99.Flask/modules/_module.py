# Miscellaneous operating system interfaces
import os

# A light weight extension of the default python dict object. This allows for the use of key names as object attributes.
from dotted_dict import DottedDict

# Import custom bin and module files.
from modules.os import get_app_dir

# Set the absolute directory path.
appdir = get_app_dir()


def sample():
    pass
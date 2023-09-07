#!/usr/bin/python

import json

import sadface as sf

from . import config


def init(config_pathname=None):
    """
    Initialises ArgDB. If a configuration file is supplied then that is used
    otherwise a default configuration is generated and saved to the working
    directory in which ArgDB was initiated.
    """
    if config_pathname is None:
        config.generate_default()
        config_pathname = config.get_config_name()

    current_config = config.load(config_pathname)
    

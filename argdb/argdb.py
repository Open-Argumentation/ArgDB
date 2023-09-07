#!/usr/bin/python

import json

import sadface as sf

from . import config


def info():
    """
    Retrieve overview information about the status of ArgDB &
    it's constituent datastores, for example,

    {
        'Num Datastores': '1', 
        'Datastore List': '["argdb"]', 
        'Datastore Info': [
            {'Name': 'argdb', 'Num Docs': 4}
        ]
    }

    Returns a dict describing ArgDB contents
    """
    info = {}
    stores = get_datastores()

    info["Num Datastores"] = str(len(stores))
    info['Datastore List'] = stores
    info['Datastore Info'] = []
    for store in stores:
        data = {}
        data['Name'] = store
        data['Type'] = config.current.get(store, "type")
        info['Datastore Info'].append(data)

    return info


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
    

def get_datastores():
    """
    Retrieve a list of all extant datastores
    """
    return config.current.sections()


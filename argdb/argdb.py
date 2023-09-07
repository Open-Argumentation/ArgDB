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
#    stores = get_datastores()

    info["Num Datastores"] = 0#str(len(stores))
    info['Datastore List'] = []
    info['Datastore Info'] = []
#    for store in stores:
#        data = {}
#        data['Name'] = store
#        data['Num Docs'] = get_size(store)
#        info['Datastore Info'].append(data)

    return info


def init(config_pathname=None):
    """
    Initialises ArgDB. If a configuration file is supplied then that is used
    otherwise a default configuration is generated and saved to the working
    directory in which ArgDB was initiated.
    """
    print("Starting ArgDB...")
    if config_pathname is None:
        config.generate_default()
        config_pathname = config.get_config_name()

    print("Loading configuration from file: "+str(config_pathname))
    current_config = config.load(config_pathname)
    
    if current_config is not None:
        print("Loaded configuration successfully")
        #datastore_list = get_datastores()
        #print("This ArgDB instance has the following datastores defined: "+str(datastore_list))



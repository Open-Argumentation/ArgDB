#!/usr/bin/python

import json

import sadface as sf

from . import config
from . import utils
from . datastores import type_tinydb as tdb

def add_datastore(db_name, db_type):
    """
    Given a datastore name and type, create a new datastore &
    add it to our configuration.

    This is part of the public API for ArgDB & delegates to a
    specific datastorage type (from the datastores sub-package)
    """
    if config.add_datastore_config_entry(db_name, db_type):
        if db_type == "tinydb":
            return tdb.add_datastore(db_name)
        else:
            config.remove_datastore_config_entry(db_name)

def add_doc(db_name, doc):
    """
    Given a nominated datastore and a SADFace document, verifies
    the doc then adds it to the store

    This is part of the public API for ArgDB & delegates to a
    specific datastorage type (from the datastores sub-package)
    """
    result, problems = sf.validation.verify(doc)
    if not result:
        db = get_datastore(db_name)
        if db is not None:
            if "tinydb" == get_datastore_type(db_name):
               tdb.add_doc(db_name, doc) 
    else:
        return result, problems

def clear_datastore(db_name):
    """
    Give an datastore name, removes it's contents

    This is part of the public API for ArgDB & delegates to a
    specific datastorage type (from the datastores sub-package)
    """
    db = get_datastore(db_name)
    if db is not None:
        if "tinydb" == get_datastore_type(db_name):
            tdb.clear_datastore(db_name)

def delete_datastore(db_name):
    """
    Deletes the named datastore

    This is part of the public API for ArgDB & delegates to a
    specific datastorage type (from the datastores sub-package)
    """    
    db = get_datastore(db_name)
    if db is not None:
        if "tinydb" == get_datastore_type(db_name):
            tdb.delete_datastore(db_name)
        
        config.remove_datastore_config_entry(db_name)
       

def delete_doc(db_name, doc_id):
    """
    Deletes the document, identified by the supplied ID, from
    the nominated datastore.

    This is part of the public API for ArgDB & delegates to a
    specific datastorage type (from the datastores sub-package)
    """
    db = get_datastore(db_name)
    if db is not None:
        if "tinydb" == get_datastore_type(db_name):
            tdb.delete_doc(db_name, doc_id)

def get_datastore(db_name):
    """
    Given a datastore name, return a handle to it.

    This is part of the public API for ArgDB & delegates to a
    specific datastorage type (from the datastores sub-package)

    Returns a valid datastore or None
    """
    if db_name in get_datastores():
        if "tinydb" == get_datastore_type(db_name):
            return tdb.get_datastore(db_name)

def get_datastore_type(db_name):
    """
    Given a datastore name, returns the type of the datastore
    where that is recorded in the configuration file

    Note that suppoted types are defined wholly by entries in
    the datastores sub-package
    """
    return config.current.get(db_name, "type")

def get_datastores():
    """
    Retrieve a list of all extant datastores
    """
    return utils.rectify(config.current.get('datastores','names'))

def get_doc(db_name, doc_id):
    """
    Retrieve a specific doc, identified by the supplied ID, from 
    the nominated datastore.

    This is part of the public API for ArgDB & delegates to a
    specific datastorage type (from the datastores sub-package)
    """
    db = get_datastore(db_name)
    if db is not None:
        if "tinydb" == get_datastore_type(db_name):
            return tdb.get_doc(db_name, doc_id)

def info():
    """
    Retrieve overview information about the status of ArgDB &
    it's constituent datastores, for example,

    {
        'Num Datastores': '1', 
        'Datastore List': '["default"]', 
        'Datastore Info': [
            {'Name': 'default', 'Num Docs': 4}
        ]
    }

    Returns a dict describing ArgDB contents
    """
    info = {}
    stores = utils.rectify(config.current.get('datastores','names'))

    info["Num Datastores"] = str(len(stores))
    info['Datastore List'] = str(config.current.get('datastores','names'))
    info['Datastore Info'] = []
    for store in stores:
        data = {}
        data['Name'] = store
        data['Num Docs'] = get_datastore(store).__len__()
        info['Datastore Info'].append(data)

    return info

def init(config_pathname=None):
    """
    Initialises ArgDB. If a configuration file is supplied then that is used
    otherwise a default configuration is generated and saved to the working
    directory in which ArgDB was initiated.
    """
    print("Starting ArgDB...")
    if config_pathname is None:
        config.generate()
        config_pathname = "default.cfg"

    print("Loading configuration from file: "+str(config_pathname))
    current_config = config.load(config_pathname)
    
    if current_config is not None:
        datastore_types = current_config.get('datastores','types')
        datastore_list = current_config.get('datastores','names')
        print("This ArgDB instance supports the following datastore types: "+str(datastore_types))
        print("This ArgDB instance has the following datastores defined: "+str(datastore_list))

def search(db_name, query):
    """
    """
    pass

#!/usr/bin/python

import inspect
import json

def rectify(input_string):
    """
    Replaces single quotes in the input string with double quotes
    so that the resulting string can be treated as valid JSON and
    loaded into a Python list object.

    NB. Fixes a weird edge case where lists are loaded from a config
    (ini) file as a string with single quotes but these can't be 
    used/parsed directly into a list for processing.

    Returns: a python object
    """
    return json.loads(str(input_string).replace("'", '"'))

def validate_datastore_api():
    """
    Determines whether a datastore type implements our data storage API.

    Checks the source of each datastore descriptions in argdb.datastores
    for the presence of the following functions:
        add_datastore 
        add_doc
        clear_datastore 
        delete_datastore 
        delete_doc 
        get_datastore 
        get_doc 
    """
    result = {}
    result['tinydb'] = validate_type_tinydb()

    return result
    

def validate_type_tinydb():
    """
    Validates the tinydb API from the datastores sub-package

    Returns a pair (l, r) in which the left object shows the required 
    api functions not present in the datastore descriptor and the right
    side shows the functions in the datastore descriptor that aren't 
    defined in the API. Returns True for l or r if there is no difference
    """
    from . datastores import type_tinydb
    
    api = ['add_datastore','add_doc','clear_datastore','delete_datastore','delete_doc','get_datastore','get_doc']
    fun_list = []
    for name, data in inspect.getmembers(type_tinydb, inspect.isfunction):
        if name.startswith('__'):
            continue
        else:
            fun_list.append(name)

    if set(api) == set(fun_list):
        return True
    else:
        diff_l = set(api).difference(fun_list)
        if len(diff_l) == 0:
            diff_l = True
        diff_r = set(fun_list).difference(api)
        if len(diff_r) == 0:
            diff_r = True

        return diff_l, diff_r


        

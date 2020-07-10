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
        

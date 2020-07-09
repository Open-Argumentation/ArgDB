#!/usr/bin/python

import json
import os
import uuid
import requests as rq
import sadface as sf

from .. import config

def add_datastore(db_name):
    """
    This function is a requirement of the ArgDB plugin architecture

    Returns: 

    """
    url = get_datastore(db_name)
    if not db_exists(url):
        try:
            r = rq.put(url)
            r.raise_for_status()           
        except rq.exceptions.HTTPError as e:
            print(e)

def add_doc(db_name, doc):
    """

    This function is a requirement of the ArgDB plugin architecture

    Returns: None
    """
    pass

def clear_datastore(db_name):
    """

    This function is a requirement of the ArgDB plugin architecture

    Returns: None
    """
    pass

def db_exists(db_name):
    """
    Check whether a nominated DB exists

    Returns: True if the nominated DB exists, False otherwise
    """
    r = rq.get(db_name)
    if r.status_code == rq.codes.ok:
        return True
    else:
        return False
 
def delete_datastore(db_name):
    """

    This function is a requirement of the ArgDB plugin architecture

    Returns: None
    """
    pass

def delete_doc(db_name, doc_id):
    """

    This function is a requirement of the ArgDB plugin architecture

    Returns: None
    """
    pass


def get_datastore(db_name):
    """
    object.

    This function is a requirement of the ArgDB plugin architecture

    Returns: 
    """
    db_type = config.current.get(db_name, "type")
    db_ip   = config.current.get(db_name, "ip")
    db_port = config.current.get(db_name, "port")
    db_protocol = config.current.get(db_name, "protocol")
    db_username = config.current.get(db_name, "username")
    db_password = config.current.get(db_name, "password")

    url = db_protocol + "://" + db_username + ":" + db_password + "@" + db_ip + ":" + db_port + "/" + db_name + "/"
    return url


def get_doc(db_name, doc_id):
    """

    This function is a requirement of the ArgDB plugin architecture

    Returns: A SADFace document
    """
    pass

def get_size(db_name):
    """
    """
    return 666
    

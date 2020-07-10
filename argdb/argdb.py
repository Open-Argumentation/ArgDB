#!/usr/bin/python

import json
import requests as rq

import sadface as sf

from . import config
from . import utils

def add_datastore(db_name):
    """
    Given a datastore name and type, create a new datastore &
    add it to our configuration.

    This is part of the public API for ArgDB & delegates to a
    specific datastorage type (from the datastores sub-package)
    """
    print("adding datastore")
    config.add_datastore_config_entry(db_name)
    url = get_datastore(db_name)
    if not db_exists(url):
        try:
            r = rq.put(url)
            r.raise_for_status()         
        except rq.exceptions.HTTPError as e:
            print(e)

def add_doc(db_name, doc):
    """
    Given a nominated datastore and a SADFace document, verifies
    the doc then adds it to the store

    This is part of the public API for ArgDB & delegates to a
    specific datastorage type (from the datastores sub-package)
    """
    result, problems = sf.validation.verify(doc)
    if not result:
        docid = sf.get_document_id(doc)
        print("docid="+str(docid))
        url = get_datastore(db_name)
        print("url="+str(url))
        r = rq.put(url + docid, data=json.dumps(doc))
    else:
        return result, problems

def clear_datastore(db_name):
    """
    Give an datastore name, removes it's contents. 

    Dirty Hack Warning!!! 
    We could also do this using the CouchDB bulk document API but 
    it is easier to just delete and re-create the entire database.

    This is part of the public API for ArgDB & delegates to a
    specific datastorage type (from the datastores sub-package)
    """
    delete_datastore(db_name)
    add_datastore(db_name)

def delete_datastore(db_name):
    """
    Deletes the named datastore

    This is part of the public API for ArgDB & delegates to a
    specific datastorage type (from the datastores sub-package)
    """
    config.remove_datastore_config_entry(db_name)
    url = get_datastore(db_name)
    result = rq.delete(url)
    if result.status_code == rq.codes.ok:
        return True
    else:
        return False


def delete_doc(db_name, doc_id):
    """
    Deletes the document, identified by the supplied ID, from
    the nominated datastore.

    This is part of the public API for ArgDB & delegates to a
    specific datastorage type (from the datastores sub-package)
    """
    doc = get_raw_doc(db_name, doc_id)
    doc = json.loads(doc)
    rev = doc.get("_rev")
    url = get_datastore(db_name)
    r = rq.delete(url + doc_id + "?rev="+rev)

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

def get_datastore(db_name):
    """
    Given a datastore name, return a handle to it.

    This is part of the public API for ArgDB & delegates to a
    specific datastorage type (from the datastores sub-package)

    Returns a valid datastore or None
    """
    db_ip   = config.current.get(db_name, "ip")
    db_port = config.current.get(db_name, "port")
    db_protocol = config.current.get(db_name, "protocol")
    db_username = config.current.get(db_name, "username")
    db_password = config.current.get(db_name, "password")

    url = db_protocol + "://" + db_username + ":" + db_password \
        + "@" + db_ip + ":" + db_port + "/" + db_name + "/"
    return url

def get_datastores():
    """
    Retrieve a list of all extant datastores
    """
    return config.current.sections()

def get_doc(db_name, doc_id):
    """
    Retrieve a specific doc, identified by the supplied ID, from 
    the nominated datastore.

    This is part of the public API for ArgDB & delegates to a
    specific datastorage type (from the datastores sub-package)
    """
    """
    db = get_datastore(db_name)
    if db is not None:
        if "tinydb" == get_datastore_type(db_name):
            return tdb.get_doc(db_name, doc_id)
        elif "couchdb" == get_datastore_type(db_name):
            return cdb.get_doc(db_name, doc_id)
    """
    doc = get_raw_doc(db_name, doc_id)
    doc = json.loads(doc)
    doc.pop("_id")
    doc.pop("_rev")
    return doc

def get_raw_doc(db_name, doc_id):
    """
    Get the SADFace document, identified by docid, from the named datastore

    This function is a requirement of the ArgDB plugin architecture

    Returns: A SADFace document
    """
    url = get_datastore(db_name)
    r = rq.get(url + doc_id)
    return r.text

def get_size(db_name):
    """
    """
    url = get_datastore(db_name)
    response = rq.get(url)
    db_info = json.loads(response.text)
    num_docs = db_info.get("doc_count")
    return num_docs

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
    stores = get_datastores()

    info["Num Datastores"] = str(len(stores))
    info['Datastore List'] = stores
    info['Datastore Info'] = []
    for store in stores:
        data = {}
        data['Name'] = store
        data['Num Docs'] = get_size(store)
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
        config_pathname = "argdb.cfg"

    print("Loading configuration from file: "+str(config_pathname))
    current_config = config.load(config_pathname)
    
    if current_config is not None:
        print("Loaded configuration successfully")
        datastore_list = get_datastores()
        print("This ArgDB instance has the following datastores defined: "+str(datastore_list))

def search(db_name, query):
    """
    """
    pass

def update_doc(db_name, doc):
    """
    Update the document, identified by docid, in the datastore

    Expects: Will accept a SADFace doc encoded either as a JSON string
    or loaded into a Python dict

    Returns: None
    """
    new = None
    if type(doc) is str:
        new = json.loads(doc)
    elif type(doc) is dict:
        new = doc

    url = get_datastore(db_name)
    doc_id = sf.get_document_id(new)
    old = get_raw_doc(db_name, doc_id)
    
    old = json.loads(old)
    rev = old.get("_rev")
    new["_id"] = doc_id
    new["_rev"] = rev

    r = rq.put(url + doc_id, data=json.dumps(new))
    

#!/usr/bin/python

import json
import os
import uuid
from tinydb import TinyDB, Query
import sadface as sf

def add_datastore(db_name):
    """
    Add a new TinyDB datastore for usage. Note that a side-effect
    of this function is the creation of a database file on disk.

    This function is a requirement of the ArgDB plugin architecture

    Returns: A TinyDB instance of the given name

    """
    return TinyDB(db_name)

def add_doc(db_name, doc):
    """
    Adds the supplied document to the nominated DB. Assumes that
    validity checks on the document have been applied before calling
    this function, e.g. call to sadface.validation.verify(doc) for
    SADFace documents

    Returns: None
    """
    doc_id = sf.get_document_id(doc)
    if get_doc(db_name, doc_id) is not None:
        db = get_datastore(db_name)
        if db is not None:
            db.insert(doc)

def clear_datastore(db_name):
    """
    Removes all contents from the nominated datastore

    This function is a requirement of the ArgDB plugin architecture

    Returns: None
    """
    db = get_datastore(db_name)
    if db is not None:
        db.truncate()
        
def delete_datastore(db_name):
    """
    Removes the underlying file that holds the named DB.

    This function is a requirement of the ArgDB plugin architecture

    Returns: None
    """
    clear_datastore(db_name)
    if os.path.exists(db_name):
        os.remove(db_name)

def delete_doc(db_name, doc_id):
    """
    Removes the document, identified by doc_id, from the nominated DB.

    This function is a requirement of the ArgDB plugin architecture

    Returns: None
    """
    db = get_datastore(db_name)
    if db is not None:
        doc = Query()
        db.remove(doc.metadata.core.id == doc_id)

def get_datastore(db_name):
    """
    Returns a handle to the named Datastore, in this case a TinyDB
    object.

    This function is a requirement of the ArgDB plugin architecture

    Returns: A TinyDB Object
    """
    return TinyDB(db_name)

def get_doc(db_name, doc_id):
    """
    Returns the first SADFace document from the nominated datstore whose
    ID matches that supplied.

    This function is a requirement of the ArgDB plugin architecture

    Returns: A SADFace document
    """
    db = get_datastore(db_name)
    if db is not None:
        doc = Query()
        result = db.search(doc.metadata.core.id == doc_id)
        return result

def get_size(db_name):
    """
    """
    db = get_datastore(db_name)
    return db.__len__()


#!/usr/bin/python

import json
import sqlite3

import sadface as sf

from . import config

db = None

def cleanup():
    """

    """
    db.close()
    exit(1)


def add_doc(new_doc, overwrite=False):
    """
    Add a validated SADFace document to the datastore. If overwrite is True then overwrite an existing document,
    otherwise disallow duplicates. A duplicate is considered to be so under the minimal constraint of: a document 
    that has the same id in metatdata>core. SADFace document validation is entirely handled by the SADFace library.

    """
    result = sf.validation.verify(new_doc)

    if result[0] == True:
        if overwrite:
            try:
                docid = sf.get_document_id(json.loads(new_doc))
                cursor = db.cursor()
                cursor.execute("UPDATE raw SET data = json('"+new_doc+"') where id = '"+docid+"'")
                db.commit()
            except sqlite3.Error as error:
                print("Couldn't add your SADFace document to ArgDB due to the following:", error)
        else:
            try:
                docid = sf.get_document_id(json.loads(new_doc))
                cursor = db.cursor()
                cursor.execute("INSERT INTO raw (id, data) VALUES ('"+docid+"',json('"+new_doc+"') );")
                db.commit()
            except sqlite3.IntegrityError as error:
                print("Couldn't add your SADFace document to ArgDB due to the following:", error)
    else:
        print("Couldn't add document to DB as it failed SADFace validation due to the following:",result[1])

def clear():
    """

    """
    cursor = db.cursor()
    cursor.execute('DROP TABLE IF EXISTS raw')
    init_db()


def delete_doc(docid):
    """

    """
    cursor = db.cursor()
    cursor.execute("DELETE FROM raw WHERE id = '"+docid+"'")
    db.commit()


def get_doc(docid):
    """

    """
    try:
        cursor = db.cursor()
        data = cursor.execute("SELECT data FROM raw WHERE id = '"+docid+"'")
        data = cursor.fetchone()

        if data is not None:
            return data[0]
            
    except sqlite3.Error as error:
        print("Failed to read data from table", error)

    return None


def get_docs():
    """

    """
    try:
        cursor = db.cursor()
        data = cursor.execute("SELECT id FROM raw")
        data = cursor.fetchall()

        if data is not None:
            docs = []
            for row in data:
                docs.append(row[0])
            return docs
            
    except sqlite3.Error as error:
        print("Failed to read data from table", error)

    return []

def init(config_pathname=None):
    """
    Initialises ArgDB. If a configuration file is supplied then that is used
    otherwise a default configuration is generated and saved to the working
    directory in which ArgDB was initiated.
    """
    init_config()
    init_db()
    

def init_config(config_pathname=None):
    """

    """
    if config_pathname is None:
        config.generate_default()
        config_pathname = config.get_config_name()

    current_config = config.load(config_pathname)


def init_db():
    """

    """
    global db
    dbname = config.current.get('datastore', "name")

    db = sqlite3.connect(dbname+'.sqlite3')

    cur = db.cursor()
    
    cur.executescript('''
        CREATE TABLE IF NOT EXISTS raw (
        id   TEXT PRIMARY KEY,
        data JSON);
        ''')

    db.commit()


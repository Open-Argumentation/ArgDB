#!/usr/bin/python

from configparser import ConfigParser, NoSectionError
import json
import os

current = None
config_pathname = None

def generate_default(name='argdb.cfg'):
    """
    Create a new default configuration file called argdb.cfg
    """
    global config_pathname
    config_pathname = name
    
    if not os.path.exists(config_pathname):
        cp = ConfigParser()
        cp['argdb'] = {'ip': '127.0.0.1','port': '5984','protocol': 'http','username': 'admin','password': 'password'}
        cp.write(open(config_pathname, 'w'))

def get_config_name():
    return config_pathname

def get_url_from_config(db_name):
    """
    Construct & return the URL for a given datastore from the
    associated config entry
    """
    try:
        db_ip   = current.get(db_name, "ip")
        db_port = current.get(db_name, "port")
        db_protocol = current.get(db_name, "protocol")
        db_username = current.get(db_name, "username")
        db_password = current.get(db_name, "password")

        url = db_protocol + "://" + db_username + ":" + db_password \
            + "@" + db_ip + ":" + db_port + "/" + db_name + "/"
        return url
    except NoSectionError:
        return None

def load(pathname=None):
    """
    Load a configuration file
    """
    if(pathname is not None):
        try:
            global current, config_pathname
            config_pathname = pathname
            current = ConfigParser()
            current.read(pathname)
            return current
        except:
            print("Could not read configs from " + pathname)
            exit(1) 
    else:
        raise Exception("Tried to load config file but pathname (location) was set to None")
        exit(1)

def add_datastore_config_entry(db_name):
    """
    Add a new datastore entry to the in memory config & persist changes to disk

    A datastore entry comprises an entry in the list of datastore names and an associated
    named section in the body of the config where the name of the section matches the name
    entered in the list of datastores. This way we can easily retrieve a list of datastores
    which enables us to process the rest of the configuration.
    """
    global current, config_pathname
    conf = current

    datastores = current.sections()
    
    if db_name not in datastores:
        datastores.append(db_name)
        conf[db_name] = {}
        conf[db_name]['ip'] = '127.0.0.1'
        conf[db_name]['port'] = '5984'
        conf[db_name]['protocol'] = 'http'
        conf[db_name]['username'] = 'admin'
        conf[db_name]['password'] = 'password'

        with open(config_pathname, 'w') as config_file:
            conf.write(config_file)

        current = conf
        return True

def remove_datastore_config_entry(db_name):
    """
    Removes the configuration entry for a given datastore.
    """
    global current, config_pathname
    conf = current

    datastores = current.sections()
    if db_name in datastores:
        datastores.remove(db_name)
        conf.remove_section(db_name)

        with open(config_pathname, 'w') as cfile:
            conf.write(cfile)

        current = conf
   


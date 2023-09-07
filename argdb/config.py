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
        cp['datastore'] = {'name':'argdb', 'path':'.'}
        cp['gui'] = {'port':'8080'}
        cp['api'] = {'port':'5000'}
        cp.write(open(config_pathname, 'w'))


def get_config_name():
    return config_pathname


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



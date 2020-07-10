#!/usr/bin/python

import argparse

from . import argdb
from . import config


def process(args):
    """
    Process arguments passed in from the command linke
    """
    print("ArgDB Command Line UI")
    print()
    if args.generate:
        print("Generating a configuration file for you...")
        config.generate_default()
        exit(1)

    if args.config:
        argdb.init(args.config)
        print(argdb.info())
        print()

        if args.datastore:
            print("Adding the following datastore: "+str(args.datastore))
            argdb.add_datastore(args.datastore)
            exit(1)

        if args.removedatastore:
            print()
            db_name = args.removedatastore
            if argdb.delete_datastore(db_name):
                print("Deleting the following datastore: " + db_name)
            else:
                print("There doesn't appear to be a datastore named: " + db_name)
            print(argdb.info())
            exit(1)
    else:
        print("You didn't supply a configuration file. If you don't have one then perhaps you want to generate one?")
   


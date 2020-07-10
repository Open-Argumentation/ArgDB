#!/usr/bin/python

import argparse
import sadface

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

        if args.add_datastore:
            print("Adding the following datastore: "+str(args.add_datastore))
            argdb.add_datastore(args.add_datastore)
            exit(1)

        if args.remove_datastore:
            print()
            db_name = args.remove_datastore
            if argdb.delete_datastore(db_name):
                print("Deleting the following datastore: " + db_name)
            else:
                print("There doesn't appear to be a datastore named: " + db_name)
            print(argdb.info())
            exit(1)

        if args.datastore:
            print("Using the following datastore: " + args.datastore)
            if args.add_document:
                print("Adding a sadface document to: "+ args.datastore)
                argdb.add_doc(args.datastore, args.add_document)
            elif args.remove_document:
                print("Deleting a sadface document from: "+ args.datastore)
                argdb.delete_doc(args.datastore, args.remove_document)
            elif args.get_document:
                doc = argdb.get_doc(args.datastore, args.get_document)
                print(sadface.prettyprint(doc))
                

            
    else:
        print("You didn't supply a configuration file. If you don't have one then perhaps you want to generate one?")
   


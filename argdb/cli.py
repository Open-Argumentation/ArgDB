#!/usr/bin/python

import argparse
import json

from . import argdb
from . import config


def process(args):
    """
    Process arguments passed in from the command linke
    """
    if args.generate:
        print("Generating a configuration file for you...")
        config.generate_default()
        exit(1)


        """
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
       """  

            
    else:
        print("Nothing to do.")
        print("Cleaning up.")
        print("Stopping ArgDB...")
   


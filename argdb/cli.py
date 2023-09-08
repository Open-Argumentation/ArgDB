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
        argdb.cleanup()


    if args.add_document:
        print("Adding document to datastore...")
        argdb.add_doc(args.add_document)
        argdb.cleanup()

    if args.delete_document:
        print("Deleting document from datastore...")
        argdb.delete_doc(args.delete_document)
        argdb.cleanup()

    if args.get_document:
        print("Retrieving document from datastore...")
        doc = argdb.get_doc(args.get_document)
        if doc is not None:
            print(doc)
        argdb.cleanup()
            

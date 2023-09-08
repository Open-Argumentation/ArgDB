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
        config.generate_default()
        argdb.cleanup()

    if args.add_document:
        argdb.add_doc(args.add_document)
        argdb.cleanup()

    if args.load_document:
        with open(args.load_document) as sadface_file:
            sfdoc = json.dumps(json.load(sadface_file))
            argdb.add_doc(sfdoc)
            argdb.cleanup()

    if args.delete_document:
        argdb.delete_doc(args.delete_document)
        argdb.cleanup()

    if args.get_document:
        doc = argdb.get_doc(args.get_document)
        if doc is not None:
            print(doc)
        argdb.cleanup()

    if args.tabula_rasa:
        argdb.clear()
            

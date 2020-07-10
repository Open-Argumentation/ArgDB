#!/usr/bin/python

import argparse

from . import argdb

def process(args):
    """
    Process arguments passed in from the command linke
    """
    if args.config:
        argdb.init(args.config)
        print(argdb.info())
        

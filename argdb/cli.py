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
    else:
        print("You didn't supply a configuration file. If you don't have one then perhaps you want to generate one?")
   


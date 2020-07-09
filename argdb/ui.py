#!/usr/bin/python

from . import argdb

import argparse
import cmd

def main():
    parser = argparse.ArgumentParser(description="This is the ArgDB Python tool")
    parser.add_argument("-w", "--web", help="Launch the Web UI", action="store_true")

    args = parser.parse_args()

    if args.web:
        print("ArgDB Web UI")

    else:
        print("ArgDB CLI UI")

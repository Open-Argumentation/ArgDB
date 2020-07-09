#!/usr/bin/python

from . import argdb

import argparse
import cmd

def web():
    """
    Launch a pywebview and bottle powered web-based UI for ArgDB
    """
    import webview
    webview.create_window('Hello world', 'https://pywebview.flowrl.com/hello')
    webview.start()


def main():
    parser = argparse.ArgumentParser(description="This is the ArgDB Python tool")
    parser.add_argument("-i", "--interactive", help="Use the ArgDB REPL (WARNING EXPERIMENTAL)", action="store_true")
    parser.add_argument("-w", "--web", help="Launch the Web UI", action="store_true")

    args = parser.parse_args()

    if args.web:
        print("Launching ArgDB Web UI...")
        web()
        
    elif args.interactive:
        print("ArgDB Interactive REPL")
    else:
        print("ArgDB CLI UI")
        

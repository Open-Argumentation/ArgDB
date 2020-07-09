#!/usr/bin/python

from . import argdb

import argparse
import cmd
from bottle import route, run, template
import webview
import threading

class Shell(cmd.Cmd):
    """
    The ArgDB REPL
    """

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(ArgDB) '
        self.intro = "The ArgDB REPL. Type 'help', '?', or 'help <command>' for assistance"

    def do_quit(self, line):
        """
        Quit the SADRace REPL.
        """
        return True

    def emptyline(self):
        pass
    
    do_q = do_quit


def cli(args):
    """
    Process arguments passed in from the command linke
    """
    pass

@route('/')
def root():
    return template('<b>Hello {{name}}</b>!', name='Simon')
    
def web():
    """
    Launch a pywebview and bottle powered web-based UI for ArgDB
    """
   
    thread = threading.Thread(target=run, kwargs=dict(host='localhost', port=8080))
    thread.daemon = True
    thread.start()

    webview.create_window("ArgDB", "http://localhost:8080", width=800, height=600, resizable=False)
    webview.start()
    

def main():
    parser = argparse.ArgumentParser(description="This is the ArgDB Python tool")
    parser.add_argument("-i", "--interactive", help="Use the ArgDB REPL (WARNING EXPERIMENTAL)", 
        action="store_true")
    parser.add_argument("-w", "--web", help="Launch the Web UI  (WARNING EXPERIMENTAL)", 
        action="store_true")

    args = parser.parse_args()

    if args.web:
        print("Launching ArgDB Web UI...")
        web()
        
    elif args.interactive:
        print("ArgDB Interactive REPL")
        Shell().cmdloop()

    else:
        print("ArgDB CLI UI")
        cli(args)
        
        

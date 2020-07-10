#!/usr/bin/python

from . import argdb
from . import webui
from . import cli

import argparse
import cmd

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

def main():
    parser = argparse.ArgumentParser(description="This is the ArgDB Python tool")
    parser.add_argument("-i", "--interactive", help="Use the ArgDB REPL (WARNING EXPERIMENTAL)", 
        action="store_true")
    parser.add_argument("-w", "--web", help="Launch the Web UI  (WARNING EXPERIMENTAL)", 
        action="store_true")

    parser.add_argument("-c", "--config", help="Specift a configuration file")

    args = parser.parse_args()

    if args.web:
        print("Launching ArgDB Web UI...")
        webui.launch()
        
    elif args.interactive:
        print("ArgDB Interactive REPL")
        Shell().cmdloop()

    else:
        print("ArgDB CLI UI")
        cli.process(args)
        
        

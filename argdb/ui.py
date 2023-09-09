#!/usr/bin/python

from . import argdb
from . import gui
from . import cli
from . import version

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

    parser.add_argument("-i", "--interactive", help="Use the ArgDB REPL (WARNING EXPERIMENTAL)", action="store_true")
    parser.add_argument("--gui", help="Launch the WebView GUI  (WARNING EXPERIMENTAL)", action="store_true")
    
    parser.add_argument("-c", "--config", help="Specify a configuration file")
    parser.add_argument("--generate", help="Generate a default configuration file", action="store_true")


    parser.add_argument("-a", "--add_document", help="Add the supplied SADface document string to the current datastore")
    parser.add_argument("-l", "--load_document", help="Add the supplied SADface document file to the current datastore")
    
    parser.add_argument("-d", "--delete_document", help="Delete a SADFace document, identifed by its ID")
    parser.add_argument("-g", "--get_document", help="Retrive a SADFace document, identified by its ID")
    parser.add_argument("--tabula-rasa", help="Empty the datastore of all contents", action="store_true")

    args = parser.parse_args()

    argdb.init(args.config)
    
    if args.gui:
        print("Launching ArgDB WebView GUI...")
        gui.launch(args)
        
    elif args.interactive:
        print("ArgDB Interactive REPL")
        Shell().cmdloop()

    else:
        cli.process(args)
    

    
        

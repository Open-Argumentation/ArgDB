# ArgDB

A Datastore for arguments

ArgDB is a datastore, API, and suite of tools for working with argument data represented using the Simple Argument Description Format (SADFace). The default backend datastore is SQLite3. This currently supports storage of raw SADFace documents in JSON format using the native JSON support within SQLite3. The CLI is a python flask application that provides two modes of interaction. The first is as a command line app, passing in and retrieving data from the store via command line arguments. This can be useful to script interaction with the datastore, treating ArgDB like any other command line tool. The second is a REPL mode that allows a user manipulate their argument datastore directly and interactively. The API is a Python-Flask web-app that provides a public interface to the datastore that is appropriate to the domain. The API is designed to serve the contents of the datastore publiclly if so exposed, i.e. serving using a compliant WSGI  server (uWSGI or Waitress are good choices), ideally proxied behind a static webserver like NGinX to provide TLS support. The GUI is a Pywebview web-app that provides a web-based user interface to the datastore. As for the API, this can be proxied publily or kept for private use.

## Usage


Running the CLI REPL:

~~~~
$ python -m argdb
~~~~

Running the (web) gui:

~~~~
$ python -m argdb --gui
~~~~


## History

Prior to version 0.1, ArgDB used CouchDB as the default backend. However, recent advances in support JSON within SQLite3 meant that a simpler implementation could be produced that could use a single backend to store raw SADFace documents, as well as a relational subset of SADFace that could be optimised for scalability and ad hoc search.



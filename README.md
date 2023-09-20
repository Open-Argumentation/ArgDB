# ArgDB

A Datastore for arguments

ArgDB is a datastore, API, and suite of tools for working with argument data represented using the Simple Argument Description Format (SADFace). The default backend datastore is SQLite3. This currently supports storage of raw SADFace documents in JSON format using the native JSON support within SQLite3. The CLI is a python flask application that provides two modes of interaction. The first is as a command line app, passing in and retrieving data from the store via command line arguments. This can be useful to script interaction with the datastore, treating ArgDB like any other command line tool. The second is a REPL mode that allows a user manipulate their argument datastore directly and interactively. The API is a Python-Flask web-app that provides a public interface to the datastore that is appropriate to the domain. The API is designed to serve the contents of the datastore publiclly if so exposed, i.e. serving using a compliant WSGI  server (uWSGI or Waitress are good choices), ideally proxied behind a static webserver like NGinX to provide TLS support. The GUI is a Pywebview web-app that provides a web-based user interface to the datastore. As for the API, this can be proxied publily or kept for private use.

## Usage


Running the Command Line Interface (CLI):

~~~~
$ python -m argdb
~~~~

This doesn't actually do much as the CLI relies on passing in documents or queries and receiving back a result from the datastore. So use the help option to find out a bit more:

~~~~
$ python -m argdb -h
~~~~

Note that the CLI is designed to be used either in the terminal, either directly, or as part of command pipeline. For example, using SADFace, or some other tool to generate a SADFace document containing argumentative data, and then storing it in the ArgDB datastore.


Running the (web) gui:

~~~~
$ python -m argdb --gui
~~~~

Running the (web) API:

~~~~
$ python -m argdb --api
~~~~
This starts a JSON-RPC API on the port specified in your argdb.cfg file. This port defaults to 5000. The API is a fully functional WSGI web-app, so can be used to expose an ArgDB datastore publiclly to the wider world.





## History

Prior to version 0.1, ArgDB used CouchDB as the default backend. However, recent advances in support JSON within SQLite3 meant that a simpler implementation could be produced that could use a single backend to store raw SADFace documents, as well as a relational subset of SADFace that could be optimised for scalability and ad hoc search.



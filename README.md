# ArgDB

A Datastore for arguments

ArgDB is a datastore, API, and suite of tools for working with argument data represented using the Simple Argument Description Format (SADFace). The default backend datastore is SQLite3. This currently supports storage of raw SADFace documents in JSON format using the native JSON support within SQLite3. The CLI is a python flask application that provides two modes of interaction. The first is as a command line app, passing in and retrieving data from the store via command line arguments. This can be useful to script interaction with the datastore, treating ArgDB like any other command line tool. The second is a REPL mode that allows a user manipulate their argument datastore directly and interactively. The API is a Python-Flask web-app that provides a public interface to the datastore that is appropriate to the domain. The API is designed to serve the contents of the datastore publiclly if so exposed, i.e. serving using a compliant WSGI  server (uWSGI or Waitress are good choices), ideally proxied behind a static webserver like NGinX to provide TLS support. The GUI is a Pywebview web-app that provides a web-based user interface to the datastore. As for the API, this can be proxied publily or kept for private use.

## Usage


### Running the Command Line Interface (CLI):

~~~~
$ python -m argdb
~~~~

This doesn't actually do much as the CLI relies on passing in documents or queries and receiving back a result from the datastore. So use the help option to find out a bit more:

~~~~
$ python -m argdb -h
~~~~

Note that the CLI is designed to be used either in the terminal, either directly, or as part of command pipeline. For example, using SADFace, or some other tool to generate a SADFace document containing argumentative data, and then storing it in the ArgDB datastore.

The core functionality for a datastore are the so-called CRUD operations, Create, Retrieve, Update, and Delete. These are at the core of ArgDB's functionality. Let's explore them:

You can add a document to an ArgDB datastore in two ways, by supplying it as a string using the add function or by loading in a document from a file. We'll look at each in turn. Assuming you have a well formed SADFace document to hand then the following should work to add a SADFace document to your ArgDB datastore (Note that the supplied JSON in the example isn't a valid document and would actually be rejected):

~~~~
$ python -m argdb -a '{"valid":"SADFace","demo":"document"}'
~~~~

Under normal circumstances though, this usage would be via a scripted interaction rather than a human command line interaction. The other way is to take a SADFace document stored in a file, that, for example, might have been exported from the MonkeyPuzzle tool, and load it into SADFace:

~~~~
$ python -m argdb -l FILEPATH-TO-SADFACE-DOCUMENT
~~~~

The load feature won't allow you to add a document whose ID matches an existing document in ArgDB. If you do want to do this, then the overwrite feature let's you replace an existing SADFace document with a new one like so:

~~~~
$ python -m argdb -o FILEPATH-TO-SADFACE-DOCUMENT
~~~~


Once you have a document stored in the ArgDB you can then delete it by supplying the SADFace UUID for the target document as follows:

~~~~
$ python -m argdb -d "12345678-1234-5678-1234-567812345678"
~~~~

To retrieve a document, once added to the ArgDB, supply it's UUID

~~~~
$ python -m argdb -g "12345678-1234-5678-1234-567812345678"
~~~~




### Running the REPL environment (experimental | development path):

~~~~
$ python -m argdb --gui
~~~~

This provides similar functionality to the CLI version, but instead of being optimised for scripted usage, this uses a dedicated, ArgDB read-evaluate-print-loop (REPL) environment within which you can work with your ArgDB datasets. This is part of the experimental development path and functionality is rudimentary at present.

### Running the (web) GUI (experimental | development path):

~~~~
$ python -m argdb --gui
~~~~

This causes a PyWebView based GUI to be displayed. This uses the native browser of your system to display the interface and is a lightweight method to distribute a web-based tool, packaged for the deskop but without including an entire browser. This is part of the experimental development path and functionality is rudimentary at present.


### Running the (web) API (experimental | development path):

~~~~
$ python -m argdb --api
~~~~

This starts a JSON-RPC API on the port specified in your argdb.cfg file. This port defaults to 5000. The API is a fully functional WSGI web-app, so can be used to expose an ArgDB datastore publiclly to the wider world. This is part of the experimental development path and functionality is rudimentary at present.


### Running the (web) search GUI  (experimental | development path)

~~~~
$ python -m argdb --web
~~~~

This starts a dynamic WSGI web-app that presents the ArgDB search GUI in a manner suitable for deploying publicly. This is part of the experimental development path and functionality is rudimentary at present.



## History

Prior to version 0.1, ArgDB used CouchDB as the default backend. However, recent advances in support JSON within SQLite3 meant that a simpler implementation could be produced that could use a single backend to store raw SADFace documents, as well as a relational subset of SADFace that could be optimised for scalability and ad hoc search.



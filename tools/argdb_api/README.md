ArgDB API
=========

This is a HTTP-based API for working with the ArgDB datastore.

Running
=======

The ArgDB API should be deployed using uWSGI as the app server but it should run perfectly happily using the Flask development server. Assuming that you have Pip, VirtualEnv and CouchDB installed, cd into the argdb_api/ directory then create a new virtualenv:
    $ cd argdb_api/
    $ virtualenv env

Start your virtualenv then install the external libraries using the supplied requirements.txt
    $ source env/bin/activate
    $ pip install -r requirements.txt

Now create a var/ directory to store log files from the running app and create an empty log file ready for data:
    $ mdkir var
    $ touch var/argdb_api.log

Start your CouchDB instance (we assume that once running it is available on localhost:5984). If not you may have to adjust the settings in argdb_api/etc/defaults.cfg
    $ couchdb

We want the ArgDB API to run with the src directory as a sub-directory of our application root (mainly so that the etc/ and var/ directories are located correctly relative to the runing app) so cd to argdb_api then start the app:
    $ python src/argdb_api.py

Now open a browser and navigate to http://localhost:5000/

Run the tests
-------------

Add application src to the PYTHONPATH:
    $ PYTHONPATH=`pwd`/src/argdb_api

Run the tests:
    $ python test/test.py

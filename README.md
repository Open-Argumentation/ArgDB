# ArgDB
A Datastore for arguments

ArgDB is a datastore, API, and tools for working with argument data. The default backend datastore is couchDB but this can be swapped for any other store that is performant for the kind of problem that you are working on. The backend stores arguments and their constituent elements. The API is a Python-Flask web-app that provides a public interface to the datastore that is appropriate to the domain.

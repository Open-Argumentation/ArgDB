#!/usr/bin/python

from . import argdb

from bottle import route, run, template
import webview
import threading

@route('/')
def root():
    return template('<b>Hello {{name}}</b>!', name='Simon')
    
def launch():
    """
    Launch a pywebview and bottle powered web-based UI for ArgDB
    """
   
    thread = threading.Thread(target=run, kwargs=dict(host='localhost', port=8080))
    thread.daemon = True
    thread.start()

    webview.create_window("ArgDB", "http://localhost:8080", width=800, height=600, resizable=False)
    webview.start()
    

from __future__ import absolute_import
import os

class PrefixMiddleware(object):
    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        print(environ['PATH_INFO'])
        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]

# Needed if a settings.py file exists
os.environ['PUPPETBOARD_SETTINGS'] = '/etc/puppetboard/settings.py'
from puppetboard.app import app
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/puppetboard')

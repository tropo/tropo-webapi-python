#!/usr/bin/env python

# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

from itty import *
from tropo_web_api import Tropo, Session

@post('/index.json')
def index(request):
    s = Session(request.body)
    t = Tropo()
    t.say(['hello world!', 'how are you doing?'])
    return t.RenderJson()

run_itty(server='wsgiref', host='0.0.0.0', port=8888)


#!/usr/bin/env python

from itty import *
from tropo_web_api import Tropo

@post('/index.json')
def index(request):
    t = Tropo()
    t.say(['hello workd!', 'how are you doing?'])
    return t.RenderJson()

run_itty(server='wsgiref', host='0.0.0.0', port=8888)


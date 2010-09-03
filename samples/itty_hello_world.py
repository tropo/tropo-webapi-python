#!/usr/bin/env python

from itty import *
from tropo import Tropo, Session

@post('/index.json')
def index(request):
    s = Session(request.body)
    t = Tropo()
    t.say(['hello workd!', 'how are you doing?'])
    return t.RenderJson()

run_itty(server='wsgiref', host='0.0.0.0', port=8888)


#!/usr/bin/env python

from itty import *
from tropo import Tropo
import datetime



@post('/index.json')
def index(request):
    currenttime = datetime.datetime.now()
    t = Tropo()
    sayobjOutbound = "Now is " + str(currenttime)
    t.message(sayobjOutbound, to="+1 725-419-2113", network="SMS")
    print t.RenderJson()
    return t.RenderJson()

run_itty(server='wsgiref', host='192.168.26.1', port=8041)
#run_itty(config='sample_conf')
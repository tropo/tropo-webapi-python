#!/usr/bin/env python
"""
Hello world script for Session API ( https://www.tropo.com/docs/webapi/sessionapi.htm )

Upon launch, it will trigger a message to be sent via Jabber to the addess specified in
'number'.
"""

# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

from itty import *
from tropo import Tropo, Session, JoinPrompt, LeavePrompt
from urllib import urlencode
from urllib2 import urlopen

@post('/index.json')
def index(request):
    session = Session(request.body)
    print 'request.body begin'
    print request.body
    print 'request.body end'
    t = Tropo()
    #t.call(to=session.parameters['callToNumber'], network='SIP')
    dhhm = session.parameters['callToNumber']
    say_obj = session.parameters['message252121']
    #t.message(say_obj, to=dhhm, network="SMS", _from="+17754641173", channel = "TEXT")
    #t.call(dhhm, network="SMS", _from="+17754641173", channel = "TEXT")
    t.call(dhhm)
    t.say(say_obj)
    print t.RenderJson()
    return t.RenderJson()

run_itty(server='wsgiref', host='192.168.26.1', port=8043)
#run_itty(config='sample_conf')
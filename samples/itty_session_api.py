#!/usr/bin/env python
"""
Hello world script for Session API ( https://www.tropo.com/docs/webapi/sessionapi.htm )

Upon launch, it will trigger a message to be sent via Jabber to the addess specified in
'number'.
"""

# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

from itty import *
from tropo_webapi import Tropo, Session
from urllib import urlencode
from urllib2 import urlopen

@post('/index.json')
def index(request):
    session = Session(request.body)
    t = Tropo()
    t.call(to=session.parameters['numberToDial'], network='JABBER')
    t.say(session.parameters['message'])
    return t.RenderJson()


base_url = 'http://api.tropo.com/1.0/sessions'
token = 'xxxxxxxxxx'		# Insert your token here
action = 'create'
number = 'username@domain'	# change to the Jabber ID to which you want to send the message
message = 'hello from the session API!'

params = urlencode([('action', action), ('token', token), ('numberToDial', number), ('message', message)])
data = urlopen('%s?%s' % (base_url, params)).read()

run_itty(server='wsgiref', host='0.0.0.0', port=8888)


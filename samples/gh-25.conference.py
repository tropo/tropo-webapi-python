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
    t = Tropo()
    #jj = JoinPrompt(value = "who are you who let you come in")
    jj = JoinPrompt("who are you who let you come in")
    #ll = LeavePrompt(value = "byebye samsung")
    ll = LeavePrompt("byebye samsung")
    t.call(to=session.parameters['callToNumber'], network='SIP')
    t.conference(id='yuxiangj', joinPrompt=jj.json, leavePrompt=ll.json)
    t.say(session.parameters['message'])
    return t.RenderJsonSDK()


#base_url = 'http://api.tropo.com/1.0/sessions'
base_url = 'http://192.168.26.21:8080/gateway/sessions'
token = '7776687947547a6261677359524e665670427145574f544e44616b5a64456d6c526b576265647448516e796c'		# Insert your token here
action = 'create'
#number = 'sip:xiangjun_yu@10.140.254.55:5678'	# change to the Jabber ID to which you want to send the message
number = 'sip:frank@172.16.22.128:5678'	# change to the Jabber ID to which you want to send the message
message = 'hello from the session API!'

params = urlencode([('action', action), ('token', token), ('callToNumber', number), ('message', message)])
data = urlopen('%s?%s' % (base_url, params)).read()

#run_itty(server='wsgiref', host='0.0.0.0', port=8888)
run_itty(config='sample_conf')


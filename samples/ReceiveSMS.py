#!/usr/bin/env python

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
    smsContent = session.initialText
    #t.call(to=session.parameters['callToNumber'], network='SIP')
    #t.say(session.parameters['message'])
    """
    t = Tropo()
    t.call(to="xiangjun_yu@192.168.26.1:5678")
    t.say("wo shi yi ke xiao xiao cao")
    """
    #base_url = 'http://192.168.26.21:8080/gateway/sessions'
    base_url = 'https://api.tropo.com/1.0/sessions'
    #token = '4c586866434c4c59746f4361796b634477600d49434d434874584d4546496e70536c706749436841476b684371'		# Insert your token here  Application ID: 301
    token = '6c77565670494a6b474f646a5658436b514658724a0055674f4e735041764f665463626b535472616869746768'		# Insert your fire-app-with-token.py token here
    action = 'create'
    #number = 'sip:xiangjun_yu@10.140.254.55:5678'	# change to the Jabber ID to which you want to send the message
    #number = 'sip:frank@172.16.22.128:5678'	# change to the Jabber ID to which you want to send the message
    #number = '+861891020382'	# change to the Jabber ID to which you want to send the message
    number = '+86134766549249'	# change to the Jabber ID to which you want to send the message
    message = 'redirect by Python content is ' + str(smsContent)
    
    params = urlencode([('action', action), ('token', token), ('callToNumber', number), ('message252121', message)])
    data = urlopen('%s?%s' % (base_url, params)).read()
    
    print 'data is '
    print data
    #return t.RenderJson()
    return "receive SMS successfully"

run_itty(server='wsgiref', host='192.168.26.1', port=8042)
#run_itty(config='sample_conf')
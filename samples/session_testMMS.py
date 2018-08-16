#!/usr/bin/env python
"""
https://www.tropo.com/docs/webapi/session
"""

# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

import sys
sys.path = ['..'] + sys.path

from itty import *
from tropo import Tropo, Session, JoinPrompt, LeavePrompt

@post('/index.json')
def sessiontest(request):
    session = Session(request.body)
    print 'request.body is ' + request.body
    accountId = session.accountId
    callId = session.callId
    fromm = session.fromaddress
    headers = session.headers
    idd = session.id
    initialText = session.initialText
    if hasattr(session,'parameters'):
        parameters = session.parameters
    else:
        parameters = ''
    timestamp = session.timestamp
    too = session.to
    userType = session.userType
    
    subjectVar = session.subject
    if subjectVar:
        print subjectVar
        
    mediaList = session.initialMedia
    if mediaList:
        for i in range(len(mediaList)):
            print("mediaList {}: {}".format(i + 1, mediaList[i]))
    
    
    t = Tropo()
    t.say('accountId is ' + accountId)
    t.say('callId is ' + callId)
    
    fromid = fromm['id']
    frome164Id = fromm['e164Id']
    fromname = fromm['name']
    fromchannel = fromm['channel']
    fromnetwork = fromm['network']
    
    t.say('from id is ' + fromid)
    t.say('from e164Id ' + frome164Id)
    t.say('from name ' + str(fromname))
    t.say('from channel ' + fromchannel)
    t.say('from network ' + fromnetwork)
    
    t.say('id is ' + idd)
    t.say('initialText is ' + str(initialText))
    t.say('headers is ' + str(headers))
    t.say('parameters is ' + parameters)
    t.say('timestamp is ' + timestamp)
    
    tooid = too['id']
    too164Id = too['e164Id']
    tooname = too['name']
    toochannel = too['channel']
    toonetwork = too['network']
    
    t.say('to id is ' + tooid)
    t.say('to e164Id ' + too164Id)
    t.say('to name ' + str(tooname))
    t.say('to channel ' + toochannel)
    t.say('to network ' + toonetwork)
    
    t.say('userType is ' + userType)
    
    if("frank" in str(fromname)):
        t.say('hello frank ')
    else:
        t.say('sorry you are not frank')
    
    json = t.RenderJson()
    print json
    return json

#run_itty(server='wsgiref', host='0.0.0.0', port=8888)
run_itty(config='sample_conf')


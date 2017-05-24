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

@post('/continue.json')
def index(request):
    t = Tropo()
    t.say("I am continue")
    json = t.RenderJsonSDK()
    print json
    return json


@post('/error.json')
def index(request):
    t = Tropo()
    t.say("I am error")
    json = t.RenderJsonSDK()
    print json
    return json


@post('/hangup.json')
def index(request):
    t = Tropo()
    t.say("I am hangup")
    json = t.RenderJsonSDK()
    print json
    return json


@post('/incomplete.json')
def index(request):
    t = Tropo()
    t.say("I am incomplete")
    json = t.RenderJsonSDK()
    print json
    return json


@post('/index.json')
def index(request):
    t = Tropo()
    t.on("continue", next="/continue.json", post = 'http://192.168.26.88:8080/FileUpload/receiveJson', say = "this is say in on function")
    t.on("error", next = "/error.json")
    t.on("hangup", next = "/hangup.json")
    t.on("incomplete", next = "/incomplete.json")
    t.ask(say = "Welcome to Tropo.  What's your birth year?", name = "year", require = "true", choices = "[4 DIGITS]")
    json = t.RenderJsonSDK()
    print json
    return json


run_itty(config='sample_conf')


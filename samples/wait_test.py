import sys
sys.path = ['..'] + sys.path
from itty import *
from tropo import Tropo, Session, Result

@post('/index')
def index(request):

    t = Tropo()
    t.call("sip:frank@172.16.22.128:5678")
    t.say("tropo status")
    t.wait(27222, allowSignals = 'dfghjm')
    t.say("today is Friday 2017-06-02")
    return t.RenderJson()

run_itty(server='wsgiref', host='192.168.26.1', port=8086)

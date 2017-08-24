import sys
sys.path = ['..'] + sys.path
from itty import *
from tropo import Tropo


@post('/index.json')
def index(request):
    t = Tropo()
    t.answer(headers={"P-Header":"value goes here","Remote-Party-ID":"\"John Doe\"<sip:jdoe@foo.com>;party=calling;id-type=subscriber;privacy=full;screen=yes"})
    t.say('This is your mother. Did you brush your teeth today?')
    json = t.RenderJson() 
    print json
    return json


run_itty(server='wsgiref', host='192.168.26.1', port=8888)



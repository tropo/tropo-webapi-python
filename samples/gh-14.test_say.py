# tests fix of gh-14 for "_as" parameter in the "say" function. 
# Proposed convention is to use "_from" as the parameter
# so as not to conflict with "from" Python reserved word.




# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

import sys
sys.path = ['..'] + sys.path

from itty import *
from tropo import Tropo, Session

@post('/index.json')
def index(request):
    t = Tropo()
    t.say('12345', _as='DIGITS', voice='dave', promptLogSecurity='suppress')
    t.say('s s s s f f f ', promptLogSecurity='suppress')
    t.say(["Hello, World", "How ya doing?"], promptLogSecurity = "suppredd")
    json = t.RenderJson()
    print json
    print 'sys.path is %s' % sys.path
    return json


run_itty(server='wsgiref', host='192.168.26.1', port=8083)


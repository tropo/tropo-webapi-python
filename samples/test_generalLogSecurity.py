# tests fix of gh-14 for "_as" parameter in the "say" function. 
# Proposed convention is to use "_from" as the parameter
# so as not to conflict with "from" Python reserved word.




# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

from itty import *
from tropo import Tropo, Session

@post('/index.json')
def index(request):
#    s = Session(request.body)
    t = Tropo()
    t.say('12345466974710071', _as='DIGITS')
    t.generalLogSecurity('suppress')
    t.say('line 20 should be suppressed')
    t.generalLogSecurity('none')
    t.say('line 22 should be logged')
    t.generalLogSecurity('suppress')
    t.say('line 24 is not logged')
    t.generalLogSecurity('none')
    t.say('line 26 will be logged')
    json = t.RenderJson()
    print json
    return json


run_itty(config='sample_conf')


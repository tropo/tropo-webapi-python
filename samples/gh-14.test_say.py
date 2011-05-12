# tests fix of gh-14 for "_as" parameter in the "say" function. 
# Proposed convention is to use "_from" as the parameter
# so as not to conflict with "from" Python reserved word.




# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

from itty import *
from tropo import Tropo, Session

@post('/index.json')
def index(request):
    s = Session(request.body)
    t = Tropo()
    t.say('12345', _as='DIGITS', voice='dave')
    json = t.RenderJson()
    print json
    return json


run_itty()


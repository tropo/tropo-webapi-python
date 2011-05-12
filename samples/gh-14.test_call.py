# tests fix of gh-14 for "from" parameter in the "call" function. 
# Proposed convention is to use "_from" as the parameter
# so as not to conflict with "from" Python reserved word.

# _from arg works

# Invoke using a token

# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

from itty import *
from tropo import Tropo, Session

TO_NUMBER = '1xxxxxxxxxx'
FROM_NUMBER = '1yyyyyyyyyy'


@post('/index.json')
def index(request):
    s = Session(request.body)
    t = Tropo()
    t.call(to='tel:+' + TO_NUMBER, _from='tel:+' + FROM_NUMBER)
    t.say('This is your mother. Did you brush your teeth today?')
    json = t.RenderJson()
    print json
    return json


run_itty()


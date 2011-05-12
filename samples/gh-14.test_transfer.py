# tests fix of gh-14 for "from" parameter in the "transfer" function. 
# Proposed convention is to use "_from" as the parameter
# so as not to conflict with "from" Python reserved word.

# _from arg works
# _from arg works with straight json

# Invoke by calling up app access number

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
    t.say ("One moment please.")
    t.transfer(TO_NUMBER, _from="tel:+" + FROM_NUMBER)
    t.say("Hi. I am a robot")
    json = t.RenderJson()
    print json
    return json


run_itty()


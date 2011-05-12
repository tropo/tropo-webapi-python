# tests fix of gh-14. Proposed convention is to use "_as" as
# the attribute in "say" function, so as not to conflict with "as"
# Python reserved word.

# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

from itty import *
from tropo import Tropo, Session

@post('/index.json')
def index(request):
    s = Session(request.body)
    t = Tropo()
    t.say('12345', _as='DIGITS', voice='allison')
    json = t.RenderJson()
    print json
    return json

run_itty()

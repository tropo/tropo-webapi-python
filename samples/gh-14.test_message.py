# tests fix of gh-14 for "_from" parameter in the "message" function. 
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
        t = Tropo()
        t.message("Hello World", TO_NUMBER, channel='VOICE', _from='tel:+' + FROM_NUMBER)
	json = t.RenderJson()
	print json
	return json
#retest


run_itty()


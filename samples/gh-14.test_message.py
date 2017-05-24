# tests fix of gh-14 for "_from" parameter in the "message" function. 
# Proposed convention is to use "_from" as the parameter
# so as not to conflict with "from" Python reserved word.

# _from arg works

# Invoke using a token

# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

from itty import *
from tropo import Tropo, Session

TO_NUMBER = 'sip:frank@172.16.22.128:5678'
FROM_NUMBER = 'sip:xiangjun_yu@192.168.26.21:5678'


@post('/index.json')
def index(request):
        t = Tropo()
	t.message("Hello World from tylor", TO_NUMBER, channel='VOICE', _from='' + FROM_NUMBER, promptLogSecurity='sss')
	json = t.RenderJson()
	print json
	return json
#retest


run_itty(config='sample_conf')


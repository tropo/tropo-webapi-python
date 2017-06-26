# tests fix of gh-14 for "from" parameter in the "transfer" function. 
# Proposed convention is to use "_from" as the parameter
# so as not to conflict with "from" Python reserved word.

# _from arg works
# _from arg works with straight json

# Invoke by calling up app access number

# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

import sys
sys.path = ['..'] + sys.path
from itty import *
from tropo import Tropo, Session, On, TransferOnChoices, Ask, Choices

TO_NUMBER = 'sip:frank@172.16.22.128:5678'
FROM_NUMBER = 'sip:xiangjun_yu@192.168.26.1:5678'


@post('/index.json')
def index(request):
    t = Tropo()
    t.call("sip:xiangjun_yu@192.168.26.1:5678", say = "ha ha ha ha ha ah ah ah ah")
    t.say("ah ah ah ah ah uh uh uh uh ha ha ha")
    on1 = On("connect", ask = Ask(Choices("[5 DIGITS]")).json).json
    on2 = On("ring", say = "emily2").json
    t.transfer(TO_NUMBER, _from= FROM_NUMBER, on=[on1,on2], choices = TransferOnChoices(terminator = '#').json)
    t.say("Hi. I am a robot")
    json = t.RenderJson()
    print json
    return json


run_itty(config='sample_conf')


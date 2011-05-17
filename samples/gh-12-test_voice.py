# tests fix of gh-12 . Need a way to set the default voice
# for a Tropo object.
# added a new method "setVoice" on the Tropo object

# These examples show precdence of setVoice vs using "voice="..." in 
# the method call.

# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

from itty import *
from tropo import Tropo, Session, TropoAction, Choices

@post('/index.json')
def index(request):
    s = Session(request.body)
    t = Tropo()
    t.setVoice('dave')
    # we use what has been set in Tropo object
    t.say(['hello world!'])
    # we use what is set in the method call
    t.say(['hello world!'], voice="allison")

    # we use the voice that has been set in Tropo object
    choices = Choices("[5 digits]").obj
    t.ask(choices,
              say="Please enter your 5 digit zip code.",
              attempts=3, bargein=True, name="zip", timeout=5)

    # we use the voice passed in the method call.
    choices = Choices("[5 digits]").obj
    t.ask(choices,
              say="Please enter your 5 digit zip code.",
              attempts=3, bargein=True, name="zip", timeout=5, voice="allison")


    json = t.RenderJson()
    print json
    return json


run_itty()


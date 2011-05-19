# tests fix of gh-21 . Sorting out syntax of choices for ask.

# Fixed an error in the way the Ask class init function was
# taking apart the choices argument passed to it.

# Then, I corrected the original example provided for gh-21.
# Correct way to provide "choices" argument to "ask" is shown in 
# the example below.


# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

from itty import *
from tropo import Tropo, Session, Result, Choices


@post('/index.json')
def index(request):

	t = Tropo()

        choices = Choices("[4-5 DIGITS]", mode="dtmf", terminator = "#")
	t.ask(choices, timeout=15, name="digit", say = "What's your four or five digit pin? Press pound when finished.")

	t.on(event = "continue", next ="/continue")

        json = t.RenderJson()

        print json
	return json

@post("/continue")
def index(request):

	r = Result(request.body)        
        print "Result : %s" % r
#        dump(r)
	t = Tropo()

	answer = r.getInterpretation()

	t.say("You said ")
	t.say (answer, _as="DIGITS")

        json = t.RenderJson()
        print json
	return json

run_itty()


# tests fix of gh-20 . Extracting out of Result

# Added a new method on the Result object, called getInterpretation()


# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

from itty import *
from tropo import Tropo, Session, Result


@post('/index.json')
def index(request):

	t = Tropo()

	t.ask(choices = "yes(yes,y,1), no(no,n,2)", timeout = 15, name = "directory", minConfidence = 1, attempts = 3, say = "Are you trying to reach the sales department??")

	t.on(event = "continue", next ="/continue")

        json = t.RenderJson()

        print json
	return json

@post("/continue")
def index(request):

	r = Result(request.body)        
        print "Result : %s" % r

	t = Tropo()

	answer = r.getInterpretation()
	value = r.getValue()

	t.say("You said " + answer + ", which is a " + value)

        json = t.RenderJson()
        print json
	return json

run_itty()

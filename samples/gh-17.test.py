from itty import *
from tropo import Tropo, Result

# Fixes issue gh-17 getValue() should work with "value" property
# and not "interpretation"

@post('/index.json')
def index(request):
	t = Tropo()
	t.ask(choices = "yes(yes,y,1), no(no,n,2)", timeout=60, name="reminder", say = "Hey, did you remember to take your pills?")	
	t.on(event = "continue", next ="/continue")
	t.on(event = "incomplete", next ="/incomplete")
	json = t.RenderJson()
	print json
	return json

@post("/continue")
def index(request):
	r = Result(request.body)
	t = Tropo()

	answer = r.getValue()

	t.say("You said " + str(answer))

	if answer == "yes" :
		t.say("Ok, just checkin.")
	else :
		t.say("What are you waiting for?")

	json = t.RenderJson()
	print json
	return json

@post("/incomplete")
def index(request):
	t = Tropo()
	t.say("Sorry, that wasn't on of the options.")
	json = t.RenderJson()
	print json
	return json

run_itty()

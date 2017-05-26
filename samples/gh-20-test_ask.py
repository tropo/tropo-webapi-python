# tests fix of gh-20 . Extracting out of Result

# Added a new method on the Result object, called getInterpretation()


# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

import sys
sys.path = ['..'] + sys.path
from itty import *
from tropo import Tropo, Session, Result


@post('/index.json')
def index(request):

	t = Tropo()

	t.ask(choices = "yes(yes,y,1), no(no,n,2)", timeout = 15, name = "directory", minConfidence = 1, attempts = 3, say = "Are you trying to reach the sales department??")
	
        t.ask(choices = "red(red,1), blue(blue,2)", timeout = 15, name = "color", minConfidence = 1, attempts = 3, say = "What color do you like??")

	t.on(event = "continue", next ="/continue")

        json = t.RenderJson()

        print json
	return json

@post("/continue")
def index(request):

	r = Result(request.body)        
        print "request.body : %s" % request.body

	t = Tropo()

	answer = r.getInterpretation()
	value = r.getValue()
        
	t.say("You said " + answer + ", which is a " + value)
        
        actions_options_array = ['name', 'attempts', 'disposition', 'confidence', 'interpretation', 'utterance', 'value', 'concept', 'xml', 'uploadStatus']
        actions = r.getActions()
	if (type (actions) is list):
	     for item in actions:
		for opt in actions_options_array:
                    print 'action object filed %(actionfieldname)s\'s value is %(vaalue)s' % {'actionfieldname':opt, "vaalue":item.get(opt,'NoValue')}
                print '------------------------------'
             
       	else:
            dict = actions
	    for opt in actions_options_array:
                print 'action object filed %(actionfieldname)s\'s value is %(vaalue)s' % {'actionfieldname':opt, "vaalue":dict.get(opt,'NoValue')}
        
        json = t.RenderJson()
        print json
	return json

run_itty(server='wsgiref', host='192.168.26.1', port=8082)

from itty import *
from tropo import Tropo, Result, MachineDetection

@post('/index.json')
def index(request):

  t = Tropo()

  mc = MachineDetection(introduction="This is a test. Please hold while I determine if you are a Machine or Human. Processing. Finished. THank you for your patience.", voice="Victor").json
  t.call(to="+14071234321", machineDetection=mc)
  
  t.on(event="continue", next="/continue.json")

  return t.RenderJson()

@post("/continue.json")
def index(request):

  r = Result(request.body)
  t = Tropo()

  userType = r.getUserType()

  t.say("You are a " + userType)

  return t.RenderJson()

run_itty(server='wsgiref', host='0.0.0.0',   port=8888)
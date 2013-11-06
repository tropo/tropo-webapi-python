# tests fix of gh-22 . headers parameter for transfer()

# Fixes an error whereby we weren't passing 
# the "headers" parameter to transfer()

# Sample below shows how to pass in headers.


# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty


from itty import *
from tropo-webapi-python/tropo import Tropo, Session


#TO_NUMBER = '1xxxxxxxxxx'
TO_NUMBER = '16039570051'


@post('/index.json')
def index(request):

  s = Session(request.body)
  t = Tropo()

  t.say("Hello. , , , Transferring")
#  t.transfer(to="sip:9991489767@sip.tropo.com", headers={"x-callername":"Kevin Bond"})

  t.transfer(TO_NUMBER, headers={"x-callername":"Kevin Bond"})

  json = t.RenderJson()
  print json
  return json


run_itty()


